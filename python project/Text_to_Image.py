# Convert text into an image
# pip install pillow

from PIL import Image, ImageDraw, ImageFont

text = input("Enter text: ")

try:
    font = ImageFont.truetype("arial.ttf", 40)
except OSError:
    font = ImageFont.load_default()

# Measure the text to size the image
left, top, right, bottom = ImageDraw.Draw(Image.new("RGB", (1, 1))).textbbox((0, 0), text, font=font)
padding = 30
width = right - left + 2 * padding
height = bottom - top + 2 * padding

img = Image.new("RGB", (width, height), "white")
draw = ImageDraw.Draw(img)
draw.text((padding - left, padding - top), text, fill="black", font=font)

img.save("text_image.png")
print("Image saved as text_image.png")
