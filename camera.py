import cv2
# start camera
cap=cv2.VideoCapture(0)
#  status of camera
if   cap.isOpened() : 
     print("camera is ready to take pictures")
else :
	 print("check your web cam drivers")
status,img=cap.read()




cv2.imshow('liveimage',img)
cv2.waitKey(0)
cap.release()       