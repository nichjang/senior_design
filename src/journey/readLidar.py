#Attempt #2 for reading the subscriber
#Author: Ryan Mitchell
#Plugin: gazebo_radar_plugin

import rospy
from geometry_msgs.msg import Point
from sensor_msgs.msg import PointCloud

#data.header.stamp.secs + data.header.stamp.nsecs for time
#len(data.points) for the length of the data = number of points
#data.points[i].(x y or z for the specific point)
#callback = where it reads the data from the topic
def callback(data):
	print (data.points[0].x)

def listener():
	#used to connect to the ROS Master node (replace 10.145.236.187:11311 with Master host IP)
	rospy.init_node('10.145.236.187:11311', anonymous=True)

	#should be the name of the subscriber 
	rospy.Subscriber('/radar', PointCloud, callback)

	#keep reading ths subscriber continuously
	rospy.spin()
	

if __name__ == '__main__':
	listener()
