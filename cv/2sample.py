import numpy as np
import cv2, matplotlib
import matplotlib.pyplot as plt

img = cv2.imread('img_11.jpg')
filename = "new_img_11.png"
plt.imshow(img)
plt.show()
#plt.savefig(filename)
         
# gaussian blurring with a 5x5 kernel
img_blur_small = cv2.GaussianBlur(img, (15,15), 0)
plt.imshow(img_blur_small)
plt.show()
#plt.savefig(filename)
