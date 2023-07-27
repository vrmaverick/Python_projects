from PIL import Image, ImageFilter

img = Image.open(r'.\images\Neon-Tetra-4.png')

# Convert the image to RGB mode
img_rgb = img.convert("RGB")

# Apply the BLUR filter
new = img_rgb.filter(ImageFilter.SMOOTH_MORE)

# Save the filtered image
name = input("Enter name of png file you want to create: ")
save_path = f".\\images\\{name}.png"
print(f"Saving the filtered image to: {save_path}")
new.save(save_path, 'PNG')

print("Image saved successfully.")
