# coding=utf-8
from PIL import Image
import cv2
import numpy as np


def merge(img_array, direction="horizontal", gap=0):
    img_array = [Image.fromarray(img) for img in img_array]
    w, h = img_array[0].size
    if direction == "horizontal":
        result = Image.new(img_array[0].mode, ((w + gap) * len(img_array) - gap, h))
        for i, img in enumerate(img_array):
            result.paste(img, box=((w + gap) * i, 0))
    elif direction == "vertical":
        result = Image.new(img_array[0].mode, (w, (h + gap) * len(img_array) - gap))
        for i, img in enumerate(img_array):
            result.paste(img, box=(0, (h + gap) * i))
    else:
        raise ValueError("The direction parameter has only two options: horizontal and vertical")
    return np.array(result)


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
            print("x:%s,y:%s" % (x, y))
            img = img1 if matrix[x][y] == 0 else img2
            result.paste(img, box=(y * 22, x * 22))
    return np.array(result)


if __name__ == '__main__':
    white_img = cv2.imread("D:\\tmp\\w.jpg")
    black_img = cv2.imread("D:\\tmp\\b.jpg")
    print("---begin---")
    img_array = [Image.fromarray(img) for img in white_img]
    print(img_array[0].mode)
    
    
    matrix = [
    [0, 1, 0, 1],
    [1, 1, 1, 0]
    ]
    out_img = draw(matrix, white_img, black_img)
    cv2.imwrite("D:\\tmp\\out.png", out_img)
    exit()
    
    # <<<<<<<
    
    img_list = []
    
    for i in range(0, 10):
        if i % 2 == 0:
            img_list.append(w_img)
        else:
            img_list.append(b_img)
    img = merge(img_list, "vertical")
    cv2.imwrite("D:\\tmp\\out.png", img)
