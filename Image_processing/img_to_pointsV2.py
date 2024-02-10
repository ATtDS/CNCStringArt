import cv2 
import numpy as np
import matplotlib.pyplot as plt

def image_to_points(image_path, output_size, num_points):
    # Load the image in grayscale
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Resize the image
    img = cv2.resize(img, output_size)

    # Apply Canny edge detection
    edges = cv2.Canny(img, 100, 200)

    # Find indices of edge points
    points = np.argwhere(edges > 0)

    # Reduce the number of points if necessary
    if len(points) > num_points:
        # Randomly select 'num_points' from the available edge points
        points = points[np.random.choice(len(points), num_points, replace=False)]

    # Normalize points to the range [0, 1]
    points_normalized = points / np.array(output_size)

    return points_normalized

def display_points(points, output_size):
    # Convert points to x and y arrays
    x, y = points[:, 1], points[:, 0]

    # Plot the points
    plt.scatter(x, -y, s=1)
    plt.xlim(0, output_size[0])
    plt.ylim(-output_size[1], 0)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()

# Example usage
image_path = '/Users/eliasabouchaaya/Desktop/CNCStringArt/Image_processing/input/ada.png'  # Path to your image
output_size = (100, 100)  # Size of the output image in points
num_points = 10000  # Number of points

points = image_to_points(image_path, output_size, num_points)
display_points(points, output_size)
