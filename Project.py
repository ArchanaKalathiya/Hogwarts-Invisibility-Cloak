import cv2  #comouter vision
import numpy as np 
video = cv2.VideoCapture("Asian women talking to camera with green bg.mp4") #video and image datatype 
image = cv2.imread("Bg1.jpg")
while True :
    ret , frame = video.read()
    frame=cv2.resize(frame, (768,480))
    image = cv2.resize(image,(768,480))
    hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  #HSV - Hue Saturation and Volume
    #creating object to hide background of video 
    l_g=np.array([32,94,132])
    u_g=np.array([179,255,255])
    mask = cv2.inRange(hsv, l_g, u_g)
    res=cv2.bitwise_and(frame,frame, mask=mask)
    f=frame-res
    green_screen=np.where(f==0,image,f)
    # cv2.imshow("Frame", frame)  #imshow has no sound 
    # cv2.imshow("Mask",mask)
    # cv2.imshow("RES",res)
    # cv2.imshow("f",f)
    cv2.imshow("Green_screen",green_screen)
    #print(f) - It is nothing but array 
    k=cv2.waitKey(1)    #Quitting the video on any click - unicode value of the video will be saved inside the k 
    if k == ord('q'):   #ord - function of python returns the unicode value 
        break
video.release()
cv2.destroyAllWindows() #Window that opend up will be closed up - deallocate all the resources

 

