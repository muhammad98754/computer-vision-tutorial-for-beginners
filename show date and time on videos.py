#here we are going to show the current date and time on live video using putText feature

import cv2
import datetime #import datetime module
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3,1280)
#cap.set(4,720)
#print(cap.get(3))
#print(cap.get(4))
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        text="width:"+str(cap.get(3))+"height:"+str(cap.get(4)) #width and height also we can show on live video.remember convert the values to string to set as argument in putTex
       
        datet=str(datetime.datetime.now()) #date time convert to str.current datetime saved to to satet variable
        cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)  #putting the text on live vido here the text is current date and time
      
        cv2.imshow("window",frame)

        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    else:
         break
cap.release()
cv2.destroyAllWindows()
