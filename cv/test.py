import matplotlib, cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('home/yugo/deeplearning/cv/sample.jpg',0)

img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

#plt.imshow(img)
#plt.show()
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img)
plt.show()
