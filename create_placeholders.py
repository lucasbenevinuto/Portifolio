import os
from PIL import Image, ImageDraw, ImageFont
import random

# Create directories if they don't exist
os.makedirs('static/images', exist_ok=True)
os.makedirs('static/files', exist_ok=True)

# Function to create a placeholder image with text
def create_placeholder_image(filename, width, height, text, bg_color=None):
    if bg_color is None:
        # Generate a random pastel color
        r = random.randint(200, 255)
        g = random.randint(200, 255)
        b = random.randint(200, 255)
        bg_color = (r, g, b)
    
    # Create image with background color
    image = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(image)
    
    # Try to use a font, fall back to default if not available
    try:
        font = ImageFont.truetype("arial.ttf", 30)
    except IOError:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    text_width, text_height = draw.textsize(text, font=font) if hasattr(draw, 'textsize') else (width//2, height//2)
    position = ((width - text_width) // 2, (height - text_height) // 2)
    
    # Draw text
    draw.text(position, text, fill=(50, 50, 50), font=font)
    
    # Save the image
    image.save(f'static/images/{filename}')
    print(f"Created {filename}")

# Create project images
create_placeholder_image('project1.jpg', 800, 500, 'Machine Learning Fraud Detection')
create_placeholder_image('project2.jpg', 800, 500, 'NLP for Customer Service')
create_placeholder_image('project3.jpg', 800, 500, 'Computer Vision for Retail')

# Create profile image
create_placeholder_image('profile.jpg', 500, 500, 'Profile Photo', bg_color=(100, 149, 237))

# Create a placeholder resume PDF
try:
    from fpdf import FPDF
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Data Scientist & AI Engineer Resume", ln=True, align='C')
    pdf.cell(200, 10, txt="This is a placeholder resume file.", ln=True)
    pdf.output("static/files/resume.pdf")
    print("Created resume.pdf")
except ImportError:
    print("FPDF not installed. Skipping resume creation.")
    # Create an empty file as a placeholder
    with open("static/files/resume.pdf", "w") as f:
        f.write("Placeholder resume file")

print("All placeholder files created successfully!") 