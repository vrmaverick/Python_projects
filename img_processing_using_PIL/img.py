from PIL import Image, ImageFilter

while True:
    try:
        path = input("Enter full path of the image file (without qoutes) : ")
        img = Image.open(path)
        break
    except FileNotFoundError:
        print("File not found. Please enter a valid path.")

# Convert the image to RGB mode
while True:
    mode = int(input("Which mode do you want? Press 1 for RGB, press 0 for Black & White: "))
    if mode == 0:
        img_rgb = img.convert("L")
        break
    elif mode == 1:
        img_rgb = img.convert("RGB")
        break
    else:
        print("Enter a valid number.")

# Apply the BLUR filter
new = img_rgb.filter(ImageFilter.SMOOTH_MORE)
rotate = input("Do you wish to rotate? (yes/no) Default will be considered no: ")
if rotate.lower() in ['yes', 'y']:
    degree = int(input("Enter degree for rotation: "))
    rot = new.rotate(degree)
else:
    rot = new.rotate(0)

crop = input("Do you wish to crop the image without disturbing the ratio? (yes/no) Default will be considered no: ")
if crop.lower() in ['yes', 'y']:
    w = int(input("Enter Width: "))
    l = int(input("Enter Length: "))
    rot.thumbnail((w, l))

# Save the filtered image
name = input("Enter name of the PNG file you want to create: ")
save_path = f"C:\\Users\\vedant\\OneDrive\\Desktop\\New folder (5)\\Image_processing\\images\\{name}.png"
print(f"Saving the filtered image to: {save_path}")
rot.save(save_path, 'PNG')

print("Image saved successfully.")
