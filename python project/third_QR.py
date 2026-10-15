# QR code with a logo in the centre
# pip install qrcode[pil]

import qrcode
from PIL import Image, ImageDraw

data = "https://www.python.org"

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Use logo.png if present, otherwise draw a simple circular logo
try:
    logo = Image.open("logo.png")
except FileNotFoundError:
    logo = Image.new("RGB", (100, 100), "white")
    ImageDraw.Draw(logo).ellipse((5, 5, 95, 95), fill="red")

# Logo should cover at most ~1/4 of the QR width (ERROR_CORRECT_H keeps it scannable)
logo_size = img.size[0] // 4
logo = logo.resize((logo_size, logo_size))

pos = ((img.size[0] - logo_size) // 2, (img.size[1] - logo_size) // 2)
img.paste(logo, pos)

img.save("third_qr.png")
print("QR code with logo saved as third_qr.png")
