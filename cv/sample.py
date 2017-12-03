import cv2, matplotlib
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('cat.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
print(img)
plt.imshow(img)

filename = "new_img_cat.png"
plt.savefig(filename)


gray_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
 
print(gray_img)
plt.imshow(gray_img)

filename = "gray_img_cat.png"
plt.savefig(filename)

average_color_per_row = np.average(img, axis=0)
average_color = np.average(average_color_per_row, axis=0)
average_color = np.uint8(average_color)
print(average_color)
average_color_img = np.array([[average_color]*100]*100, np.uint8)
  
plt.imshow(average_color_img)


filename = "average_img_cat.png"
plt.savefig(filename)



# threshold for image, with threshold 60
_, threshold_img = cv2.threshold(gray_img, 60, 255, cv2.THRESH_BINARY)
 
# show image
threshold_img = cv2.cvtColor(threshold_img, cv2.COLOR_GRAY2RGB)
plt.imshow(threshold_img)


filename = "threshold_img_cat.png"
plt.savefig(filename)

piet  = cv2.imread('img_11.jpg')
piet_hsv = cv2.cvtColor(piet, cv2.COLOR_BGR2HSV)
 
# threshold for hue channel in blue range
blue_min = np.array([100, 100, 100], np.uint8)
blue_max = np.array([140, 255, 255], np.uint8)
threshold_blue_img = cv2.inRange(piet_hsv, blue_min, blue_max)
 
threshold_blue_img = cv2.cvtColor(threshold_blue_img, cv2.COLOR_GRAY2RGB)
 
plt.imshow(threshold_blue_img)

filename = "threadhold_blue_sample.png"
plt.savefig(filename)
plt.show()

upstate = cv2.imread('img_11.jpg')
plt.imshow(upstate)
plt.show()
upstate_hsv = cv2.cvtColor(upstate, cv2.COLOR_BGR2HSV)
plt.imshow(cv2.cvtColor(upstate_hsv, cv2.COLOR_HSV2RGB))
plt.show()
filename = "threadhold_1_sample.png"
# get mask of pixels that are in blue range
mask_inverse = cv2.inRange(upstate_hsv, blue_min, blue_max)

# inverse mask to get parts that are not blue
mask = cv2.bitwise_not(mask_inverse)
plt.imshow(cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB))
filename = "threadhold_2_sample.png"
                                               
# convert single channel mask back into 3 channels
mask_rgb = cv2.cvtColor(mask, cv2.COLOR_GRAY2RGB)
                                                            
# perform bitwise and on mask to obtain cut-out image that is not blue
masked_upstate = cv2.bitwise_and(upstate, mask_rgb)
                                                                         
# replace the cut-out parts with white
masked_replace_white = cv2.addWeighted(masked_upstate, 1, \
cv2.cvtColor(mask_inverse, cv2.COLOR_GRAY2RGB), 1, 0)
                                                                                      
plt.imshow(cv2.cvtColor(masked_replace_white, cv2.COLOR_BGR2RGB))

filename = "threadhold_3_sample.png"
plt.savefig(filename)

