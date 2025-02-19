import PIL 
from PIL import Image

img=PIL.Image.open("file location")
width,height=img.size
print(width,"X",height)
