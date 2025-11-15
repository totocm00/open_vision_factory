## =================================
# Module Folder Usage Guide
## (assets/modules/ 내부 모듈 폴더 사용 방법)

<br>

This document briefly explains how to use folders inside:  
`assets/modules/`

이 문서는 `assets/modules/` 폴더 안의 모듈 구조를  
어떻게 사용하면 되는지 간단히 안내합니다.

---
```
1. Summary (간단 요약)
2. Folder Usage
   2-1) modules/ (root)
   2-2) converted_files/
   2-3) images/
3. How to Use (사용 예)
4. Notes (참고)
```
---

<br><br>


## =================================
# 1. Summary (간단 요약)

Inside `assets/modules/`, Vision modules are organized into three categories:

`assets/modules/` 내부의 Vision 모듈은 다음 3가지 영역으로 구성됩니다:

```
modules/
 ├─ public/            # modules that can be shared publicly
 ├─ private/           # experimental or internal-only modules
 └─ task_method_model  # template for creating new modules

 ├─ public/            # 공개 가능한 모듈
 ├─ private/           # 비공개·실험용 모듈
 └─ task_method_model  # 템플릿 구조
```

Each Vision module folder follows this structure:  
각 Vision 모듈은 다음 구조를 따릅니다:

```
<task>_<method>_<model>/
 ├─ converted_files/   # non-image outputs such as JSON, TXT, XML
 └─ images/            # original / processed / visualized images

 ├─ converted_files/   # JSON, TXT, XML 등 비이미지 출력 폴더
 └─ images/            # 원본 / 가공 / 시각화 이미지 저장 폴더
```

Example module names / 모듈 이름 예시:

```
module_ltr_ocr_paddle/
module_detection_yolo_v8/
module_pose_landmark_mediapipe/
```

<br>
<br>

## =================================
# 2. Folder Usage
## (폴더 별 사용 방법 안내)

<br>

## 2-1) modules/ (root)
각 영역의 역할은 다음과 같습니다:

- **public/**  
  modules that can be shared publicly  
  공개 가능한 실제 사용 모듈을 저장합니다.

- **private/**  
  internal or experimental modules  
  비공개 실험용 / 테스트용 모듈을 저장합니다.  
  기본적으로 `.gitkeep`만 둔 빈 구조입니다.

- **task_method_model/**  
  template used when creating a new module  
  새로운 모듈 생성 시 복사하여 쓰는 **샘플 템플릿 구조**입니다.  
  내부 폴더 구조는 실제 모듈과 동일합니다.

<br>

---

## 2-2) converted_files/
Stores non-image outputs such as JSON, TXT, XML.  
JSON, TXT, XML 등 **비이미지 결과물**을 저장합니다.

```
converted_files/
 ├─ json/   # prediction outputs
 ├─ txt/    # extracted text
 ├─ xml/    # annotation files
 └─ yaml/   # optional configuration

 ├─ json/   # 모델 예측 JSON
 ├─ txt/    # 텍스트 결과
 ├─ xml/    # XML 어노테이션
 └─ yaml/   # (선택) 설정·라벨 정보
```

<br>

## 2-3) images/
Stores all image-based files created during processing.  
모듈 처리 과정에서 생성되는 모든 **이미지 기반 결과물**을 저장합니다.

```
images/
├─ origin/       # original input images (raw data)
├─ processed/    # images after preprocessing or postprocessing
├─ visualized/   # final images with labels, boxes, overlays
├─ cropped/      # cropped image segments(words,objects,regions)

├─ origin/       # 입력에 사용되는 원본 이미지
├─ processed/    # 전처리 또는 후처리된 이미지
├─ visualized/   # 라벨·박스 등이 반영된 최종 시각화 이미지
└─ cropped/      # 단어·객체·영역 단위로 잘라낸 이미지
```

<br>
<br>

## =================================
# 3. How to Use (사용 예)

1. **Provide input images in** `images/origin/`  
   You may **manually place images** into the `images/origin/` folder,  
   or depending on the module, **original images may be automatically generated**  
   (e.g., camera capture, screenshot, pipeline-generated input).

   입력 이미지는 `images/origin/` 폴더에 직접 넣을 수도 있고,  
   일부 모듈에서는 **카메라 촬영·캡처 등으로 자동 생성될 수도 있습니다.**

2. **Run the module pipeline**  
   모듈의 파이프라인을 실행합니다.

3. **Check results**

   결과는 다음 폴더에 생성됩니다:
---
   - JSON/TXT/XML → `converted_files/`  
   - Visualization images → `images/visualized/`  
   - Cropped images → `images/cropped/`  
   - Original images → `images/origin/` (manual or auto-generated)
---
   - JSON/TXT/XML → `converted_files/`
   - 시각화 이미지 → `images/visualized/`
   - 잘라낸 이미지 → `images/cropped/`
   - 원본 이미지 → `images/origin/`

---

<br>
<br>

## =================================
# 4. Notes (참고)

- All modules follow the same folder structure.  
  모든 모듈은 동일한 폴더 구조를 사용합니다.

- You may extend these folders depending on your project.  
  필요하면 프로젝트에 맞게 자유롭게 확장해도 됩니다.

- `public/`  
  → modules that are ready for actual service or distribution  
    실제 서비스 또는 배포가 가능한 모듈을 보관합니다.

- `private/`  
  → internal modules used for experiments or testing  
    실험·테스트용 내부 모듈을 보관합니다.

- `task_method_model/`  
  → template structure used when creating a new Vision module  
    새로운 Vision 모듈을 만들 때 참고하는 템플릿 구조입니다.  
    폴더를 복사하여 형태의 신규 모듈 또는 확장이 가능합니다.



---

# End of Document
