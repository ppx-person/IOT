from PIL import Image
import os


def read_path(input_filename):
    pic = Image.open(input_filename)
    pic = pic.convert('RGBA')  # 转为RGBA模式
    width, height = pic.size
    array = pic.load()  # 获取图片像素操作入口
    for i in range(width):
        for j in range(height):
            pos = array[i, j]  # 获得某个像素点，格式为(R,G,B,A)元组
            #黑色背景，白色背景改255或者>=240     == 0为黑色背景
            isEdit = (sum([1 for x in pos[0:3] if x == 255]) == 3)
            if i == 0 and j == 0:
                print(pos)
            if isEdit:
                # 更改为透明
                array[i, j] = (255, 255, 255, 0)
    pic.save("out.png")

read_path("input.png")









