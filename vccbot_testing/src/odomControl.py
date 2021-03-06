#!/usr/bin/env python
import rospy
from math import sqrt
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
# forward is +X
firstOdom = True
speed = 0.1 # 10cm per sec
firstX = 0
currentDist = 0 # Distance traveled forward.
def odomCallback(data):
	global firstX
	global currentDist
	global firstOdom
	if firstOdom:
		firstX = data.pose.pose.position.x
		firstOdom = False
	else:
		currentDist = data.pose.pose.position.x - firstX
	rospy.loginfo("Dist: %s", currentDist)


def main():
	global speed
	cmd_vel_publisher = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
	rospy.init_node('odom_control')
	rospy.Subscriber("/odom", Odometry, odomCallback)
	rate = rospy.Rate(50) # 10hz
	while not rospy.is_shutdown():
		twist_message = Twist()
		twist_message.linear.y = 0 
		twist_message.linear.z = 0
		twist_message.angular.x = 0
		twist_message.angular.y = 0
		twist_message.angular.z = 0
		if currentDist < 0.1:
			twist_message.linear.x = speed
			
			
		else:
			twist_message.linear.x = 0
			rospy.loginfo("Stopping...")
			f = True

		cmd_vel_publisher.publish(twist_message)
		

if __name__ == '__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass
