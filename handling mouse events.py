#opencv support for detecting mouse events.these mouse events include mouse clicks like left button down and up,double click
#capturing mouse click events with opencv and python is easy.we just need to create callback function and call this callback function using cv2.setmousecallback method

import numpy as np
import cv2


#events=[i for i in dir(cv2) if "EVENT" in i]
#print(events) #printing all events in cv2.it will show all classes,functions,variables etc


def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN: #when clicking left button down,sthen show x,y coordinates on image
        print(x, ",",y)
        font=cv2.FONT_HERSHEY_SIMPLEX
        strxy=str(x)+","+str(y)
        cv2.putText(img,strxy,(x,y),font,1,(255,255,0),2) #x,y values as text showing on image
        cv2.imshow("window",img) #show the text on image using imshow()
    elif event==cv2.EVENT_RBUTTONDOWN: #when clicking right button down,sthen show x,y coordinates on image
        blue=img[x,y,0] #channel for blue color is zero
        green=img[x,y,1] #channel for green color is one
        red=img[x,y,2] #channel for red color is two
        font=cv2.FONT_HERSHEY_SIMPLEX
        strxy=str(blue)+","+str(green)+","+str(red)
        cv2.putText(img,strxy,(x,y),font,.5,(0,255,255),2) #to show BGR channels on the image
        cv2.imshow("window",img)
img=np.zeros((512,512,3),np.uint8) #createing black image using numpy zeros,2nd argument is datatype
cv2.imshow("window",img) #showing the black image
cv2.setMouseCallback("window",click_event) #to call our call back function that is click_event,"window name" should be the same
cv2.waitKey(0)
cv2.destroyAllWindows()
