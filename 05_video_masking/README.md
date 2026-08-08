# Video Masking

## Purpose

HSV 색 공간을 이용하여 실시간 영상에서
특정 색상 영역을 검출하고 마스킹하는 방법을 실습했습니다.

## Environment

- Raspberry Pi 4
- Raspberry Pi Camera
- Python
- OpenCV
- Picamera2
- NumPy

## Practice

- BGR에서 HSV로 변환
- HSV 색상 범위 설정
- Color Mask 생성
- 여러 Mask 결합
- Bitwise Operation
- 실시간 영상 마스킹

## Description

카메라에서 입력받은 영상을 HSV 색 공간으로 변환한 후
특정 색상에 해당하는 영역을 검출했습니다.

노란색, 빨간색, 파란색에 대한 HSV 범위를 설정하고
각 색상에 대한 Mask를 생성했습니다.

생성된 Mask를 결합한 후 Bitwise Operation을 이용하여
검출된 색상 영역만 원본 영상에 표시했습니다.

## Demo

HSV 색 공간을 이용하여 특정 색상 영역을 검출하고 마스킹하는 과정을 확인할 수 있습니다.

[동작 영상](https://www.youtube.com/shorts/8uY9u5GmhPM)

## Result

실시간 카메라 영상에서 설정한 색상 영역만
추출하여 출력하는 것을 확인했습니다.
