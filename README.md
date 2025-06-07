# Fullstack Backend AI Server

## 프로젝트 소개 - Snap Campus
이 프로젝트는 Snap Campus의 핵심 기능인 이미지 유사도 분석을 위한 AI 서버입니다. 사용자가 촬영한 랜드마크 사진과 실제 랜드마크 이미지를 비교하여 유사도를 계산하고, 이를 통해 퀘스트 완료 여부를 판단하는 중요한 역할을 수행합니다. OpenCV와 HSV 색공간 기반의 히스토그램 분석을 통해 정확한 이미지 유사도를 제공합니다.

## 기술 스택
- **Backend Framework**: Flask
- **Image Processing**: OpenCV (cv2)
- **Numerical Computing**: NumPy
- **HTTP Client**: Requests
- **Language**: Python 3.x

## 프로젝트 구조
image-comparison-server/
├── app.py # 메인 애플리케이션 파일
│ ├── fetch_image() # 이미지 다운로드 및 변환
│ ├── normalize_image_size() # 이미지 크기 정규화
│ ├── compute_image_similarity() # 이미지 유사도 계산
│ └── compare_images() # API 엔드포인트
└── README.md # 프로젝트 문서

## 핵심 기능

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

### 2. 이미지 처리 기능
- **이미지 다운로드**: URL에서 이미지 다운로드 및 OpenCV 형식 변환
- **크기 정규화**: 두 이미지의 크기를 동일하게 조정
- **유사도 계산**: HSV 색공간 기반 히스토그램 비교

## 실행 방법

### 사전 요구사항
- Python 3.x
- pip (Python 패키지 관리자)

### 설치 및 실행
1. 필요한 패키지 설치:
```bash
pip install flask opencv-python numpy requests
```

2. 서버 실행:
```bash
python app.py
```

3. 서버는 기본적으로 `http://localhost:5000`에서 실행됩니다.

### EC2 배포 방법
1. EC2 인스턴스 접속:
```bash
ssh -i your-key.pem ec2-user@your-ec2-public-ip
```

2. 필요한 패키지 설치:
```bash
sudo dnf update -y
sudo dnf install python3 python3-pip -y
```

3. 프로젝트 파일 전송:
```bash
scp -i your-key.pem -r ./ ec2-user@your-ec2-public-ip:~/image-comparison-server/
```

4. 서버 실행:
```bash
nohup python3 app.py > server.log 2>&1 &
```

## 주의사항
- 이미지 URL은 공개적으로 접근 가능해야 합니다
- 이미지 형식은 일반적인 웹 이미지 형식(jpg, png 등)을 지원합니다
- 서버는 기본적으로 로컬호스트:5000에서 실행됩니다

## 에러 처리
- 잘못된 URL 형식
- 이미지 다운로드 실패
- 이미지 디코딩 오류
- 잘못된 요청 형식
