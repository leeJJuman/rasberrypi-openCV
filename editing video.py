import cv2
import numpy as np
from picamera2 import Picamera2

def main():
    cam = Picamera2()
    cam.configure(cam.create_video_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    cam.start()

    print("Camera Started. Press 'q' to quit.")

    while True:
        frame = cam.capture_array()
        
        edges = cv2.Canny(frame, 100, 200)
        flipped = cv2.flip(edges, 1)
        
        cv2.imshow('camera.test', flipped)
        
        if cv2.waitKey(1) == ord('q'):
            print("Quitting...")
            break
            
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()


