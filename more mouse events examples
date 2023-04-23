#the first project is when clicking left button down click event of mouse,draw a circle and when clicking next point join both points by a line

import numpy as np
import cv2
#events=[i for i in dir(cv2) if "EVENT" in i]
#print(events)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),3,(0,0,255),-1) #draw circle, -1 as thickness for filling the circle
        points.append((x,y)) #append into the array x,y coordinates when mouse clicked
        if len(points)>=2: #if length of array more than 2 points
            cv2.line(img,points[-1],points[-2],(255,0,0),5) #then connect the points with line,-1 and -2 are last and second last points of array everytime
            cv2.imshow("window",img)
   
#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("C:\\Users\\PC\\Downloads\\pexels-secret-garden-931162.jpg")
cv2.imshow("window",img)
points=[] #creating array of points
cv2.setMouseCallback("window",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()


#for next example we will show the color of points where we click
import numpy as np
import cv2
#events=[i for i in dir(cv2) if "EVENT" in i]
#print(events)
def click_event(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        blue=img[x,y,0] #getting the blue channel at the corresponding coordinate
        green=img[x,y,1] #getting the green channel
        red=img[x,y,2] #getting the red channel
        cv2.circle(img,(x,y),3,(0,0,255),-1) 3draw a circle on the point
        mycolorimage=np.zeros((512,512,3),np.uint8) #creating an image
        mycolorimage[:]=[blue,green,red] #fill the image with BGR channels
        
        cv2.imshow("windows", mycolorimage)
   
#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread("C:\\Users\\PC\\Downloads\\pexels-secret-garden-931162.jpg")
cv2.imshow("window",img)
points=[]
cv2.setMouseCallback("window",click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
