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


if __name__ == '__main__':
    img_list = []
    for i in range(0, 10):
        img = cv2.imread("D:\\tmp\\0.png")
        img_list.append(img)
    img = merge(img_list, "vertical")
    cv2.imwrite("D:\\tmp\\out.png", img)
