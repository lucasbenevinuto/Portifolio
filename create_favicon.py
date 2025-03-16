from PIL import Image, ImageDraw, ImageFont

# Create a 32x32 image with a blue background
img = Image.new('RGB', (32, 32), color=(74, 108, 247))
draw = ImageDraw.Draw(img)

# Try to use a font, fall back to default if not available
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

# Draw "AI" text in white
draw.text((5, 5), "AI", fill=(255, 255, 255), font=font)

# Save as ICO
img.save('static/images/favicon.ico')
print("Favicon created successfully!") 