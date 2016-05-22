#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Int32
def out(matrix):
	one = matrix[0, 0]
	two = matrix[0, 1]
	three = matrix[0, 2]
	four = matrix[1, 0]
	five = matrix[1, 1]
	six = matrix[1, 2]
	seven = matrix[2, 0]
	eight = matrix[2, 1]
	nine = matrix[2, 2]
	ten = matrix[3, 0]
	eleven = matrix[3, 1]
	twelve = matrix[3, 2]
	thirteen = matrix[4, 0]
	fourteen = matrix[4, 1]
	fifteen = matrix[4, 2]
	out = -1
	if one == two and two == two and three == two and four == two and five != two and six == two and seven == two and eight != two and nine == two and ten == two and eleven != two and twelve == two and thirteen == two and fourteen == two and fifteen == two:
		out =  0
	elif one != two and two == two and three != two and four != two and five == two and six != two and seven != two and eight == two and nine != two and ten != two and eleven == two and twelve != two and thirteen != two and fourteen == two and fifteen != two:
		out =  1
	elif one == two and two == two and three == two and four != two and five != two and six == two and seven == two and eight == two and nine == two and ten == two and eleven != two and twelve != two and thirteen == two and fourteen == two and fifteen == two:
		out =  2
	elif one == two and two == two and three == two and four != two and five != two and six == two and seven == two and eight == two and nine == two and ten != two and eleven != two and twelve == two and thirteen == two and fourteen == two and fifteen == two:
		out =  3
	elif one == one and two != one and three != one and four == one and five != one and six == one and seven == one and eight != one and nine == one and ten == one and eleven == one and twelve == one and thirteen != one and fourteen != one and fifteen == one:
		out =  4
	elif one == one and two != one and three != one and four == one and five != one and six != one and seven == one and eight != one and nine == one and ten == one and eleven == one and twelve == one and thirteen != one and fourteen != one and fifteen == one:
		out =  4
	elif one == one and two == one and three == one and four == one and five != one and six != one and seven == one and eight == one and nine == one and ten != one and eleven != one and twelve == one and thirteen == one and fourteen == one and fifteen == one:
		out =  5
	elif one == one and two == one and three == one and four == one and five != one and six != one and seven == one and eight == one and nine == one and ten == one and eleven != one and twelve == one and thirteen == one and fourteen == one and fifteen == one:
		out =  6
	elif one == one and two == one and three == one and four != one and five != one and six == one and seven != one and eight != one and nine == one and ten != one and eleven != one and twelve == one and thirteen != one and fourteen != one and fifteen == one:
		out =  7
	elif one == one and two == one and three == one and four == one and five != one and six == one and seven == one and eight == one and nine == one and ten == one and eleven != one and twelve == one and thirteen == one and fourteen == one and fifteen == one:
		out =  8
	elif one == one and two == one and three == one and four == one and five != one and six == one and seven == one and eight == one and nine == one and ten != one and eleven != one and twelve == one and thirteen != one and fourteen != one and fifteen == one:
		out =  9
	return out

def main():
	display_publisher = rospy.Publisher("/display", Int32, anonymous=False)
	
