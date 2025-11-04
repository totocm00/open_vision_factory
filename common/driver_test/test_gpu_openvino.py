import sys, subprocess, importlib

REQ_FILE = "requirements_test.txt"
TARGET_PKG = "openvino"

def find_pkg_line(pkg_name: str):
    with open(REQ_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.lower().startswith(pkg_name):
                return line
    return None

def ensure_openvino():
    try:
        import openvino as ov
        print(f"[INFO] OpenVINO already installed ({ov.__version__})")
        return ov, False
    except ImportError:
        pkg_line = find_pkg_line(TARGET_PKG)
        if not pkg_line:
            raise RuntimeError("openvino not found in requirements_test.txt")
        print("### 오픈비노 설치중... (Installing OpenVINO...) ###")
        subprocess.run([sys.executable, "-m", "pip", "install", pkg_line], check=True)
        ov = importlib.import_module("openvino")
        return ov, True

def uninstall_openvino():
    print("### 오픈비노 삭제중... (Uninstalling OpenVINO...) ###")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "openvino"], check=False)
    print("[CLEANUP] OpenVINO removed.")

def main():
    ov, installed_here = ensure_openvino()

    core = ov.Core()
    devices = core.available_devices
    print("[OpenVINO] Available devices:", devices)

    if any("GPU" in d for d in devices):
        print("[OpenVINO] ✅ GPU device is available.")
    else:
        print("[OpenVINO] ⚠️ GPU device not found. (CPU may still work)")

    print("[DONE] OpenVINO test finished. (오픈비노 런타임 정상 작동 중 ✅)")

    if installed_here:
        uninstall_openvino()

if __name__ == "__main__":
    main()