from PIL import Image 
import numpy as np
from tqdm import tqdm

def bayer(n):
    if n == 1:
        return np.array([[0,2],[3,1]])/((2*n)**2)
    M = np.array(((2*n)**2)*bayer(n/2))
    return np.concatenate((np.concatenate((M, M+2), axis=1), np.concatenate((M+3, M+1), axis=1)), axis=0)/((2*n)**2)

image_name = '3.jpg'
original_image = Image.open(image_name)

image_matrix = np.array(original_image) 
image_size = image_matrix.shape[:2]
# original_image.show()

grayscale_matrix = np.array([
    [
        np.average(image_matrix[i][j]) for j in range(image_size[1])
    ]
    for i in tqdm(range(image_size[0]), 'creating grayscale')
])

grayscale_image = Image.fromarray(grayscale_matrix)
# grayscale_image.show()

window_size = int(input('Enter Window Size:   '))//2

matrix = bayer(window_size)*255
print(matrix)

print(matrix.shape)

dithered_matrix = np.zeros((image_size[0], image_size[1]))

for x in range(image_size[0]):
    for y in range(image_size[1]):
        i = x % matrix.shape[0]
        j = y % matrix.shape[1]
        if grayscale_matrix[x][y] > matrix[i][j]:
            dithered_matrix[x][y] = 255
        else:
            dithered_matrix[x][y] = 0

dithered_image = Image.fromarray(dithered_matrix)
# print(dithered_matrix)
dithered_image.show()
# print(dithered_matrix.shape)