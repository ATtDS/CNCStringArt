from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def image_to_points(image_path, output_size, num_points):
    # Load the image
    img = Image.open(image_path).convert('L')  # Convert to grayscale

    # Resize the image
    img = img.resize(output_size)

    # Convert image to numpy array
    img_array = np.array(img)

    # Select points
    threshold = np.quantile(img_array, 1 - num_points / np.prod(output_size))
    points = np.argwhere(img_array < threshold)

    # Normalize points to the range [0, 1]
    points_normalized = points / np.array(output_size)

    return points_normalized

def display_points(points, output_size):
    # Convert points to x and y arrays
    x, y = points[:, 1], points[:, 0]

    # Plot the points
    plt.scatter(x, -y, s=1)  # Negative y to flip the image to the correct orientation
    plt.xlim(0, output_size[0])
    plt.ylim(-output_size[1], 0)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage
image_path = '/Users/eliasabouchaaya/Desktop/CNCStringArt/Image_processing/input/ada.png'  # Path to your image
output_size = (100, 100)  # Size of the output image in points
num_points = 500  # Number of points

points = image_to_points(image_path, output_size, num_points)
display_points(points, output_size)
