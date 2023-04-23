#binding trackbars to opencv windows
import cv2
import numpy as np
def nothing(x): #callback function
    print(x) #know the position of trackbar
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("window") #create a window with name
cv2.createTrackbar("B","window",0,255,nothing)#create trackbar on window
cv2.createTrackbar("G","window",0,255,nothing)#create trackbar on window
cv2.createTrackbar("R","window",0,255,nothing)#create trackbar on window
switch="0:OFF 1:ON"
cv2.createTrackbar(switch,"window",0,1,nothing)#create trackbar on window
while True:
    cv2.imshow("window",img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    b=cv2.getTrackbarPos("B","window")
    g = cv2.getTrackbarPos("G", "window")
    r = cv2.getTrackbarPos("R", "window")
    s = cv2.getTrackbarPos(switch, "window")
    if s==0: #when switch position at zero no color change
        img[:]=0
    else:  #when switch position at one  color change takes place
        img[:] = [b, g, r]

    
cv2.destroyAllWindows()

#track bar position printed on the same colored and grayscale image

import cv2
import numpy as np


def nothing(x):
    print(x)


cv2.namedWindow("image")
cv2.createTrackbar("CP", "image", 10, 400, nothing)

switch = "color/gray"
cv2.createTrackbar(switch, "image", 0, 1, nothing)
while True:
    img = cv2.imread("C:\\Users\\PC\\Downloads\\pexels-secret-garden-931162.jpg")
    pos = cv2.getTrackbarPos("CP", "image")
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255))

    s = cv2.getTrackbarPos(switch, "image")
    if s == 0:
        pass
    else:

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("image", img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
