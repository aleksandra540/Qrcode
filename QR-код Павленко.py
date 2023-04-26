import qrcode
qr = qrcode.QRCode(
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://vk.com/molbert_ptd')
qr.make(fit=True)

img = qr.make_image(fill_color="black", Back_color="white")
img.save("qrcode8.jpg", "JPEG")
