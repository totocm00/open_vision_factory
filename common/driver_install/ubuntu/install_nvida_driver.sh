set -e

echo "### STEP 1: GPU 확인 중... (Detecting GPU...) ###"
# lspci 결과가 없더라도 스크립트가 죽지 않도록 || true 추가
lspci | egrep 'VGA|3D' || true

echo "### STEP 2: ubuntu-drivers 도구 확인 중... (Checking ubuntu-drivers tool...) ###"
if ! command -v ubuntu-drivers >/dev/null 2>&1; then
    echo "ubuntu-drivers 명령이 없습니다. 설치 중... (Installing ubuntu-drivers-common...)"
    sudo apt update && sudo apt install -y ubuntu-drivers-common
fi

echo "### STEP 3: 사용 가능한 드라이버 목록 조회 (Listing available NVIDIA drivers...) ###"
if command -v ubuntu-drivers >/dev/null 2>&1; then
    ubuntu-drivers devices || true
else
    echo "ubuntu-drivers를 사용할 수 없습니다. (ubuntu-drivers not available.)"
fi

echo "### STEP 4: 권장 드라이버 자동 설치 (Automatic recommended driver install) ###"
read -p "설치를 진행할까요? (y/N): " yn

# shellcheck disable=SC1010,SC1011
case "$yn" in
    [yY]* )
        echo "설치 중입니다... (Installing...)"
        sudo ubuntu-drivers autoinstall
        echo "[DONE] 설치 완료! 재부팅 후 적용됩니다. (Installation finished! Please reboot.)"
        echo "재부팅 명령: sudo reboot"
        ;;
    * )
        echo "설치를 취소했습니다. (Installation cancelled.)"
        ;;
esac