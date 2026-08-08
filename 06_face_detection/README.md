# Face Detection

## Purpose

OpenCV의 Haar Cascade Classifier를 이용하여
실시간 카메라 영상에서 얼굴을 검출하는 방법을 실습했습니다.

## Environment

- Raspberry Pi 4
- Raspberry Pi Camera
- Python
- OpenCV
- Picamera2

## Practice

- Haar Cascade Classifier
- Grayscale 변환
- Face Detection
- Bounding Box
- 실시간 얼굴 검출

## Description

Raspberry Pi Camera에서 입력받은 실시간 영상을
Grayscale 이미지로 변환한 후 Haar Cascade Classifier를 이용하여
얼굴 영역을 검출했습니다.

검출된 얼굴의 위치를 Bounding Box로 표시하여
실시간으로 얼굴의 위치를 확인할 수 있도록 구현했습니다.

## Result

카메라 영상에서 얼굴을 검출하고
검출된 얼굴 영역에 사각형을 표시하는 것을 확인했습니다.
