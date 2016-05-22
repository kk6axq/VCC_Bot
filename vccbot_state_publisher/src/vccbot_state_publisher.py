#!/usr/bin/env python
import rospy
from std_srvs.srv import Empty
from vccbot_msgs.msg import GlobalState
WAITING=0
MOVING=1
SPIN=2
DISPLAY=3
UNKNOWN=4
currentState = UNKNOWN

def service_move(msg):
	global MOVING
	global currentState
	currentState = MOVING
	return []
def service_waiting(msg):
	global WAITING
	global currentState
	currentState = WAITING
	return []

def service_spin(msg):
	global SPIN
	global currentState
	currentState = SPIN
	return []

def service_display(msg):
	global DISPLAY
	global currentState
	currentState = DISPLAY
	return []
	
def main():
	global_state_publisher = rospy.Publisher('/global_state', GlobalState, queue_size = 10)
	rospy.init_node('vccbot_state_publisher')
	move = rospy.Service('move', Empty, service_move)
	waiting = rospy.Service('waiting', Empty, service_waiting)
	spin = rospy.Service('spin', Empty, service_spin)
	display = rospy.Service('display', Empty, service_display)
	rate = rospy.Rate(30)
	while not rospy.is_shutdown():
		global_state_publisher.publish(currentState)
		rate.sleep()


if __name__ == "__main__":
	main()
