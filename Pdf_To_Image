from PIL import Image
import fitz  

def convert_pdf_to_images(pdf_path):
    images = extract_images_from_pdf(pdf_path)
    for index, image in enumerate(images):
        r = resize_image(image)
        r.save(f'output/{pdf_path}-{index}.png')


def extract_images_from_pdf(pdf_path):
    images = []
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)
    doc.close()
    return images


# def resize_image(image):
#     width, height = image.size
#     aspect_ratio = width / height

#     new_width = min(width, height)
#     new_height = int(new_width / aspect_ratio)

#     resized_image = image.resize((new_width, new_height), Image.LANCZOS)

#     # Create a blank white canvas of 1080x1080 size
#     new_image = Image.new("RGB", (1080, 1080), (255, 255, 255))

#     # Paste the resized image onto the center of the canvas
#     x_offset = (1080 - new_width) // 2
#     y_offset = (1080 - new_height) // 2
#     new_image.paste(resized_image, (x_offset, y_offset))

#     return new_image

def resize_image(image):
    width, height = image.size
    aspect_ratio = width / height

    # Calculate the new dimensions to fit within a 1000x1000 square
    if aspect_ratio > 1:
        new_width = min(width, 1000)
        new_height = int(new_width / aspect_ratio)
    else:
        new_height = min(height, 1000)
        new_width = int(new_height * aspect_ratio)

    resized_image = image.resize((new_width, new_height), Image.LANCZOS)

    # Create a blank white canvas of 1000x1000 size
    print("Enter Canvas size or size of the image")
    h=input("Height in pixels")
    w= input("Width in pixels")
    new_image = Image.new("RGB", (h, w), (255, 255, 255))

    # Paste the resized image onto the center of the canvas
    x_offset = (1000 - new_width) // 2
    y_offset = (1000 - new_height) // 2
    new_image.paste(resized_image, (x_offset, y_offset))

    return new_image


def task():
    pdf = input("Enter name of pdf with .pdf extension ")
    convert_pdf_to_images(pdf)
    # convert_pdf_to_images('example-multipage.pdf')


if __name__ == "__main__":
    task()
