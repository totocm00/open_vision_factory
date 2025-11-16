import os
from datetime import datetime

import cv2

# 패키지(-m)로 실행할 때와, 단일 스크립트로 실행할 때 둘 다 지원
try:
    from .loader import load_camera_config, CameraConfig, BASE_DIR
except ImportError:  # python test_capture.py 로 직접 실행할 때
    from loader import load_camera_config, CameraConfig, BASE_DIR


def _normalize_key_char(raw: str, default: str) -> str:
    if not raw:
        return default
    key = str(raw).strip().lower()
    if key == "space":
        return " "
    if len(key) != 1:
        return default
    return key


def find_first_available_camera(min_index: int, max_index: int) -> int | None:
    print(f"[INFO] Auto searching cameras from {min_index} to {max_index}...")

    for idx in range(min_index, max_index + 1):
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            print(f"[OK] Camera found at index {idx}")
            cap.release()
            return idx
        cap.release()

    print("[WARN] No available camera found in given range.")
    return None


def open_camera(index: int, width: int, height: int) -> cv2.VideoCapture | None:
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        print(f"[ERROR] Failed to open camera index {index}")
        cap.release()
        return None

    if width > 0:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    if height > 0:
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

    print(f"[INFO] Opened camera index {index} ({width}x{height})")
    return cap


def get_save_dir(cfg: CameraConfig, override_subdir: str | None = None) -> str:
    """
    저장 경로: BASE_DIR / save_root_dir / (subdir)
    override_subdir를 넘기면 config의 save_subdir 대신 사용.
    """
    subdir = override_subdir or cfg.save_subdir
    root = os.path.join(BASE_DIR, cfg.save_root_dir)
    path = os.path.join(root, subdir) if subdir else root

    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        print(f"[INFO] Created directory: {path}")

    return path


def capture_frame(frame, cfg: CameraConfig, override_subdir: str | None = None) -> str:
    save_dir = get_save_dir(cfg, override_subdir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"capture_{timestamp}.jpg"
    filepath = os.path.join(save_dir, filename)

    cv2.imwrite(filepath, frame)
    print(f"[CAPTURE] Saved frame to: {filepath}")

    return filepath


def resolve_camera_index(cfg: CameraConfig) -> int | None:
    if cfg.auto:
        idx = find_first_available_camera(cfg.search_min_index, cfg.search_max_index)
        if idx is not None:
            return idx
        print("[WARN] Auto mode failed. Try changing search range or disable auto.")
        return None

    print(f"[INFO] Auto mode is OFF. Trying fixed_index={cfg.fixed_index}")
    cap = cv2.VideoCapture(cfg.fixed_index)
    if cap.isOpened():
        cap.release()
        return cfg.fixed_index

    cap.release()
    print(f"[ERROR] Fixed camera index {cfg.fixed_index} is not available.")
    return None


def run_camera_loop(camera_index: int, cfg: CameraConfig) -> None:
    cap = open_camera(camera_index, cfg.frame_width, cfg.frame_height)
    if cap is None:
        return

    capture_ch = _normalize_key_char(cfg.key_capture, " ")
    quit_ch = _normalize_key_char(cfg.key_quit, "q")

    print("[INFO] Camera loop started.")
    print(f"       Capture key: '{capture_ch}' (config: {cfg.key_capture})")
    print(f"       Quit key   : '{quit_ch}' (config: {cfg.key_quit})")
    print(
        f"       Save dir   : {cfg.save_root_dir}/{cfg.save_subdir} "
        "(relative to camera folder)"
    )
    print("       Press the quit key to exit.")

    window_name = f"Camera Preview (index {camera_index})"

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Failed to read frame.")
            break

        info_text = (
            f"Idx {camera_index} | "
            f"Cap: '{cfg.key_capture}' Quit: '{cfg.key_quit}'"
        )
        cv2.putText(
            frame,
            info_text,
            (10, 30),
            0.6,
            (0, 255, 0),
            2,
            cv2.LINE_AA,
        )

        cv2.imshow(window_name, frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(quit_ch):
            print("[INFO] Quit key pressed. Exiting loop.")
            break
        if key == ord(capture_ch):
            capture_frame(frame, cfg)

    cap.release()
    cv2.destroyAllWindows()
    print("[INFO] Camera loop finished.")


def print_config_summary(cfg: CameraConfig) -> None:
    """콘솔에 사람이 보기 좋은 설정 요약 출력."""
    mode = "AUTO" if cfg.auto else "FIXED"
    print("\n[CONFIG] Camera settings")
    print(f"  - mode          : {mode}")
    if cfg.auto:
        print(f"  - search range  : {cfg.search_min_index} ~ {cfg.search_max_index}")
    else:
        print(f"  - fixed index   : {cfg.fixed_index}")
    print(f"  - frame size    : {cfg.frame_width} x {cfg.frame_height}")
    print(f"  - key (capture) : {cfg.key_capture}")
    print(f"  - key (quit)    : {cfg.key_quit}")
    print(f"  - save root     : {cfg.save_root_dir}")
    print(f"  - save subdir   : {cfg.save_subdir}\n")


def main() -> None:
    cfg = load_camera_config()
    print_config_summary(cfg)

    idx = resolve_camera_index(cfg)
    if idx is None:
        print("[FATAL] Could not resolve a valid camera index.")
        return

    print(f"[CONFIG] Selected camera index: {idx}\n")
    run_camera_loop(idx, cfg)


if __name__ == "__main__":
    main()