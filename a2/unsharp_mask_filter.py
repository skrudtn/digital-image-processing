import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

# kernel = np.array(([1,1,1], [1,1,1], [1,1,1]))
# kernel = np.array(([1,2,1], [2,4,2], [1,2,1]))
kernel = np.array(([0,-1,0], [-1,5,-1], [0,-1,0]))
read = misc.imread('sample.jpg')

img = np.array(read, dtype=np.int32)
output = np.zeros(img.shape, dtype=np.uint8)
w = int(len(kernel)/2)


for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        if i == 0 or i == img.shape[0]-1:
            output[i, j] = img[i, j]
        elif j == 0 or j == img.shape[1]-1:
            output[i, j] = img[i, j]
        else:
            sub_sum = 0
            for y in range(-w, w+1):
                for x in range(-w, w+1):
                    sub_sum += kernel[y + w, x + w] * img[y+i, x+j]
            if(sub_sum<0):
                sub_sum = 0
            elif(sub_sum>255):
                sub_sum = 255

            output[i, j] = sub_sum

misc.imsave("output_unsharp_mask_filter.jpg", output)