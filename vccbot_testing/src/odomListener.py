#!/usr/bin/env python
import rospy
import math
from nav_msgs.msg import Odometry

first = True
firstX = 0
firstY = 0
deltaX = 0
deltaY = 0
d = 0
def callback(data):
	global first
	global firstX
	global firstY
	global deltaX
	global deltaY
	global d
	if first:
		firstX = data.pose.pose.position.x
		firstY = data.pose.pose.position.y
		first = False
	else:
		deltaX = data.pose.pose.position.x - firstX
		deltaY = data.pose.pose.position.y - firstY
		d = math.sqrt((deltaX*deltaX) + (deltaY*deltaY))
		rospy.loginfo(rospy.get_caller_id() + "Distance is %s", d)
	#rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.pose.pose)	
	
def listener():
	rospy.init_node('listener')
	rospy.Subscriber("/odom", Odometry, callback)
	rospy.spin()

if __name__ == '__main__':
	listener()
