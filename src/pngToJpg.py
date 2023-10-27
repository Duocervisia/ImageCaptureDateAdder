
#importing the required package 
from PIL import Image 
import glob


path = "C:/Users/Tobias/Desktop/Instagram"

for filename in glob.glob(path + '/*.png'):
    #open image in png format 
    img_png = Image.open(filename) 

    filename = filename[0:-3] + "jpg"
    
    #The image object is used to save the image in jpg format 
    img_png.save(filename)
