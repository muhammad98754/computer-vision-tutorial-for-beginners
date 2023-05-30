here i will teach you how you can draw different geometrci shapes like line,circle,rectangle,text etc on images using opencv.

import cv2
import numpy as np #importing numpy library as np.

img=cv2.imread("C:\\Users\\PC\\Downloads\\pexels-secret-garden-931162.jpg")

img=np.zeros([512,512,3],np.uint8) #create an image using numpy zeros method.it will give you a black image on which you can draw your geometric shapes.

cv2.line(img,(0,0),(255,255),(0,0,255),10) #we draw line on image.1st argument is image,2nd argument is starting coordinate of point1,
3rd argument is ending coordinate,4th argument is color and it should be BGR format,5th argument is thickness.

cv2.arrowedLine(img,(0,255),(255,255),(0,255,0),10) #similar to the line but here we get arrowed line

cv2.rectangle(img,(384,0),(510,128),(0,0,255),10) #we draw rectangle on image.the arguments are similar to line.
but here the first coordinate is top left vertex coordinate and second is lower right vertex coordinate.

cv2.circle(img,(447,63),63,(0,255,0),-1) #we draw circle on image.2nd argument is centre coordinate of circle.third argument is radius.
thickness if we use -1 we get filled version of circle.

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,"opencv",(10,500),font,4,(0,255,255),10,cv2.LINE_AA) # to put text on image.2nd argument is the text we want to showcase.
3rd argument is coordinate of textt we want to start from,4th argument is font and 5th argument is font size,next argument is color and thickness.
final argument is line type.

cv2.imshow("window",img)  
cv2.waitKey(0) 
cv2.destroyAllWindows()
