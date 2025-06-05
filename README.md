# Image Comparison AI Server

이 서버는 이미지 비교를 위한 AI 기능을 제공하는 Flask 기반의 웹 서버입니다.

## 주요 기능

### 1. 이미지 비교 API (`/compare_images`)
두 이미지의 유사도를 계산하여 0-100 사이의 점수로 반환합니다.

**엔드포인트:** `/compare_images`  
**메소드:** POST  
**요청 형식:**
```json
{
    "url1": "첫 번째 이미지 URL",
    "url2": "두 번째 이미지 URL"
}
```
**응답 형식:**
```json
{
    "score": 85.5  // 0-100 사이의 유사도 점수
}
```

## 주요 함수 설명

### 1. `fetch_image(url)`
- **역할:** URL에서 이미지를 다운로드하고 OpenCV 형식으로 변환
- **입력:** 이미지 URL
- **반환:** (이미지 데이터, 에러 메시지)
- **주요 기능:**
  - HTTP 요청을 통한 이미지 다운로드
  - 이미지 형식 검증
  - OpenCV 형식으로 이미지 디코딩

### 2. `normalize_image_size(image1, image2)`
- **역할:** 두 이미지의 크기를 동일하게 조정
- **입력:** 두 개의 이미지
- **반환:** 크기가 조정된 두 이미지
- **주요 기능:**
  - 두 이미지 중 더 작은 크기에 맞춰 리사이징
  - INTER_AREA 보간법을 사용한 고품질 리사이징

### 3. `compute_image_similarity(image1, image2)`
- **역할:** 두 이미지 간의 유사도 계산
- **입력:** 두 개의 이미지
- **반환:** 유사도 점수 (0-1 사이)
- **주요 기능:**
  - HSV 색공간으로 이미지 변환
  - 히스토그램 계산 및 정규화
  - Bhattacharyya 거리를 사용한 유사도 측정

## 기술 스택
- Python 3.x
- Flask (웹 프레임워크)
- OpenCV (이미지 처리)
- NumPy (수치 계산)
- Requests (HTTP 클라이언트)

## 설치 및 실행

1. 필요한 패키지 설치:
```bash
pip install flask opencv-python numpy requests
```

2. 서버 실행:
```bash
python app.py
```

## 에러 처리
- 잘못된 URL 형식
- 이미지 다운로드 실패
- 이미지 디코딩 오류
- 잘못된 요청 형식

## 주의사항
- 이미지 URL은 공개적으로 접근 가능해야 합니다
- 이미지 형식은 일반적인 웹 이미지 형식(jpg, png 등)을 지원합니다
- 서버는 기본적으로 로컬호스트:5000에서 실행됩니다 