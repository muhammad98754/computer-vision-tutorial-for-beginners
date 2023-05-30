here i am going to teach you how you can read ,write and show videos from camera in opencv.

import cv2

cap=cv2.VideoCapture(0) #we can provide vedio file name also.here i have provided the device index zero.videocapture class will help you to capture the video.

fourcc_code=cv2.VideoWriter_fourcc(*'XVID') 

out=cv2.VideoWriter("window.mp4",fourcc_code,20,(640,480)) #for saving the video use Videowriter class.first argument is name of output file 
second argument is fourcc code.its is a 4byte code. third argument is number of frames per second and 4th argument is size.size you will get from get() below.

#print(cap.isOpened()) #to check if the video is opened or not.

while cap.isOpened(): #to cature the frames continously we use while loop also you can use (while True:)

    ret,frame=cap.read() #read() cature the frames and return true if frame avilable.
    
    if ret==True: 
        

           print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) #you can read the properties like frame width and frame height.
           print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))#you can read the properties like frame width and frame height.
           out.write(frame) #writing the frame to the file using write().
           gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting video input from coloured to gray scale,cvtCOLOR is simply convert color.
           cv2.imshow("window",gray)  #show the frame 

           if cv2.waitKey(1) & 0xFF==ord("q"): #based on user input we can close the window.
               
               break
    else:
         break

cap.release() #releasing the resources.
out.release() #releasing the resources.
cv2.destroyAllWindows() #destroy the windows
