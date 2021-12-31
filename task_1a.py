'''
*****************************************************************************************
*
*        		===============================================
*           		Berryminator (BM) Theme (eYRC 2021-22)
*        		===============================================
*
*  This script is to implement Task 1A of Berryminator(BM) Theme (eYRC 2021-22).
*  
*  This software is made available on an "AS IS WHERE IS BASIS".
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*
*****************************************************************************************
'''

# Team ID:			[ Team-ID ]
# Author List:		[ Names of team members worked on this file separated by Comma: Name1, Name2, ... ]
# Filename:			task_1a.py
# Functions:		detect_shapes
# 					[ Comma separated list of functions in this file ]


####################### IMPORT MODULES #######################
## You are not allowed to make any changes in this section. ##
## You have to implement this task with the three available ##
## modules for this task (numpy, opencv, os)                ##
##############################################################
import cv2
import numpy as np
import os
##############################################################

################# ADD UTILITY FUNCTIONS HERE #################
low=[[0,150,50],[95,150,0],[45,150,50],[15,150,0]]

upp=[[10,255,255],[125,255,255],[75,255,255],[25,255,255]]

colours=['Red','Blue','Green','Orange']


def detect_colour(hsv,x,y):
    for i in range(0,4):
        mask = cv2.inRange(hsv, np.array([low[i]]), np.array([upp[i]]))
        if mask[y,x]==255:
            colour=colours[i]
    return colour

##############################################################

def detect_shapes(img):

	"""
	Purpose:
	---
	This function takes the image as an argument and returns a nested list
	containing details of colored (non-white) shapes in that image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	Returns:
	---
	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image
	
	Example call:
	---
	shapes = detect_shapes(img)
	"""
	    
	detected_shapes = []

	##############	ADD YOUR CODE HERE	##############
	gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	_, thres = cv2.threshold(gray_image, 200, 255, cv2.THRESH_BINARY)
	contours, _ = cv2.findContours(thres, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	count = 0
	for contour in contours:
		if count == 0:
			count = 1
			continue
		lines = cv2.approxPolyDP(
			contour, 0.03 * cv2.arcLength(contour, True), True)

		M = cv2.moments(contour)
		if M['m00'] != 0.0:
			x = int(M['m10']/M['m00'])
			y = int(M['m01']/M['m00'])

	
		if len(lines) == 3:
			detected_shapes.append([detect_colour(hsv,x,y),'Triangle',(x,y)])
		

		elif len(lines) == 4:
			(a, b, c, d) = cv2.boundingRect(lines)
			temp = c / float(d)
			if(temp >= 0.95 and temp <= 1.05):
				detected_shapes.append([detect_colour(hsv,x,y),'Square',(x,y)])
			else:
				detected_shapes.append([detect_colour(hsv,x,y),'Rectangle',(x,y)])

		elif len(lines) == 5:
		
			detected_shapes.append([detect_colour(hsv,x,y),'Pentagon',(x,y)])
		
		elif len(lines) == 6:
			detected_shapes.append([detect_colour(hsv,x,y),'Hexagon',(x,y)])
	
		else:
			detected_shapes.append([detect_colour(hsv,x,y),'Circle',(x,y)])

	
	##################################################
	
	return detected_shapes

def get_labeled_image(img, detected_shapes):
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########
	"""
	Purpose:
	---
	This function takes the image and the detected shapes list as an argument
	and returns a labelled image

	Input Arguments:
	---
	`img` :	[ numpy array ]
			numpy array of image returned by cv2 library

	`detected_shapes` : [ list ]
			nested list containing details of colored (non-white) 
			shapes present in image

	Returns:
	---
	`img` :	[ numpy array ]
			labelled image
	
	Example call:
	---
	img = get_labeled_image(img, detected_shapes)
	"""
	######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THIS FUNCTION #########    

	for detected in detected_shapes:
		colour = detected[0]
		shape = detected[1]
		coordinates = detected[2]
		cv2.putText(img, str((colour, shape)),coordinates, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)
	return img

if __name__ == '__main__':
	
	# path directory of images in 'test_images' folder
	img_dir_path = 'test_images/'

	# path to 'test_image_1.png' image file
	file_num = 1
	img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
	
	# read image using opencv
	img = cv2.imread(img_file_path)
	
	print('\n============================================')
	print('\nFor test_image_' + str(file_num) + '.png')
	
	# detect shape properties from image
	detected_shapes = detect_shapes(img)
	print(detected_shapes)
	
	# display image with labeled shapes
	img = get_labeled_image(img, detected_shapes)
	cv2.imshow("labeled_image", img)
	cv2.waitKey(2000)
	cv2.destroyAllWindows()
	
	choice = input('\nDo you want to run your script on all test images ? => "y" or "n": ')
	
	if choice == 'y':

		for file_num in range(1, 16):
			
			# path to test image file
			img_file_path = img_dir_path + 'test_image_' + str(file_num) + '.png'
			
			# read image using opencv
			img = cv2.imread(img_file_path)
	
			print('\n============================================')
			print('\nFor test_image_' + str(file_num) + '.png')
			
			# detect shape properties from image
			detected_shapes = detect_shapes(img)
			print(detected_shapes)
			
			# display image with labeled shapes
			img = get_labeled_image(img, detected_shapes)
			cv2.imshow("labeled_image", img)
			cv2.waitKey(2000)
			cv2.destroyAllWindows()


