import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=1,
    border=0,
)
qr.add_data('http://192.168.101.108/redsea-fastdev-projects/rootId/fastdev-appweb.git')
qr.make(fit=True)
img = qr.make_image()
filename = 'demo.png'
img.save(filename)





# img.show()






















