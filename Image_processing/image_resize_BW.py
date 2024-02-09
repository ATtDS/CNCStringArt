from PIL import Image

def resize_and_convert_to_bw(input_image_path, output_image_path, new_width, new_height):
    # Open the image
    with Image.open(input_image_path) as img:
        # Resize the image
        img_resized = img.resize((new_width, new_height))

        # Convert to black and white
        img_bw = img_resized.convert('L')

        # Save the image
        img_bw.save(output_image_path)

# Example usage
input_image = '/Users/eliasabouchaaya/Desktop/CNCStringArt/Image_processing/input/ada.png'  # Replace with your input image path
output_image = 'converted.jpg'  # Replace with your desired output image path
new_width = 300  # Replace with your desired width
new_height = 300  # Replace with your desired height

resize_and_convert_to_bw(input_image, output_image, new_width, new_height)
