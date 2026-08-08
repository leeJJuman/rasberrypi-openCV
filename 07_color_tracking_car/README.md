# Color Tracking Car

## Purpose

Raspberry Pi AI Car Kit과 Raspberry Pi Camera를 이용하여
특정 색상을 추적하고 해당 색상의 위치에 따라
자동차가 이동하도록 구현했습니다.

## Environment

- Raspberry Pi 4
- Raspberry Pi AI Car Kit
- Raspberry Pi Camera
- Python
- OpenCV
- Picamera2
- RPi.GPIO
- NumPy

## Practice

- HSV Color Detection
- Color Masking
- Trackbar를 이용한 HSV 범위 조절
- Contour Detection
- Largest Contour Selection
- Bounding Rectangle
- Centroid Calculation
- Position Decision
- PWM
- Raspberry Pi GPIO
- Motor Control

## Description

Raspberry Pi Camera를 통해 실시간 영상을 입력받고
HSV 색 공간으로 변환하여 추적할 색상의 영역을 검출했습니다.

검출된 색상 영역에 Mask를 적용하고
Contour를 분석하여 일정 크기 이상의 영역 중
가장 큰 영역을 추적 대상으로 선택했습니다.

선택된 영역의 Bounding Rectangle을 구하고
중심 좌표를 계산하여 화면에서 목표 색상의 위치를 판단했습니다.

목표 색상의 중심 좌표를 기준으로
자동차의 좌회전, 우회전, 직진을 결정하도록 구현했습니다.

목표 색상 영역이 일정 크기 이상으로 검출되면
자동차를 정지하도록 설정했습니다.

목표 색상이 검출되지 않는 경우에도
자동차가 정지하도록 구현했습니다.

## Tracking Process

- Camera
- HSV Conversion
- Color Mask
- Contour Detection
- Largest Contour Selection
- Centroid Calculation
- Position Decision
- Motor Control

## Position Decision

- 중심 좌표가 240보다 작으면 좌회전
- 중심 좌표가 400보다 크면 우회전
- 중심 좌표가 240 이상 400 이하이면 직진 또는 정지
- 색상 영역이 일정 크기 이상이면 정지
- 목표 색상이 검출되지 않으면 정지

## Motor Control

Raspberry Pi GPIO를 이용하여 자동차의 모터를 제어했습니다.

PWM을 이용하여 좌우 모터의 속도를 조절하고
목표 색상의 위치에 따라 좌우 모터의 속도를 다르게 설정하여
자동차의 방향을 제어했습니다.

## Result

카메라에서 특정 색상을 검출하고
검출된 색상의 위치에 따라 Raspberry Pi AI Car가
좌회전, 우회전, 직진 및 정지하는 것을 확인했습니다.
