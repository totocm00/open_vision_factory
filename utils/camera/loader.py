import os
from dataclasses import dataclass

import yaml


# 이 파일(loader.py)이 있는 camera 폴더 기준 경로
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CONFIG_PATH = os.path.join(BASE_DIR, "config", "camera_config.yaml")


@dataclass
class CameraConfig:
    auto: bool = True
    fixed_index: int = 0
    search_min_index: int = 0
    search_max_index: int = 10
    frame_width: int = 1280
    frame_height: int = 720
    key_capture: str = "space"
    key_quit: str = "q"
    save_root_dir: str = "images"
    save_subdir: str = "default"


def load_camera_config(config_path: str | None = None) -> CameraConfig:
    """
    camera_config.yaml을 읽어서 CameraConfig 인스턴스로 반환.
    config_path를 넘기지 않으면 camera/config/camera_config.yaml 사용.
    """
    path = config_path or DEFAULT_CONFIG_PATH

    if not os.path.exists(path):
        print(f"[INFO] camera_config.yaml not found at {path}, using defaults.")
        return CameraConfig()

    with open(path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    cam = raw.get("camera", {}) or {}
    keys_cfg = cam.get("keys", {}) or {}
    save_cfg = cam.get("save", {}) or {}

    cfg = CameraConfig(
        auto=bool(cam.get("auto", True)),
        fixed_index=int(cam.get("fixed_index", 0)),
        search_min_index=int(cam.get("search_min_index", 0)),
        search_max_index=int(cam.get("search_max_index", 10)),
        frame_width=int(cam.get("frame_width", 1280)),
        frame_height=int(cam.get("frame_height", 720)),
        key_capture=str(keys_cfg.get("capture", "space")),
        key_quit=str(keys_cfg.get("quit", "q")),
        save_root_dir=str(save_cfg.get("root_dir", "images")),
        save_subdir=str(save_cfg.get("subdir", "default")),
    )

    print(f"[INFO] Loaded camera config: {cfg}")
    return cfg