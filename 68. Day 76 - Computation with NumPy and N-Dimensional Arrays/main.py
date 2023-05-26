import numpy as np
import matplotlib.pyplot as plt
from scipy import misc, ndimage
from PIL import Image

array_2d = np.array([[1, 2, 3, 9],
                     [5, 6, 7, 8]])

print(array_2d.shape)
print(array_2d.size)
print(array_2d.ndim)
print(array_2d[1, 3])

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])  # 3D array

# Note all the square brackets!
print(mystery_array.ndim)
print(mystery_array[:, :, 0])

custom_array = np.arange(10, 29, 1)
print(custom_array)
print(custom_array[-3:])
print(custom_array[12:])
print(custom_array[0::2])
print(np.flip(custom_array))

# Use NumPy to generate a 3x3x3 array with random numbers
random_array = np.random.randint(0, 100, (3, 3, 3))
print(random_array)

# Print out all the indices of the non-zero elements in this array: [6,0,9,0,0,5,0]
non_zero_array = np.array([6.2, 0, 9, 0, 0, 5, 0])
print(np.nonzero(non_zero_array))

print(np.linspace(0, 100, 9, dtype=int))
print(np.linspace(-3, 3, 9))
plt.plot(np.linspace(0, 100, 9, dtype=int), np.linspace(-3, 3, 9))
# plt.show()

# Use NumPy to generate an array called noise with shape 128x128x3 that has random values. Then use Matplotlib's
# .imshow() to display the array as an image.
noise = np.random.randint(0, 255, (128, 128, 3))
plt.imshow(noise)
# plt.show()

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
print(v1 + v2)

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])
print(np.matmul(a1, b1))
print(a1 @ b1)

# img = (misc.face() / 255) @ [0.2126, 0.7152, 0.0722]
img = misc.face()
img = ndimage.rotate(img, 90)
img = 255 - img
# plt.imshow(img, cmap='gray', origin='upper')
plt.imshow(img)
# plt.show()

print('here')
img = Image.open('yummy_macarons.jpg')
img = np.array(img)
