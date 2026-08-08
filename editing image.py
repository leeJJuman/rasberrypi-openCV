import cv2

def main():
    image=cv2.imread('jungju.png')
    image_grayscale=cv2.imread('jungju.png',cv2.IMREAD_GRAYSCALE)
    image_fliped=cv2.flip(image,flipCode=0)
    image_rotated=cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image_edges=cv2.Canny(image,30,90)
    image_blur=cv2.GaussianBlur(image,(9,9),0)
    image_circle=cv2.circle(image,(320,240),20,(0,255,0),2)
    image_rectangle=cv2.rectangle(image,(160,160),(480,320),(0,0,255),2)
    
    if cv2.waitKey(1)&0xFF==ord('q'):
        cv2.destroyAllWindows()
    cv2.imshow('1. grayscale',image_grayscale)
    cv2.imshow('2.fliped',image_fliped)
    cv2.imshow('rotated',image_rotated)
    cv2.imshow('4. edges',image_edges)
    cv2.imshow('5. blur',image_blur)
    cv2.imshow('6. basic',image)
    
    cv2.waitKey(0)
    
if __name__=='__main__':
    main()
