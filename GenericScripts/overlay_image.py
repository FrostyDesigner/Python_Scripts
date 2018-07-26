from PIL import Image, ImageFilter
import webbrowser

#for some reason the following line does not open the file
#however is necessary to declare variable
img=Image.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\023.JPG")
#img.show()
#img="C:\\GitHub\\Python_Scripts\\GenericScripts\\023.JPG"
#img=webbrowser.open(img)

#resize image and create new file
size = (640,640)
img.thumbnail(size)
img.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_Little.JPG")
#webbrowser.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_Little.JPG")

#apply a filter
img_blur=img.filter(ImageFilter.BLUR) 
img_blur.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_BLUR.JPG")
img_boxblur=img.filter(ImageFilter.BoxBlur(radius=50))
img_boxblur.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_BoxBlur.JPG")
img_emboss=img.filter(ImageFilter.EMBOSS)
img_emboss.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_EMBOSS.JPG")
img_gaussian=img.filter(ImageFilter.GaussianBlur)
img_gaussian.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_GaussianBlur.JPG")
img_edge_enhance=img.filter(ImageFilter.EDGE_ENHANCE)
img_edge_enhance.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_EDGE_ENHANCE.JPG")

#webbrowser.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_BLUR.JPG")
#webbrowser.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_BoxBlur.JPG")
#webbrowser.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_EMBOSS.JPG")
#webbrowser.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_GaussianBlur.JPG")
#webbrowser.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_EDGE_ENHANCE.JPG")

img2=Image.open("C:\\GitHub\\Python_Scripts\\GenericScripts\\021.JPG")
#resize image and create new file
#size = (640,640)
img2.thumbnail(size)
img2.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\086_Little.JPG")

from PIL import ImageChops
img3=ImageChops.add(img, img2,1,0)
img3.save("C:\\GitHub\\Python_Scripts\\GenericScripts\\023_Combined.JPG")













