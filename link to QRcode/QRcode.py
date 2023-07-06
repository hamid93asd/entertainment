import qrcode

data = "https://www.instagram.com"  # or put any links you want

qr = qrcode.QRCode(version=1, box_size=10, border=5)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color='black', back_color='white')

img.save('myQRcode.png')
