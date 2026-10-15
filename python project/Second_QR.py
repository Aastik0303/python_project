# QR code with custom settings (size, border, colours)
# pip install qrcode[pil]

import qrcode

data = input("Enter text or URL for the QR code: ")

qr = qrcode.QRCode(
    version=1,                                         # 1 to 40, controls grid size
    error_correction=qrcode.constants.ERROR_CORRECT_H, # L, M, Q, H
    box_size=10,                                       # pixels per box
    border=4,                                          # boxes of white border
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="darkblue", back_color="white")
img.save("second_qr.png")

print("QR code saved as second_qr.png")
