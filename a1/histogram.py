import numpy as np
import matplotlib.pyplot as plt
from scipy import misc

im = misc.imread('./low_contrast.jpg')

# output image
des = np.zeros(im.shape, dtype=np.int16)

# normalized sum of output image
des_value = np.zeros(256, dtype=np.uint8)

# calculate histogram and cumulative sum
# im.flatten makes multi-dimension array to 1-dimension array
# hist : 1-dimension image's histogram array
# cdf : cumulative sum

hist, bins = np.histogram(im.flatten(), 256, [0, 256])
cdf = hist.cumsum()
max_cdf = max(cdf)
len_cdf = len(cdf)-1

for i in range(len_cdf+1):
    des_value[i] = int(round((cdf[i]/max_cdf)*len_cdf))

for i in range(len(des)):
    for j in range(len(des[0])):
        des[i, j] = des_value[im[i, j]]

des_hist, _ = np.histogram(des.flatten(), 256, [0, 256])
des_cdf = des_hist.cumsum()
plt.imshow(des, cmap='gray')
plt.show()