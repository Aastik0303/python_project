# UPI payment QR code (payer enters the amount)
# pip install qrcode[pil]

import qrcode
from urllib.parse import quote

upi_id = input("Enter UPI ID (e.g. name@okaxis): ")
name = input("Enter payee name: ")

upi_url = f"upi://pay?pa={upi_id}&pn={quote(name)}&cu=INR"

img = qrcode.make(upi_url)
img.save("upi_qr.png")

print("UPI link:", upi_url)
print("UPI QR code saved as upi_qr.png")
