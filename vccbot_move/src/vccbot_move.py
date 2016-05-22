#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from vccbot_msgs.msg import GlobalState
from nav_msgs.msg import Odometry
from std_srvs.srv import Empty
import time
#Variables that need to be changed by the user:
moveSpeed = 0.05# Speed to drive at. Units in m/s.
rotationSpeed = 0.5#Speed of rotation in rad/s


#global variables
WAITING=0
MOVING=1
SPIN=2
DISPLAY=3
UNKNOWN=4
currentGlobalState=UNKNOWN
time_at_beginning_spin = 0
firstSpin = True
maxDist = 1
#Variables and function for the odometry/distance measurement system
rotNotDone = True
initialOdometryDist = 0
currentOdomDist = 0
odomFirst = True
def odometryCallback(data):
	global currentGlobalState
	global currentOdomDist
	global WAITING
	global SPIN
	global DISPLAY
	global MOVING
	global UNKNOWN
	global maxDist
	global odomFirst
	if odomFirst:
		odomFirst = False
		odomOffset = data.pose.pose.position.x

	currentOdomDist = data.pose.pose.position.x - odomOffset#get current forward distance value from odometry. +X is forward. This is in meters.
	if currentOdomDist > maxDist and currentGlobalState == MOVING:
			mode_change_spin()


# Variables and functions for the global state system
GSFirst = True
stateName = UNKNOWN # Variable to hold state name to publish
global global_state_publisher

def globalStateCallback(data):
	global currentGlobalState
	global GSFirst
	global stateName
	global WAITING
	global MOVING
	global SPIN
	global DISPLAY
	global UNKNOWN	
	currentGlobalState = data.globalstate
	rospy.loginfo("Updated current global state to %s", currentGlobalState)
	
#Variables and functions for the Twist publisher system

twist_message = Twist() # variable to assemble the message into.

def main():
	global WAITING
	global MOVING
	global SPIN
	global DISPLAY
	global UNKNOWN
	global time_at_beginning_spin
	global firstSpin
	global rotationSpeed
	rospy.wait_for_service('move')
	rospy.wait_for_service('waiting')
	rospy.wait_for_service('display')
	rospy.wait_for_service('spin')
	mode_change_move = rospy.ServiceProxy('move', Empty)
	mode_change_waiting = rospy.ServiceProxy('waiting', Empty)
	mode_change_spin = rospy.ServiceProxy('spin', Empty)
	mode_change_display = rospy.ServiceProxy('display', Empty)
	global global_state_publisher
	global twist_publisher
	twist_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	
	rospy.init_node('vccbot_move', anonymous=False)
	rospy.Subscriber("/global_state", GlobalState, globalStateCallback)
	rospy.Subscriber("/odom", Odometry, odometryCallback)
	rate = rospy.Rate(30)
	while not rospy.is_shutdown():
		global moveSpeed
		#The program doesn't need to shutdown so loop.
		if currentGlobalState == MOVING: # The robot should move forward 
			#drive forward at a constant speed.
			twist_message = Twist()#clear any previous data in the twist_message variable.
			twist_message.linear.x = moveSpeed # These six lines create a Twist message that says move forward.
			twist_message.linear.y = 0
			twist_message.linear.z = 0
			twist_message.angular.x = 0
			twist_message.angular.y = 0
			twist_message.angular.z = 0
			twist_publisher.publish(twist_message)
		elif currentGlobalState == SPIN:# The robot needs to spin
			if firstSpin == True:
				time_at_beginning_spin = time.time()
				firstSpin = False
			if firstSpin == False and time.time() - time_at_beginning_spin > 25.1328:
				mode_change_display()
			else:
				twist_message = Twist()
				twist_message.linear.x = 0
				twist_message.linear.y = 0
				twist_message.linear.z = 0
				twist_message.angular.x = 0
				twist_message.angular.y = 0
				twist_message.angular.z = rotationSpeed#Turn at set number of rad/s
				twist_publisher.publish(twist_message)
			
		rate.sleep()



if __name__ == '__main__':#If this is being run as the main program, run the loop.
	try:
		main()
	except rospy.ROSInterruptException:
		pass

