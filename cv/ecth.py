import numpy as np
import matplotlib , cv2
import matplotlib.pyplot as plt

cups = cv2.imread('sample.jpg')
         
# preprocess by blurring and grayscale
cups_preprocessed  = cv2.cvtColor(cv2.GaussianBlur(cups, (7,7), 0), cv2.COLOR_BGR2GRAY)
                      
# find binary image with thresholding
_, cups_thresh = cv2.threshold(cups_preprocessed,190, 255, cv2.THRESH_BINARY)
plt.imshow(cv2.cvtColor(cups_thresh, cv2.COLOR_GRAY2RGB))
plt.show()
#plt.savefig("sample_black.png")
