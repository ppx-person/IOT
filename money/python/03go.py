# coding=utf-8
from PIL import Image
import cv2
import numpy as np


def draw(matrix, white_img, black_img):
    w_size = len(matrix[0])
    h_size = len(matrix)
    print(h_size)
    print(w_size)
    img_w = 22 * w_size
    img_h = 22 * h_size
    
    img1 = Image.open("D:\\tmp\\w.jpg")
    img2 = Image.open("D:\\tmp\\b.jpg")
    result = Image.new(img1.mode, (img_w, img_h))
    
    for x in range(h_size):
        for y in range(w_size):
            img = img1 if matrix[x][y] == 0 else img2
            result.paste(img, box=(y * 22, x * 22))
    return np.array(result)



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

white_img = cv2.imread("D:\\tmp\\w.jpg")
black_img = cv2.imread("D:\\tmp\\b.jpg")
out_img = draw(matrix, white_img, black_img)
cv2.imwrite("out.png", out_img)










  





