import platform
import subprocess
import shutil

print("### STEP 1: OS 및 GPU 확인 중... (Detecting OS and GPU...) ###")

# Detect OS
system = platform.system()
print(f"현재 운영체제 (Detected OS): {system}")

# Detect GPU
try:
    if system == "Windows":
        result = subprocess.run(
            ["wmic", "path", "win32_VideoController", "get", "name"],
            capture_output=True, text=True, check=True
        )
    else:
        result = subprocess.run(
            ["lspci"], capture_output=True, text=True, check=True
        )
    print("GPU 정보 (GPU Info):")
    print(result.stdout)
except Exception as e:
    print("GPU 정보를 불러올 수 없습니다. (Failed to detect GPU.)", e)

print("\n### STEP 2: 권장 드라이버 설치 스크립트 안내 (Driver Install Guide) ###")

if system == "Windows":
    print("👉 Windows 환경입니다. (Detected Windows)")
    print("실행: powershell -ExecutionPolicy Bypass -File common/driver_install/windows/install_nvidia_driver.ps1")
else:
    print("🐧 Ubuntu/Linux 환경입니다. (Detected Ubuntu/Linux)")
    print("실행: bash common/driver_install/ubuntu/install_nvidia_driver.sh")

print("\n[DONE] GPU 감지 및 설치 안내 완료! (Detection finished.)")
