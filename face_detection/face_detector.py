import cv2
import os

# errors happen when the file you are trying to read with imread doesn't exist in the current directory.
# This takes the filename of the script and converts it to an absolute path
# then it extracts the directory of that path and changes into that directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img=cv2.imread("photo.jpg",1)
#convert the BGR image to grayscale image
#grayscale images increases curacy so we use grayscale
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#the smaller the scaleFactor value means a higher curacy (more times passed through the object)
#higher number is lower curacy but faster processing (1.05 is 5%)
#higher number (like 1.1 can also eliminate some false positives)
faces=face_cascade.detectMultiScale(gray_img,
scaleFactor=1.05,
minNeighbors=5)

for x, y, w, h in faces:
    img=cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),3)

print(type(faces))
print(faces)

resized=cv2.resize(img,(int(img.shape[1]/3), int(img.shape[0]/3)))

cv2.imshow("Gray", resized)
cv2.waitKey(0)
cv2.destroyAllWindows()
