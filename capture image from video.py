import cv2
import os
from picamera2 import Picamera2

def main():
    height = 480
    width = 640
    camera = Picamera2()
    camera.configure(camera.create_video_configuration(main={'format':'XRGB8888', 'size':(width, height)}))
    camera.start()
    
    save_dir='/home/dlwjdwnman/Ai_Car/opencv/ex1/ex1pngs'
    isExist = os.path.exists(save_dir)
    if not isExist:
        os.makedirs(save_dir)
        print('The new directory is created!')
        
    count = 0
    while(True):
        image = camera.capture_array()
        cv2.imshow('camera.test',image)
        if cv2.waitKey(1)==ord('s'):
            cv2.imwrite(os.path.join(save_dir,"data_"+'%d.png')%count,image)
            count+=1
            print('image saved')
        elif cv2.waitKey(1)==ord('q'):
            print('quiting')
            break
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()
