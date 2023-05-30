here i am going to teach you how you can read,write and show images in opencv

import cv2 #here you are importing opencv library

img=cv2.imread("C:\\Users\\PC\\Downloads\\pexels-secret-garden-931162.jpg",1)   #imread () used for reading any images,
inside the imread function you have to provide the image location on your computer.along with that you can provide flags also.
flag 0 means the grayscale image you can show on to your console.flag 1 is for coloured image,and flag -1 is for the unchanged image with alpha channels.
"img" variable is used for storing the image

#print(img) #when you print the variable img we can see that the result will be a pixel matrix.

cv2.imshow("window",img)  #here you are displaying the image using imshow() function.the first argument is name for your window(you can provide any name for your window) 
and the second argument is image variable which read by imread()

k=cv2.waitKey(0) &0xFF #without waitkey the image will disappear soon.so better provide value :zero.so that image will be infinitely stayed.next we give 
the waitkey onto a variable called k.

if k==27: #if we press the escape key

     cv2.destroyAllWindows() #it is for destoying all windows
elif k==ord("g"): #if we press the g key on keyboard
     
           cv2.imwrite("copy.jpg",img) #used for writing an image onto a file just like taking a copy of the image which we have read.
           first argument is name of your new image and second variable is the image itself which read by imread()
           .
           cv2.destroyAllWindows()  #it is for destoying all windows
