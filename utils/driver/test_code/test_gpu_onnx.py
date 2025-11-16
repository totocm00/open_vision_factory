import sys, subprocess, importlib

REQ_FILE = "requirements_test.txt"
TARGET_PKG = "onnxruntime-gpu"
IMPORT_NAME = "onnxruntime"

def find_pkg_line(pkg_name: str):
    with open(REQ_FILE) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.lower().startswith(pkg_name):
                return line
    return None

def ensure_onnxruntime():
    try:
        import onnxruntime as ort
        print(f"[INFO] ONNX Runtime already installed ({ort.__version__})")
        return ort, False
    except ImportError:
        pkg_line = find_pkg_line(TARGET_PKG)
        if not pkg_line:
            raise RuntimeError("onnxruntime-gpu not found in requirements_test.txt")
        print("### 오닉스 런타임 설치중... (Installing ONNX Runtime...) ###")
        subprocess.run([sys.executable, "-m", "pip", "install", pkg_line], check=True)
        ort = importlib.import_module(IMPORT_NAME)
        return ort, True

def uninstall_onnxruntime():
    print("### 오닉스 런타임 삭제중... (Uninstalling ONNX Runtime...) ###")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "onnxruntime-gpu"], check=False)
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "onnxruntime"], check=False)
    print("[CLEANUP] ONNX Runtime removed.")

def main():
    ort, installed_here = ensure_onnxruntime()

    providers = ort.get_available_providers()
    print("[ONNX Runtime] providers:", providers)

    if "CUDAExecutionProvider" in providers:
        print("[ONNX Runtime] ✅ CUDAExecutionProvider available.")
    else:
        print("[ONNX Runtime] ⚠️ CUDAExecutionProvider not found. Using CPU provider.")

    print("[DONE] ONNX Runtime test finished. (오닉스 런타임 GPU 정상 작동 중 ✅)")

    if installed_here:
        uninstall_onnxruntime()

if __name__ == "__main__":
    main()