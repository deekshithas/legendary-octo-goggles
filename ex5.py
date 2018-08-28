#image cropping
import cv2
import numpy as pd
img=cv2.imread("flower.jpg")
height,width=img.shape[:2]
#let's get the starting pixel coordinates(top left,of cropping rectangles)
start_row,start_col=int(height*.25),int(width*.25)
#let's get the ending pixel coordinates(bottom left,of cropping rectangles) 
end_row,end_col=int(height*.75),int(width*.75)
#simply use the indexing to crop the image
cropped=img[start_row:end_row,start_col:end_col]
cv2.imshow("original image",img)
cv2.waitKey(0)
cv2.imshow("cropped",cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
