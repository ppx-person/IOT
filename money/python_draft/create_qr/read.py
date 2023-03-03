from PIL import Image
import sys   
im = Image.open("D:\\tmp\\w.jpg")  
width = im.size[0]  
height = im.size[1]  
print("/* width:%d */"%(width))
print("/* height:%d */"%(height))
count = 0

array_result = []
for h in range(0, height):  
  for w in range(0, width):  
    pixel = im.getpixel((w, h))
    array_result.append(pixel)
    """
    for i in range(0,3):  
      count = (count+1)%16  
      if count == 0:  
        array_result.append(pixel[i])
      else:
        array_result.append(pixel[i])
    """
print(len(array_result))
print(22*22)
