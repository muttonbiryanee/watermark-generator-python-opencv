import cv2
import numpy as np

img=cv2.imread(r"C:\Users\Saif\PycharmProjects\opencv2\Resources\flower.jpg")
img=cv2.resize(img,(720,480))

blank=np.zeros_like(img)

cv2.putText(blank,"Venom",(img.shape[0]//2-50,img.shape[1]//2),cv2.FONT_HERSHEY_SIMPLEX,3,(255,255,0),3)

final=cv2.addWeighted(img,1,blank,0.4,0)

cv2.imshow("blank",final)

cv2.waitKey(0)
