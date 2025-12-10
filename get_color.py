from PIL import Image
import os

image_path = r'c:\Users\quile\.gemini\antigravity\scratch\Calculadora\spectra\surgery_laptop.png'

try:
    img = Image.open(image_path)
    # Get the color of the top-left pixel (usually the background)
    pixel = img.getpixel((0, 0))
    
    # Convert to hex
    if len(pixel) == 4:
        r, g, b, a = pixel
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print(f"Color: {hex_color}, Alpha: {a}")
    else:
        r, g, b = pixel
        hex_color = '#{:02x}{:02x}{:02x}'.format(r, g, b)
        print(f"Color: {hex_color}")

except Exception as e:
    print(f"Error: {e}")
