import numpy
import cv2

# img = cv2.imread("galaxy.jpg",0)
img = cv2.imread("C:\\GitHub\\Python_Scripts\\image_processing\\galaxy.jpg",1)
#1 is RGB (3 band color), 0 is gray scale (1 band), -1 for images with transparency

print(type(img))
print(img)
print(img.shape)
print(img.ndim)

# resized_image=cv2.resize(img, (1000,500))
# resized_image=cv2.resize(img, (500,1000))
# resize by dividing by 2 - must convert the resulting float to integer
resized_image=cv2.resize(img, (int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy", resized_image)
cv2.imwrite("Galaxy_resized.jpg", resized_image)
#waitKey at 0 would wait until the user presses a key
cv2.waitKey(0)
# cv2.waitKey(2000)
cv2.destroyAllWindows()
