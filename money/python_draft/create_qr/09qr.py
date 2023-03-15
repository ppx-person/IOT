from PIL import Image
import qrcode

# 要生成二维码的视频链接地址
data = 'https://www.bilibili.com/bangumi/play/ss5761?spm_id_from=333.999.0.0'
# 生成的二维码保存地址及名称
img_file = 'new_out.png'
# logo图片所在位置


# 实例化QRCode生成qr对象
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
    )

# 向二维码中添加信息
qr.add_data(data)

# 当fit参数为真或者没有给出version参数时，调用best_fit方法来找到适合数据的最小尺寸
qr.make(fit=True)

# 将实例转换成图片并设置为彩色
img = qr.make_image()
img = img.convert('RGBA')


def insertImg(img, logo):
    # 获取二维码图片的宽高
    img_w,img_h = img.size

    # 打开logo图片

    # 获取logo图片的宽高
    logo_w,logo_h = logo.size

    # 设置logo的大小最大为二维码大小的四分之一
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_h / factor)

    if logo_w > size_w or logo_h > size_h:
        logo_w = size_w
        logo_h = size_h

    # 重新调整logo的尺寸，高质量彩色
    logo = logo.resize((logo_w, logo_h), Image.ANTIALIAS).convert('RGBA')

    # 设置logo的位置，在二维码图片的中心
    l_w = int((img_w - logo_w)/2)
    l_h = int((img_h - logo_h)/2)

    # 将logo粘贴到二维码上
    img.paste(logo, (l_w, l_h), logo)

    # 保存二维码
    img.save(img_file)


img = Image.open("qr.png")
logo_file = 'logo.png'
logo = Image.open(logo_file)
insertImg(img, logo)

# 展示二维码
# img.show()