from PIL import Image
import numpy as np

image = Image.open("download.jpeg")
image_array = np.asarray(image)

rgb_values = image_array.reshape(-1, image_array.shape[-1])

unique_colors, color_counts = np.unique(rgb_values, axis=0, return_counts=True)

colors_count = {tuple(k): v for k, v in zip(unique_colors, color_counts)}

colors_count = dict(sorted(colors_count.items(), key=lambda x: x[1], reverse=True)[:10])

print(len(unique_colors))
print(len(rgb_values))
print(len(color_counts))
print(color_counts)
print(colors_count)
