
from PIL import Image
import sys   
im = Image.open("demo.png")  
width = im.size[0]  
height = im.size[1]  
print("/* width:%d */"%(width))
print("/* height:%d */"%(height))
count = 0
matrix = []
for h in range(0, height):
  tmp_array = []
  for w in range(0, width):  
    pixel = im.getpixel((w, h))
    pixel = 0 if pixel == 0 else 1
    tmp_array.append(pixel)
  matrix.append(tmp_array)
#print(len(array_result))
#print(array_result)
print(matrix)





  




