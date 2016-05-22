#!/usr/bin/env python
#file for testing rosimage to cv2 conversion
import rospy
import cv2
import numpy as np
from cv_bridge import CvBridge
from sensor_msgs.msg import Image
from array import array
image = 0

WAITING=0
MOVING=1
SPIN=2
DISPLAY=3
UNKNOWN=4

def image_callback(data):
	global image
	global MOVING
	if currentGlobalState == MOVING
	image = CvBridge().imgmsg_to_cv2(data, desired_encoding="passthrough")[:, 160]
	image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def global_state_update(data):
	global currentGlobalState
	currentGlobalState = data.globalstate

def round_to_nearest(num, divisor):
	return int(divisor * round(float(num) / divisor))


def checkImage(_image):
	prev_value = 0
	out = array("I")
	for i in range(0, 240):
		b = int(_image[i, 0])
		if not prev_value == b and int(_image[i+1, 0]) == b:
			out.append()
	return out 
		
	

def main():
	global MOVING
	global IMAGE
	rospy.init_node('camera_listener', anonymous=False)
	rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
	rospy.Subscriber("/global_state", GlobalState, global_state_update) 
	while not rospy.is_shutdown():
		if currentGlobalState == MOVING:
			#Time to check the images.
			image[:, 0] = round_to_nearest(image[:, 0], 10)
			checkImage(image)


if __name__ == "__main__":
	main()
