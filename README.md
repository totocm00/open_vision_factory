
# Open Vision Factory  
모듈형 비전 AI 프레임워크 – OCR / Detection / Camera / Simulation / Export / GPU Tools

<br>

## 🎬 Intro Video  


<video src="assets/modules/private/private_house/video/ovf-main-video.mp4"
       autoplay loop muted playsinline
       width="100%">
</video>

<br>

## 🔊 Audio Guide

<table>
  <tr>
    <th>Language</th>
    <th>Audio</th>
  </tr>
  <tr>
    <td>🇰🇷 Korean</td>
    <td>
      <a href="assets/docs/audio/ovf_ko.mp3">
        <button style="
          background: linear-gradient(90deg, #d4af37, #f7e28b);
          border: none;
          padding: 8px 18px;
          border-radius: 6px;
          color: #000;
          font-weight: 600;
          cursor: pointer;">
          ▶ Play
        </button>
      </a>
    </td>
  </tr>
  <tr>
    <td>🇯🇵 Japanese</td>
    <td>
      <a href="assets/docs/audio/ovf_jp.mp3">
        <button style="
          background: linear-gradient(90deg, #d4af37, #f7e28b);
          border: none;
          padding: 8px 18px;
          border-radius: 6px;
          color: #000;
          font-weight: 600;
          cursor: pointer;">
          ▶ Play
        </button>
      </a>
    </td>
  </tr>
  <tr>
    <td>🇺🇸 English</td>
    <td>
      <a href="assets/docs/audio/ovf_en.mp3">
        <button style="
          background: linear-gradient(90deg, #d4af37, #f7e28b);
          border: none;
          padding: 8px 18px;
          border-radius: 6px;
          color: #000;
          font-weight: 600;
          cursor: pointer;">
          ▶ Play
        </button>
      </a>
    </td>
  </tr>
</table>


<br>
<br>



# 01. Overview  
**Open Vision Factory**(OVF)는   
OCR · Object Detection · Gaze Trigger · Landmark Detection 등을  
**모듈 단위로 조립하여 사용할 수 있는 확장형 비전 AI 프레임워크**입니다.

<br>
<br>

## 📦 1) OVF 모듈 생태계 (Public / Private / Task_Method_Model)

OVF는 Vision 기능을 3가지 유형의 모듈로 제공합니다:


### **① Public Modules**
- 외부 배포용 공개 모듈  
- 예: `label_text_recognition` (LTR)  
- OVF 없이도 단독 실행 가능하며, OVF Core에 결합하면 파이프라인으로 통합됨

### **② Private Modules**
- 개인/팀/기업 내부에서만 사용하는 모듈  
- Public과 동일한 규약으로 제작되며, `modules/`에 삽입하면 자동 로딩됨

### **③ Task_Method_Model Modules**  
- OVF Vision Module을 개발할 때 사용하는 **공식 템플릿·샘플 패키지**  
- 정식 파일구조, Config 포맷, Runner·Method·Model 패턴을 모두 포함  
- 새로운 Vision 모듈을 만들 때 복제/확장 가능한 **표준 형식(Format Guide)**

📌 Public/Private/Template 모듈은 모두 OVF 파이프라인 안에서 자유롭게 조합 가능  
📌 LTR 같은 배포 모듈도 추후 Public에 보관 예정이며,  
사용자는 **OVF + 원하는 모듈 clone** 방식으로 단독/결합 실행 가능

<br>
<br>




## ⚙️ 2) GPU 환경 구축: Driver Install + GPU Tester (One System)

OVF는 비전 모델을 GPU 가속으로 실행하기 위해  
**드라이버 설치 + GPU 동작 테스트**를 하나로 묶은 환경 구성 시스템을 제공합니다.

### ✔ 드라이버 설치 스크립트
- Ubuntu: `install_nvida_driver.sh`  
- Windows: `install_nvidia_driver.ps1`  
→ GPU 자동 탐색, 권장 드라이버 안내, 설치/재부팅 가이드 포함

### ✔ GPU 테스트 스위트
- Torch / TensorFlow / Paddle / ONNX Runtime / OpenVINO  
  모두 GPU 가속이 실제 사용 가능한지 실행 즉시 테스트 가능  
- 파일 위치: `utils/driver/test_code/`

📌 OVF는 “드라이버 설치 → GPU 테스트” 흐름을 표준화해  
Vision 프로젝트 초기 설정을 빠르게 완료할 수 있도록 설계되어 있습니다.

<br>
<br>

## 🎥 3) Camera Engine (Auto Detection & Capture)

OVF의 카메라 엔진은  
**자동 장치 탐색, 해상도 설정, 즉시 캡처 테스트, 실시간 프레임 처리**를 지원합니다.

- 자동 카메라 index 스캔  
- 장치 오류 대비 예외 처리  
- YAML 기반 Config 로딩  
- 미리보기 / 캡처 / 프레임 전달 기능 포함  
- 경로:  
  - `utils/camera/check.py`  
  - `utils/camera/open.py`  
  - `utils/camera/test_capture.py`

📌 Camera → OCR → Detection → Export 모듈을 조립해  
즉시 파이프라인 구축 가능

<br>
<br>

## 📑 4) Requirements 시스템 (run / ocr / dev)

OVF는 환경 충돌을 막고 배포 효율을 높이기 위해  
3단계 requirements 구조를 운영합니다:

### **① run.txt**
운영·배포용 최소 패키지 환경  
(OVF Core + Vision Pipeline)

### **② ocr.txt**
PaddleOCR 기반의 OCR 전용 환경  
(텍스트 인식 기능만 필요할 때)

### **③ dev.txt**
ML/DL 연구·훈련용 확장 환경  
(Torch/TF/Paddle 개발 및 실험 중심)

📌 이 3개의 환경은 서로 독립적으로 구성되어  
프로젝트 요구사항에 따라 필요한 것만 선택적으로 설치할 수 있습니다.

---

> OVF의 Overview는 “모듈 생태계 → GPU환경 → 카메라 엔진 → 요구 환경”이라는  
> 네 개의 축을 중심으로 구성되며,  
> 이를 통해 다양한 Vision AI 기반 프로젝트를 빠르고 안정적으로 제작할 수 있습니다.


<br>
<br>
<br>


---

# ▼ 02. Driver Install (Windows / Ubuntu)
<details>
<summary><strong>요약: Windows/Ubuntu GPU 드라이버 자동 설치 스크립트 제공</strong></summary>

OVF는 GPU 사용을 위한 **자동 드라이버 설치 스크립트**를 제공합니다.

### ✔ 설치 스크립트  
- Ubuntu → `utils/driver/install/ubuntu/install_nvida_driver.sh`  
- Windows → `utils/driver/install/windows/install_nvidia_driver.ps1`

### ✔ 기능  
- GPU 자동 탐색  
- 적합한 드라이버 추천  
- 설치 안내 + 재부팅 안내  

📄 자세한 설명: `docs/0001_driver_install.md`

</details>


<br>
<br>


---

# ▼ 03. GPU Test Suite
<details>
<summary><strong>요약: Torch / TF / Paddle / ONNX / OpenVINO GPU 사용 여부 검증</strong></summary>

다음 엔진의 GPU 가속 가능 여부를 검사할 수 있습니다:

| Framework | GPU Test |
|----------|----------|
| PyTorch | ✔ |
| TensorFlow | ✔ |
| PaddlePaddle | ✔ |
| OpenVINO | ✔ |
| ONNX Runtime | ✔ |

### ✔ 위치  
`utils/driver/test_code/`

### ✔ 포함 파일  
- test_gpu_basic.py  
- test_gpu_torch.py  
- test_gpu_tf.py  
- test_gpu_onnx.py  
- test_gpu_openvino.py  
- requirements_test.txt

📄 문서: `docs/0002_gpu_test.md`

</details>

<br>
<br>

---

# ▼ 04. Vision Modules & Integration
<details>
<summary><strong>요약: 외부 비전 프로젝트를 OVF에 그대로 이식/결합 가능</strong></summary>

OVF는 “모듈 플러그인 방식”으로  
외부 프로젝트를 독립/결합해 사용할 수 있습니다.

---

## ✔ 사용 예시

### 1) OVF 설치
```
git clone open_vision_factory
cd open_vision_factory
```

### 2) Vision Module 설치  
예: LTR
```
git clone https://github.com/.../label_text_recognition
```

### 3) 단독 실행 가능  
LTR처럼 단독 실행 모듈로 활용 가능.

### 4) OVF Core에 결합  
다음 경로에 넣으면 자동 인식:
```
src/open_vision_factory/modules/
```

---

📄 상세 문서: `docs/0006_module_building.md`

</details>


<br>
<br>



---

# ▼ 05. Camera Engine
<details>
<summary><strong>요약: 카메라 자동 탐색 · 해상도 설정 · 캡처 테스트 제공</strong></summary>

### ✔ 주요 기능
- 카메라 자동 인덱스 탐색  
- 연결 실패 대응  
- YAML 기반 설정 로딩  
- 실시간 캡처 테스트  

### ✔ 관련 파일
- `utils/camera/check.py`  
- `utils/camera/open.py`  
- `utils/camera/test_capture.py`  
- `utils/camera/config/camera.yaml`  
- `utils/camera/config/loader.py`

📄 문서: `docs/0003_camera_guide.md`

</details>


<br>
<br>


---

# ▼ 06. Assets (Resource System)
<details>

<summary><strong>요약: 영상/오디오/모듈/이미지/모델/임시파일을 관리하는 중앙 리소스 공간</strong></summary>

OVF의 리소스 저장소입니다.

---

## ✔ 구조

| 폴더 | 설명 |
|------|------|
| **assets/docs** | Intro 영상, 오디오, README 전용 파일 |
| **assets/modules** | public/private/test 모듈 리소스 |
| **assets/modules/public** | LTR 같은 배포 모듈 |
| **assets/modules/private** | 팀·기업 내부 모듈 |
| **assets/modules/task_method_model** | 테스트/연구/메소드/모델 기반 모듈 |
| **assets/images** | 샘플 이미지 |
| **assets/models** | 학습된 모델 가중치 |
| **assets/tmp** | 임시 출력물 |

---

📌 **LTR 같은 배포 모듈은 public 폴더에 참고용 보관 가능**  
📌 하지만 실제 실행은 “OVF clone + 모듈 clone” 방식이 기본 구조

</details>


<br>
<br>


---

# ▼ 07. Demos
<details>
<summary><strong>요약: OVF 기능을 빠르게 실행해보는 예제 모음</strong></summary>

### ✔ 제공 예제
- run_basic_pipeline.py  
- run_camera_check.py  

📄 문서: `docs/0004_demos.md`

</details>


<br>
<br>


---

# ▼ 08. Requirements (환경 구분)
<details>
<summary><strong>요약: run/ocr/dev 3종 환경 분리로 충돌 최소화</strong></summary>

| 파일 | 목적 |
|------|------|
| **run.txt** | 운영/배포 환경 |
| **ocr.txt** | PaddleOCR 환경 |
| **dev.txt** | 연구·모델링용 개발 환경 |

</details>


<br>
<br>


---

# ▼ 09. Project Structure (Full Tree)

<details>
<summary><strong>영문 구조 보기</strong></summary>

```
open_vision_factory/
 ├─ assets/                               # resources (videos, audio, images, modules)
 │   ├─ docs/                              # intro videos, mp3, markdown assets
 │   ├─ modules/                           # public/private/test modules
 │   │   ├─ public/                        # distributable modules
 │   │   ├─ private/                       # internal modules
 │   │   └─ task_method_model/             # experimental modules
 │   ├─ images/                            # sample images
 │   ├─ models/                            # model weights
 │   └─ tmp/                               # temp output files
 │
 ├─ demos/                                 # quick examples
 │   ├─ run_basic_pipeline.py
 │   └─ run_camera_check.py
 │
 ├─ docs/                                  # documentation
 │   ├─ 0001_driver_install.md
 │   ├─ 0002_gpu_test.md
 │   ├─ 0003_camera_guide.md
 │   ├─ 0004_demos.md
 │   ├─ 0005_pipeline_architecture.md
 │   └─ 0006_module_building.md
 │
 ├─ requirements/
 │   ├─ dev.txt
 │   ├─ ocr.txt
 │   └─ run.txt
 │
 ├─ src/
 │   └─ open_vision_factory/
 │       ├─ configs/
 │       ├─ core/
 │       ├─ modules/
 │       └─ utils/
 │
 ├─ utils/
 │   ├─ camera/
 │   └─ driver/
 │
 ├─ LICENSE
 └─ README.md
```

</details>

<details>
<summary><strong>한국어 구조 보기</strong></summary>

```
open_vision_factory/
 ├─ assets/                               # 공용 리소스
 │   ├─ docs/                              # 문서/영상/오디오
 │   ├─ modules/                           # public/private/테스트 모듈
 │   │   ├─ public/                        # 배포 모듈 (LTR 등)
 │   │   ├─ private/                       # 내부용 모듈
 │   │   └─ task_method_model/             # 실험용 모듈
 │   ├─ images/                            # 이미지 샘플
 │   ├─ models/                            # 모델 가중치
 │   └─ tmp/                               # 임시 파일
 │
 ├─ demos/
 │   ├─ run_basic_pipeline.py
 │   └─ run_camera_check.py
 │
 ├─ docs/
 │   ├─ 0001_driver_install.md
 │   ├─ 0002_gpu_test.md
 │   ├─ 0003_camera_guide.md
 │   ├─ 0004_demos.md
 │   ├─ 0005_pipeline_architecture.md
 │   └─ 0006_module_building.md
 │
 ├─ requirements/
 │   ├─ dev.txt
 │   ├─ ocr.txt
 │   └─ run.txt
 │
 ├─ src/
 │   └─ open_vision_factory/
 │       ├─ configs/
 │       ├─ core/
 │       ├─ modules/
 │       └─ utils/
 │
 ├─ utils/
 │   ├─ camera/
 │   └─ driver/
 │
 ├─ LICENSE
 └─ README.md
```

</details>


<br>
<br>


---

# ▼ 10. Documentation Guide
<details>
<summary><strong>요약: 모든 상세 문서는 docs/ 아래 번호별 문서로 분리</strong></summary>

- 0001_driver_install.md — GPU 드라이버 설치  
- 0002_gpu_test.md — GPU 테스트  
- 0003_camera_guide.md — 카메라 엔진  
- 0004_demos.md — 데모 설명  
- 0005_pipeline_architecture.md — 전체 아키텍처  
- 0006_module_building.md — 모듈 개발 가이드  

</details>


<br>
<br>
<br>
<br>

# License  
MIT License