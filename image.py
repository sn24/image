# import the necessary packages
import numpy as np
import cv2
import matplotlib.pyplot as plt
num = raw_input("Enter how many elements you want:")
num_array = list()
time_array = list()
for i in range(int(num)):
    img = raw_input("enter the name of the image file: ")
    image = cv2.imread(img)                                                                     #load the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)                                              #convert image to grayscale
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)                                      #find the brightest pixel
    num_array.append(maxVal)                                                                    #stores the maxVal in an array
    time = raw_input("enter time")                                                              #takes the time input
    time_array.append(time)
plt.plot(time_array,num_array,'ro')                                                             #plot the intensity vs time graph
plt.show()

