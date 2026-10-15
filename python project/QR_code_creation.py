# Basic QR code creation
# pip install qrcode[pil]

import qrcode

data = "https://www.google.com"

img = qrcode.make(data)
img.save("basic_qr.png")

print("QR code saved as basic_qr.png")
