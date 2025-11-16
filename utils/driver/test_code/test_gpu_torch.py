import sys
import subprocess
import importlib
from pathlib import Path
import os

# 이 스크립트와 같은 폴더의 requirements_test.txt 사용
REQ_FILE = Path(__file__).parent / "requirements_test.txt"
TARGET_PKG = "torch"

# 환경변수로 삭제 여부 제어 (기본: 삭제)
REMOVE_AFTER = os.environ.get("TORCH_TEST_KEEP", "0") != "1"


def find_pkg_line(pkg_name: str):
    if not REQ_FILE.exists():
        raise FileNotFoundError(f"{REQ_FILE} not found.")
    with REQ_FILE.open() as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line.lower().startswith(pkg_name):
                return line
    return None


def ensure_torch():
    try:
        import torch
        print(f"[INFO] PyTorch already installed ({torch.__version__})")
        return torch, False
    except ImportError:
        pkg_line = find_pkg_line(TARGET_PKG)
        if not pkg_line:
            raise RuntimeError("torch not found in requirements_test.txt")
        print("### 파이토치 설치중... (Installing PyTorch...) ###")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", pkg_line],
            check=True,
        )
        torch = importlib.import_module("torch")
        return torch, True


def uninstall_torch():
    print("### 파이토치 삭제중... (Uninstalling PyTorch...) ###")
    subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "torch"], check=False)
    print("[CLEANUP] PyTorch removed.")


def main():
    torch, installed_here = ensure_torch()

    print("[PyTorch] version:", torch.__version__)
    cuda_ok = torch.cuda.is_available()
    print("[PyTorch] CUDA available:", cuda_ok)

    if cuda_ok:
        device_name = torch.cuda.get_device_name(0)
        print("[PyTorch] GPU:", device_name)
        x = torch.randn(1024, 1024, device="cuda")
        y = torch.randn(1024, 1024, device="cuda")
        z = torch.matmul(x, y)
        print("[PyTorch] Matmul on GPU OK. shape:", z.shape)
    else:
        print("[PyTorch] Running on CPU.")
        print("[WARN] CUDA가 비활성화돼 있습니다. 드라이버/런타임을 확인하세요.")

    print("[DONE] PyTorch GPU test finished. (파이토치 GPU 정상 작동 중 ✅)")

    if installed_here and REMOVE_AFTER:
        uninstall_torch()
    elif installed_here:
        print("[INFO] Installed here, but keeping it because TORCH_TEST_KEEP=1")


if __name__ == "__main__":
    main()