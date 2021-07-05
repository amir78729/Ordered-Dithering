from PIL import Image 
import numpy as np
from tqdm import tqdm

image_name = '3.jpg'
original_image = Image.open(image_name)
image_matrix = np.array(original_image) 
image_size = image_matrix.shape[:2]
print(image_size[0])
print(image_size[1])

grayscale_matrix = np.array([
    [
        np.average(image_matrix[i][j]) for j in range(image_size[1])
    ]
    for i in tqdm(range(image_size[0]), 'creating grayscale')
])

result = Image.fromarray(grayscale_matrix)
result.show()