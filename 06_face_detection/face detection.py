import cv2
from picamera2 import Picamera2

def detect_bounding_box(vid):
    face_classifier=cv2.CascadeClassifier('/home/dlwjdwnman/haarcascade_frontalface_default.xml')
    gray_image=cv2.cvtColor(vid,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image,1.1,5,minSize=(40,40))
    for (x,y,w,h)in faces:
        cv2.rectangle(vid,(x,y),(x+w,y+h),(0,255,0),	4)
    return faces

def main():
    height = 480
    width = 640
    camera = Picamera2()
    camera.configure(camera.create_video_configuration(main={'format':'XRGB8888', 'size':(width, height)}))
    camera.start()
    
    while(True):
        image_stream = camera.capture_array()
        
        faces=detect_bounding_box(image_stream)
        
        cv2.imshow('camera.test',image_stream)
        
        if cv2.waitKey(1)==ord('q'):
            print('quiting')
            break
    cv2.destroyAllWindows()

if __name__=='__main__':
    main()


