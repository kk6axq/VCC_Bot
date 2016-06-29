# VCC_Bot
My code from the Vision Centric Challenge.

#Installation
Besides the code contained here, this code depends on two packages:
* A modified version of the `robot_upstart` package, available here: https://github.com/kk6axq/robot_upstart/tree/indigo-devel
* The create_autonomy package, available here: https://github.com/AutonomyLab/create_autonomy
Both packages were cloned from the `indigo-devel` branch.
#Robot Upstart
For my use of the serial ports and camera resources, I needed to access dialout and other groups that were assigned to my user.
`robot_upstart` for security reasons, perhaps, uses `setuidguid` to run the ROS launch file as the user, the only disadvantage being that
the process does not inherit the permissions of the user. My solution was to make `sudo` passwordless(VERY risky in normal circumstances) 
and to change the `robot_upstart` package to change users to the user and then run the launch file. 

