from PIL import Image, ImageDraw
import random

# Create a large image for the hero background
width, height = 1920, 1080
img = Image.new('RGB', (width, height), color=(245, 245, 250))
draw = ImageDraw.Draw(img)

# Draw some random shapes to make it interesting
for _ in range(50):
    # Random position
    x = random.randint(0, width)
    y = random.randint(0, height)
    
    # Random size
    size = random.randint(20, 200)
    
    # Random color (light blue/purple tones)
    r = random.randint(200, 255)
    g = random.randint(200, 255)
    b = random.randint(230, 255)
    color = (r, g, b)
    
    # Random shape (circle or rectangle)
    shape_type = random.choice(['circle', 'rectangle'])
    
    if shape_type == 'circle':
        draw.ellipse((x, y, x + size, y + size), fill=color)
    else:
        draw.rectangle((x, y, x + size, y + size), fill=color)

# Save the image
img.save('static/images/hero-bg.jpg', quality=90)
print("Hero background created successfully!") 