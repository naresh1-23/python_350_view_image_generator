from PIL import Image
from io import BytesIO


def create_360_view(uploaded_images, output_image_path):
    """
    Create a 360-degree panorama effect by combining multiple uploaded images horizontally.

    :param uploaded_images: A list of file-like objects containing the uploaded images.
    :param output_image_path: Path where the 360° panorama image will be saved.
    """
    # Open all uploaded images and store them in a list
    images = [Image.open(image) for image in uploaded_images]

    # Calculate the total width and height for the output image
    total_width = sum(img.size[0] for img in images)
    height = max(img.size[1] for img in images)

    # Create a new blank image with the calculated total width and max height
    panorama_img = Image.new('RGB', (total_width, height))

    # Paste each image into the panorama image
    current_x = 0
    for img in images:
        panorama_img.paste(img, (current_x, 0))
        current_x += img.size[0]

    # Save the resulting panoramic image
    panorama_img.save(output_image_path)
    print(f"360° panorama image saved as {output_image_path}")


# Example usage
# Assuming you have a list of file-like objects from uploads (e.g., from Flask):
uploaded_files = [
    "/home/mango/Downloads/image1.jpeg", "/home/mango/Downloads/image2.jpeg", "/home/mango/Downloads/image3.jpeg",
    "/home/mango/Downloads/image4.jpeg", "/home/mango/Downloads/image5.jpeg"]  # These would be the uploaded image files
create_360_view(uploaded_files, 'panorama.jpg')
