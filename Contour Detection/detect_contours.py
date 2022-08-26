import cv2
import numpy as np
  
# Let's load a simple image with 3 black squares
# Naming a window
cv2.namedWindow("Contours", cv2.WINDOW_NORMAL)
  
# Using resizeWindow()
# cv2.resizeWindow("Resized_Window", 300, 700)
image = cv2.imread('D:\SystemFols\Downloads\\sardar_patel_ring_road_khari.png')
print(image)
# Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  
# Find Canny edges
edged = cv2.Canny(gray, 30, 200)
cv2.waitKey(0)
edged = cv2.GaussianBlur(edged,(5,5),0)
# Finding Contours
# Use a copy of the image e.g. edged.copy()
# since findContours alters the image
contours, hierarchy = cv2.findContours(edged, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  
cv2.imshow('Canny Edges After Contouring', edged)
cv2.waitKey(0)
  
print("Number of Contours found = " + str(len(contours)))
  
# Draw all contours
# -1 signifies drawing all contours
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)
  
# cv2.imshow('Contours', image)

cv2.imwrite("sardar_patel_ring_road_khari.png",image)
cv2.waitKey(0)
cv2.destroyAllWindows()