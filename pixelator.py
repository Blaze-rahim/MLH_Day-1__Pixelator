from PIL import Image
import os

img = Image.open("image2.jpg")
 
img2 = img.resize((250, 250))
 
result = img2.resize(img.size,Image.NEAREST)
 
result.save('result.png')
os.startfile('result.png')