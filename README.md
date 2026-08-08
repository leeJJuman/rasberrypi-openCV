# Raspberry Pi OpenCV Practice

Raspberry Pi 4와 Raspberry Pi AI Car Kit을 활용하여
Python과 OpenCV를 학습하고 실습한 내용을 정리한 저장소입니다.

기본적인 이미지 처리부터 실시간 영상 처리, 색상 마스킹,
얼굴 검출을 거쳐 색상 추적 자동차 제어까지 단계적으로 실습했습니다.

## Environment

### Hardware

- Raspberry Pi 4
- Raspberry Pi AI Car Kit
- Raspberry Pi Camera

### Software

- Python
- OpenCV
- Picamera2
- RPi.GPIO
- NumPy

## Practice

### 01. Image Processing

OpenCV를 이용한 기본적인 이미지 처리

- Image Read
- Grayscale
- Flip
- Rotate
- Canny Edge Detection
- Gaussian Blur
- Circle Drawing
- Rectangle Drawing

### 02. Camera

Raspberry Pi Camera와 Picamera2를 이용한 실시간 영상 출력

- Camera Capture
- Real-time Video
- Center Point 표시

### 03. Video Processing

실시간 카메라 영상에 OpenCV의 영상 처리 기능 적용

- Canny Edge Detection
- Flip
- Real-time Image Processing

### 04. Capture Image

실시간 카메라 영상에서 원하는 프레임을 이미지로 저장

- Frame Capture
- Keyboard Input
- Image Saving
- PNG 파일 저장
- S 키를 이용한 이미지 캡처

### 05. Video Masking

HSV 색 공간을 이용하여 영상에서 특정 색상을 검출하고 마스킹

- HSV Color Space
- Color Thresholding
- Mask
- Bitwise Operation
- 색상 영역 추출

### 06. Face Detection

Haar Cascade Classifier를 이용한 실시간 얼굴 검출

- Haar Cascade Classifier
- Grayscale
- Face Detection
- Bounding Box
- Real-time Camera Processing

### 07. Color Tracking Car

Raspberry Pi AI Car Kit을 이용하여 특정 색상을 추적하는 자동차 구현

- HSV Color Detection
- Color Masking
- Contour Detection
- Largest Contour Selection
- Centroid Calculation
- Position Decision
- Motor Control
- PWM
- Raspberry Pi GPIO

자동차의 카메라에서 특정 색상을 검출하고
검출된 색상의 위치를 기반으로 좌회전, 우회전, 직진 및 정지를 판단합니다.

## Learning Process

- Image Processing
- Camera
- Video Processing
- Frame Capture
- Video Masking
- Face Detection
- Color Detection
- Contour Analysis
- Motor Control
- Raspberry Pi AI Car

## Demo

각 실습의 동작 영상은 해당 실습 폴더에서 확인할 수 있습니다.

## Future Improvements

- Object Tracking
- Lane Detection
- Object Detection
- 다양한 조명 환경에서의 색상 검출 개선
- 색상 추적 자동차의 주행 안정성 개선
- Raspberry Pi 기반 자율주행 기능 확장
