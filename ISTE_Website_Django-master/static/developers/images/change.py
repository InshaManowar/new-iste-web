from PIL import Image  
  
# Opens a image in RGB mode  
im = Image.open("omkar.jpg")  
  
# Size of the image in pixels (size of orginal image)  
# (This is not mandatory)  
width, height = im.size  
  
# Setting the points for cropped image  
left = 4
top = height / 5
right = 154
bottom = 3 * height / 5
  
# Cropped image of above dimension  
# (It will not change orginal image)  
# im1 = im.crop((left, top, right, bottom)) 
newsize = (640, 640) 
im1 = im.resize(newsize) 
# Shows the image in image viewer  
im1.show()
im1.save('omkar.jpg')
