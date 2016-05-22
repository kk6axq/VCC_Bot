#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import serial
disp = serial.Serial("/dev/ttyACM0", 9600)


def serialSend(data):
	disp.write(str(data))



def callback(msg):
	serialSend(msg.data)



def main():
	rospy.init_node('vccbot_display')
	sub = rospy.Subscriber('display', Int32, callback)
	rospy.spin()


if __name__ == "__main__":
	main()
