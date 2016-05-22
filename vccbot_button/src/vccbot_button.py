#!/usr/bin/env python
import rospy
import os

import Adafruit_BBIO.GPIO as GPIO
from std_srvs.srv import Empty
from vccbot_msgs.msg import GlobalState

pin = "P8_12" # Which pin the button is connected to.

WAITING=0
UNKNOWN=4
currentGlobalState=UNKNOWN
def cleanupTime():
	GPIO.cleanup()
	print "cleanup"



def getState():
	state = False
	value = GPIO.input(pin)
	if value == 1:
		state = True

	#print value
	return state

def global_state_callback(data):
	global currentGlobalState
	currentGlobalState = data.globalstate

def main():
	global currentGlobalState
	os.system("sudo chmod a+rwx /sys/class/gpio/ -R")
	os.system("sudo chmod a+rwx /dev/ -R")#chmod the serial and video
	global WAITING
	mode_change_move = rospy.ServiceProxy('move', Empty)
	mode_change_waiting = rospy.ServiceProxy('waiting', Empty)
	rospy.on_shutdown(cleanupTime)
	GPIO.setup(pin, GPIO.IN)
	#GPIO.input(pin) #returns val.
	rospy.init_node('go')
	rospy.Subscriber('global_state', GlobalState, global_state_callback)
	rate = rospy.Rate(30)#loop at 30Hz
	while not rospy.is_shutdown():
		if getState():
			if currentGlobalState == WAITING:
				mode_change_move()
				rospy.sleep(1)
			else:
				mode_change_waiting()
				rospy.sleep(1)				
		rate.sleep()
if __name__ == "__main__":
	main()
