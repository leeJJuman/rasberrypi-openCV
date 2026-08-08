import cv2
import numpy as np
import RPi.GPIO as GPIO
from picamera2 import Picamera2
import time

PWMA = 18
AIN1 = 22
AIN2 = 27

PWMB = 23
BIN1 = 25
BIN2 = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PWMA, GPIO.OUT)
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)

GPIO.setup(PWMB, GPIO.OUT)
GPIO.setup(BIN1, GPIO.OUT)
GPIO.setup(BIN2, GPIO.OUT)

L_Motor = GPIO.PWM(PWMA, 500)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB, 500)
R_Motor.start(0)

def nothing(x):
    pass

def forward(speed=50):
    print("go straight")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(speed)

def left(speed=50):
    print("turn left")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(20)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(speed)

def right(speed=50):
    print("turn right")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(speed)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(20)

def stop(speed=0):
    print("stop")
    GPIO.output(AIN1, 0)
    GPIO.output(AIN2, 1)
    L_Motor.ChangeDutyCycle(0)
    GPIO.output(BIN1, 0)
    GPIO.output(BIN2, 1)
    R_Motor.ChangeDutyCycle(0)

def main():
    height = 480
    width = 640
    cam = Picamera2()
    cam.configure(cam.create_video_configuration(main={'format': 'XRGB8888', 'size': (width, height)}))
    cam.start()

    cv2.namedWindow('Trackbars')
    cv2.createTrackbar("L - H", "Trackbars", 90, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 100, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 100, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 130, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

    try:
        while True:
            frame = cam.capture_array()
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            l_h = cv2.getTrackbarPos("L - H", "Trackbars")
            l_s = cv2.getTrackbarPos("L - S", "Trackbars")
            l_v = cv2.getTrackbarPos("L - V", "Trackbars")
            u_h = cv2.getTrackbarPos("U - H", "Trackbars")
            u_s = cv2.getTrackbarPos("U - S", "Trackbars")
            u_v = cv2.getTrackbarPos("U - V", "Trackbars")

            lower_blue = np.array([l_h, l_s, l_v])
            upper_blue = np.array([u_h, u_s, u_v])

            mask = cv2.inRange(hsv, lower_blue, upper_blue)

            contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            max_area = 0
            max_contour = None

            for c in contours:
                area = cv2.contourArea(c)
                if area > 2000 and area > max_area:
                    max_area = area
                    max_contour = c

            if max_contour is not None:
                x, y, w, h = cv2.boundingRect(max_contour)
                centroid_x = int(x + w / 2)
                centroid_y = int(y + h / 2)

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.circle(frame, (centroid_x, centroid_y), 10, (0, 0, 255), -1)

                if centroid_x < 240:
                    left(50)
                elif centroid_x > 400:
                    right(50)
                else:
                    pixels = cv2.countNonZero(mask)
                    if pixels > 50000:
                        stop()
                   
                    else:
                        forward(50)
            else:
                print("cannot detect target")
                stop()

            cv2.imshow('frame', frame)
            cv2.imshow('mask', mask)

            key = cv2.waitKey(1) & 0xFF
            if key == 27 or key == ord('q'):
                break

    finally:
        stop()
        GPIO.cleanup()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()

