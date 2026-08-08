import cv2
import numpy as np
from picamera2 import Picamera2
height = 480
width = 640
middle=((width//2),(height//2))

cam = Picamera2()
cam.configure(cam.create_video_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
cam.start()

while True:
    frame = cam.capture_array()
    cv2.circle(frame,middle,10,(255,0,255),-1)
    cv2.imshow('camera.test', frame)
    cv2.waitKey(10)
