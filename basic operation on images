#basic operation on images
import cv2
img=cv2.imread("C:\\Users\\PC\\Downloads\\s.jpg")
img1=cv2.imread("C:\\Users\\PC\\Downloads\\RR.jpg")
print(img.shape) #no.of rows ,coloumns,and channels
print(img.size)#no.of pixels
print(img.dtype)#image datatype
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))



#next is region of interest
#in the picture i have i am moving the ball position to differnet location
ball=img[280:340,330:390]
img[273:333,100:160]=ball#placing the ball another location



cv2.imshow("window",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



#next is adding two images


import cv2
img=cv2.imread("C:\\Users\\PC\\Downloads\\s.jpg")
img1=cv2.imread("C:\\Users\\PC\\Downloads\\RR.jpg")
print(img.shape) #no.of rows ,coloumns,and channels
print(img.size)#no.of pixels
print(img.dtype)#image datatype
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))



#next is region of interest
#in the picture i have i am moving the ball position to differnet location
ball=img[280:340,330:390]
#img[273:333,100:160]=ball#placing the ball another location

#next is adding two images
img=cv2.resize(img,(512,512))
img1=cv2.resize(img1,(512,512))
dst=cv2.add(img,img1)

cv2.imshow("window",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()


#next is we can add weights to both images


import cv2
img=cv2.imread("C:\\Users\\PC\\Downloads\\s.jpg")
img1=cv2.imread("C:\\Users\\PC\\Downloads\\RR.jpg")
print(img.shape) #no.of rows ,coloumns,and channels
print(img.size)#no.of pixels
print(img.dtype)#image datatype
b,g,r=cv2.split(img)
img=cv2.merge((b,g,r))



#next is region of interest
#in the picture i have i am moving the ball position to differnet location
ball=img[280:340,330:390]
#img[273:333,100:160]=ball#placing the ball another location

#next is adding two images
img=cv2.resize(img,(512,512))
img1=cv2.resize(img1,(512,512))
#dst=cv2.add(img,img1)
dst=cv2.addWeighted(img,.9,img1,.1,0) #gamma value is scalar value which is zero here
cv2.imshow("window",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
