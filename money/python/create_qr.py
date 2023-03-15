import qrcode
from PIL import Image
import cv2
import numpy as np


def create_init_code(data):
    # version 最小版本
    qr = qrcode.QRCode(version=7, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=1, border=0)
    qr.add_data(data)
    # 当fit参数为真或者没有给出version参数时，调用best_fit方法来找到适合数据的最小尺寸
    qr.make(fit=True)
    img = qr.make_image()
    return img


def get_matrix(img):
    width = img.size[0]  
    height = img.size[1] 
    matrix = []
    for h in range(0, height):
        tmp_array = []
        for w in range(0, width):  
            pixel = img.getpixel((w, h))
            pixel = 0 if pixel == 0 else 1
            tmp_array.append(pixel)
        matrix.append(tmp_array)
    return matrix


def draw(matrix, white_img, black_img):
    w_size = len(matrix[0])
    h_size = len(matrix)
    img_w = 22 * w_size
    img_h = 22 * h_size
    
    result = Image.new(white_img.mode, (img_w, img_h))
    for x in range(h_size):
        for y in range(w_size):
            img = white_img if matrix[x][y] == 0 else black_img
            result.paste(img, box=(y * 22, x * 22))
    return np.array(result)


if __name__ == "__main__":
    data = "welcome"
    img = create_init_code(data)
    matrix = get_matrix(img)
    white_img = Image.open("w.jpg")
    black_img = Image.open("b.jpg")
    out_img = draw(matrix, white_img, black_img)
    cv2.imwrite("out.png", out_img)


# img.show()






















