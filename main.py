from PIL import Image
from io import BytesIO


def create_360_view(uploaded_images, output_image_path):
    images = [Image.open(image) for image in uploaded_images]
    total_width = sum(img.size[0] for img in images)
    height = max(img.size[1] for img in images)
    panorama_img = Image.new('RGB', (total_width, height))
    current_x = 0
    for img in images:
        panorama_img.paste(img, (current_x, 0))
        current_x += img.size[0]
    panorama_img.save(output_image_path)
    print(f"360° panorama image saved as {output_image_path}")


uploaded_files = [
    "/home/mango/Downloads/image1.jpeg", "/home/mango/Downloads/image2.jpeg", "/home/mango/Downloads/image3.jpeg",
    "/home/mango/Downloads/image4.jpeg", "/home/mango/Downloads/image5.jpeg"]
create_360_view(uploaded_files, 'panorama.jpg')
