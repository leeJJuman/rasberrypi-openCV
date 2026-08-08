import cv2
import numpy as np
from picamera2 import Picamera2

def main():
    height = 480
    width = 640
    camera = Picamera2()
    camera.configure(camera.create_video_configuration(main={'format':'XRGB8888', 'size':(width, height)}))
    camera.start()
        
    count = 0
    while(True):
        image = camera.capture_array()
        hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        
        lower_yellow = np.array([15,100,100])
        upper_yellow = np.array([35,255,255])
        lower_red = np.array([170,100,100])
        upper_red = np.array([179,255,255])
        lower_blue = np.array([90,100,100])
        upper_blue = np.array([130,255,255])
        
        mask1=cv2.inRange(hsv,lower_yellow,upper_yellow)
        mask2=cv2.inRange(hsv,lower_red,upper_red)
        mask3=cv2.inRange(hsv,lower_blue,upper_blue)
        masks=mask1|mask2|mask3
        masked=cv2.bitwise_and(image,image,mask=masks)
        
        cv2.imshow('original video',image)
        cv2.imshow('output video',masked)
        
        if cv2.waitKey(1)==ord('q'):
            print('quiting')
            break
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()

