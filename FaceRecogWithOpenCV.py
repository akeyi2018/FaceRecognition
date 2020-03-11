import cv2
import time
import threading

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

def faceThread(img):
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    casecade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml"
    #casecade_path = "/usr/local/share/OpenCV/haarcascades/haarcascade_fullbody.xml"

    face_cascade = cv2.CascadeClassifier(casecade_path)
    faces = face_cascade.detectMultiScale(gray)
    color = (255,0,255)
    
    if len(faces) > 0 :
        for rect in faces:
            w = rect[0] + int(rect[3]/2)
            h = rect[1] + int(rect[3]/2)
            cv2.rectangle(img, tuple(rect[0:2]), tuple(rect[0:2]+rect[2:4]), color, thickness =2)
            #cv2.circle(img, (w,h), 5, (255,255,0), -1)
        #cv2.imwrite("/home/pi/detected.jpg", img)
        return img
        #return w

def Test():

    while True:
        ret, frame = cap.read() 
        img = faceThread(frame)

        try:
            cv2.imshow("camera capture",img)
            time.sleep(0.001)
        except:
            #print("ERROR")
            continue
            
        if cv2.waitKey(1) & 0xFF == ord("q"):
            exit()
        
        
Test()
cap.release()
cv2.destroyAllWindows()
