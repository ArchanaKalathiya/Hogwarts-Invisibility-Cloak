import cv2
import numpy as np 
video = cv2.VideoCapture("Asian women talking to camera with green bg.mp4") #video and image datatype 
image = cv2.imread("Bg2.jpg")
while True :
    ret , frame = video.read()
    frame=cv2.resize(frame, (640,480))
    image = cv2.resize(image,(640,480))
    cv2.imshow("Frame", frame)  #imshow has no sound 
    k=cv2.waitKey(1)    #Quitting the video on any click - unicode value of the video will be saved inside the k 
    if k == ord('q'):   #ord - function of python returns the unicode value 
        break
video.release()
cv2.destroyAllWindows() #Window that opend up will be closed up - deallocate all the resources



