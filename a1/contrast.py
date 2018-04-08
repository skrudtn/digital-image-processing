import matplotlib.pyplot as plt
from scipy import misc
import numpy as np

GRADIENT = 3
img = misc.imread('low_contrast.jpg')
im2 = np.zeros((img.shape), dtype=np.int16)

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        im2[i,j] = img[i,j] + (img[i,j]-128)*GRADIENT
        if im2[i,j]>255:
            im2[i,j] = 255
        elif im2[i,j]<0:
            im2[i,j]=0


plt.imshow(im2, cmap='gray')
plt.show()
