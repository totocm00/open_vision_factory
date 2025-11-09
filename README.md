<br>

# 🏭 Open Vision Factory

<br>

**Open Vision Factory**는 라벨 검사, 방향 정렬, PCB 좌표 인식 등  
비전 기반 자동화 프로젝트를 실험하고 확장할 수 있는 **AI 비전 공장**입니다.  
각 모듈은 독립 실행이 가능하며, 통합 시 완전한 생산 라인 시뮬레이션을 구성합니다.


<br>
<br>

## # Structure

```bash
open_vision_factory/
 ├── label_detect/               # 라벨 및 문자 인식 모듈 (YOLO + OCR)
 ├── assembly_orient/            # 조립체 방향 판별 모듈 (Classifier)
 ├── pcb_locator/                # PCB 좌표 검출 모듈
 ├── ...
 │
 ├── common/                     # 공통 설정, 유틸, 드라이버/환경 스크립트
 ├── assets/                     # 샘플 이미지, 모델 가중치, 테스트 리소스
 │
 ├── requirements_dev.txt      # 모델 학습/개발용 패키지 목록
 ├── requirements_run.txt            # 기본 실행/공통 의존성
 │
 ├── LICENSE
 └── README.md
```


<br>



## ⚡ Speed Tip (권장 설치 순서)

새 PC나 서버에서 바로 실행하려면 **항상!!! 가상환경(virtualenv)을 먼저 만들고**  
그 안에서 `pip install -r ...` 명령을 실행하세요.  
이렇게 하면 시스템 파이썬과 충돌하지 않아 더 안전하고 깔끔하게 설치됩니다 🚀

```bash
# 1️⃣ 파이썬 버전 확인
python --version          # 또는 python3 --version


# 2️⃣ 프로젝트 폴더로 이동
cd open_vision_factory


# 3️⃣ 가상환경 만들기 
# (Windows)
python -m venv .venv
.\.venv\Scripts\activate

# (Ubuntu / macOS)
python3 -m venv .venv
source .venv/bin/activate


# 4️⃣ pip 업그레이드 및 의존성 설치
pip install --upgrade pip


# 개발/학습용 환경
pip install -r requirements_dev.txt


# 실행/런타임 환경
pip install -r requirements_run.txt


# 가상환경이 활성화되면 프롬프트에 (venv) 표시가 보입니다.
# 작업이 끝나면 다음 명령으로 종료할 수 있습니다.
deactivate
```


<br>

## # Environment Setup

모델링(Modeling) 작업과 테스트(Testing) 작업을 구분해  
필요한 환경만 빠르게 설치할 수 있습니다.

| 목적 | 필요한 파일 | 설치 명령 | |
|------|-------------|------------|------|
| **모델링(Modeling)** | `requirements_model.txt` | `pip install -r requirements_model.txt` | 
| **테스트(Testing)** | `requirements_test.txt` | `pip install -r requirements_test.txt` | 

**모델링(Modeling)** : 데이터 전처리, 학습, 모델 생성 등 모델 개발용 환경  
**테스트(Testing)**  : 학습된 모델을 불러 테스트·시각화·평가하는 환경

<br>
<br>

## # Factory Tools 
> “공장은 자체적으로 드라이버 설치 및 테스트 도구를 제공합니다."

>"Open Vision Factory includes integrated utilities <br>
for automatic driver installation and GPU runtime testing."

**Open Vision Factory**는 개발 환경을 쉽게 준비하고 검증할 수 있도록  
**GPU 드라이버 설치(Driver Install)**, **AI 런타임 테스트(Driver Test)**,  
👇 그리고 **필수 패키지 목록(Requirements)** 파일들을 함께 제공합니다. 👇

<br>

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


<br>
<br>


## # Driver Install Quick Guide (드라이버 자동 감지 및 설치 가이드)

### STEP 0. 공장 저장소 클론 (Clone the factory repository)
터미널에서 다음 명령어를 실행하세요 👇
```bash
git clone https://github.com/totocm00/open_vision_factory.git
cd open_vision_factory
```

<br>

### STEP 1. GPU 및 OS 자동 감지 (Detect GPU and OS)
GPU 종류와 현재 운영체제를 자동으로 감지합니다.
```bash
python common/driver_install/detect_gpu.py #or python3
```

<br>

### STEP 2. 운영체제에 맞는 설치 스크립트 실행 (Run OS-specific installer)
#### 🐧 Ubuntu:
```bash
bash common/driver_install/ubuntu/install_nvidia_driver.sh
```

#### 🪟 Windows (PowerShell 관리자 권한 실행):
```powershell
powershell -ExecutionPolicy Bypass -File common/driver_install/windows/install_nvidia_driver.ps1
```

<br>

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



<br>


### ⚙️ 참고 (Notes)
- **터미널은 관리자 권한(Windows)** 또는 **sudo 권한(Ubuntu)** 으로 실행하세요.  
- 설치 후 **재부팅(sudo reboot)** 이 필요할 수 있습니다.  
- GPU가 정상적으로 인식되지 않으면, 드라이버 버전을 다시 확인하고 재설치하세요.


이 구조를 통해 새 환경에서도  
한 번의 설치로 **GPU 드라이버 → 필수 라이브러리 → AI 테스트**까지 완료할 수 있습니다 🚀  


<br>
<br>
<br>



## # Tech Stack

- **YOLOv8 / YOLOv9** : 객체 검출 및 좌표 인식  
- **PyTorch / Ultralytics** : 딥러닝 모델 프레임워크  
- **OpenCV / EasyOCR** : 영상 처리 및 문자 인식  
- **Streamlit** : 웹 UI 기반 시각화 및 테스트 인터페이스  
- **NumPy / Pandas / Matplotlib** : 데이터 분석 및 시각화


## # Versioning Policy (SemVer)

- 각 단계별 프로젝트 **Semantic Versioning** <br>

  - 예:  
    - `label_test` → v0.1.0  
    - `align_test` → v0.2.0  
    - `pcb_test` → v0.3.0    
<br>
  - 세 프로젝트를 통합한 버전은 **v0.4.0** 또는 **v1.0.0** 으로 관리합니다.

<br>

## 📜 License

MIT License  
© 2025 Open Vision Factory