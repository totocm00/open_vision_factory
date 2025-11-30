### 📦 주요 구성
- `common/driver_install/`  
  └─ OS별 **NVIDIA GPU 드라이버 자동 감지 및 설치 스크립트**
  - `detect_gpu.py` : GPU 모델 및 제조사 자동 감지
  - `ubuntu/install_nvidia_driver.sh` : Ubuntu용 드라이버 자동 설치
  - `windows/install_nvidia_driver.ps1` : Windows용 드라이버 설치 가이드

- `common/driver_test/`  
  └─ **GPU 및 AI 프레임워크 동작 테스트 스크립트**
  - `requirements_test.txt` : 테스트 환경 전용 패키지 목록  
  - `test_gpu_tf.py` : TensorFlow GPU 동작 확인  
  - `test_gpu_torch.py` : PyTorch GPU 동작 확인  
  - `test_gpu_openvino.py` : OpenVINO 런타임 테스트  
  - `test_gpu_onnx.py` : ONNX Runtime 테스트


이 구조를 통해 새 환경에서도  
한 번의 설치로 **GPU 드라이버 → 필수 라이브러리 → AI 테스트**까지 완료할 수 있습니다 🚀


```bash
common/                     # 공통 설정, 유틸, 드라이버/환경 스크립트
├── driver_install/         # OS별 GPU 드라이버 감지/설치 스크립트
│     │
│     └── ubuntu/
│     │     └── install_nvidia_driver.sh
│     │
│     └── windows/
│     │     └── install_nvidia_driver.ps1
│     │
│     └── detect_gpu.py
│ 
└── driver_test/            # GPU / AI 런타임 동작 확인용 스크립트
       │
       ├── requirements_test.txt
       │
       ├── test_gpu_tf.py
       ├── test_gpu_torch.py
       ├── test_gpu_openvino.py
       └── test_gpu_onnx.py
```

## ⚙️ Driver Install Quick Guide (드라이버 자동 감지 및 설치 가이드)

### STEP 0. 공장 저장소 클론 (Clone the factory repository)
터미널에서 다음 명령어를 실행하세요 👇
```bash
git clone https://github.com/totocm00/open_vision_factory.git
cd open_vision_factory
```

---

### STEP 1. GPU 및 OS 자동 감지 (Detect GPU and OS)
GPU 종류와 현재 운영체제를 자동으로 감지합니다.
```bash
python common/driver_install/detect_gpu.py #or python3
```

---

### STEP 2. 운영체제에 맞는 설치 스크립트 실행 (Run OS-specific installer)
#### 🐧 Ubuntu:
```bash
bash common/driver_install/ubuntu/install_nvidia_driver.sh
```

#### 🪟 Windows (PowerShell 관리자 권한 실행):
```powershell
powershell -ExecutionPolicy Bypass -File common/driver_install/windows/install_nvidia_driver.ps1
```

---

### STEP 3. GPU 테스트 (Test your GPU)
설치 후 GPU가 정상 작동하는지 테스트하세요.
```bash
cd common/driver_test
pip install -r requirements_test.txt

python test_gpu_torch.py   # or
python test_gpu_tf.py      # or
python test_gpu_onnx.py    # or
python test_gpu_openvino.py
```

---

### ⚙️ 참고 (Notes)
- **터미널은 관리자 권한(Windows)** 또는 **sudo 권한(Ubuntu)** 으로 실행하세요.  
- 설치 후 **재부팅(sudo reboot)** 이 필요할 수 있습니다.  
- GPU가 정상적으로 인식되지 않으면, 드라이버 버전을 다시 확인하고 재설치하세요.