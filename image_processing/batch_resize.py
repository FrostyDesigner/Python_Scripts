import cv2
import glob
import os

# This takes the filename of the script and converts it to an absolute path
# then it extracts the directory of that path and changes into that directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

#to get images in the current directory
images=glob.glob("*.jpg")
#to get images in a specified directory
# images=glob.glob("C:\\GitHub\\Python_Scripts\\image_processing\\*.jpg")

for image in images:
    fname=os.path.basename(image)
    img=cv2.imread(image,0)
    re=cv2.resize(img,(200,200))
    #show the resized image with the original name displayed in the window header
    cv2.imshow(fname,re)
    #show for how many milliseconds - 0 means wait until user hits key
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

    #write the new image to a file
    cv2.imwrite("resized_"+fname,re)