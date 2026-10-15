# UPI payment QR code with a fixed amount
# pip install qrcode[pil]

import qrcode
from urllib.parse import quote

upi_id = input("Enter UPI ID (e.g. name@okaxis): ")
name = input("Enter payee name: ")
amount = float(input("Enter amount (INR): "))
note = input("Enter payment note: ")

upi_url = (
    f"upi://pay?pa={upi_id}&pn={quote(name)}"
    f"&am={amount:.2f}&cu=INR&tn={quote(note)}"
)

img = qrcode.make(upi_url)
img.save("specific_amount_qr.png")

print("UPI link:", upi_url)
print(f"QR code for Rs {amount:.2f} saved as specific_amount_qr.png")
