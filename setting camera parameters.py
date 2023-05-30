import cv2
import datetime
cap=cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#cap.set(3,1280) #setting camera parameter where CAP_PROP_FRAME_WIDTH=3,width of this vedio set as 1280
#cap.set(4,720)   #setting camera parameter where CAP_PROP_FRAME_HEIGHT=4,height of this vedio set as 720
#print(cap.get(3)) #printing frame width
#print(cap.get(4)) #printing frame height
while cap.isOpened():
    ret,frame=cap.read()
    if ret==True:
        font=cv2.FONT_HERSHEY_SIMPLEX
        text="width:"+str(cap.get(3))+"height:"+str(cap.get(4))
        datet=str(datetime.datetime.now())
        cv2.putText(frame,datet,(10,50),font,1,(0,255,255),2,cv2.LINE_AA)
      
        cv2.imshow("window",frame)

        if cv2.waitKey(1) & 0xFF==ord("q"):
            break
    else:
         break
cap.release()
cv2.destroyAllWindows()
