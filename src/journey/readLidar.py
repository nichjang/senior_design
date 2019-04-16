#Attempt #2 for reading the subscriber
#Author: Ryan Mitchell
#Plugin: gazebo_radar_plugin

import rospy
import time
from geometry_msgs.msg import Point
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import PoseStamped
import tf2_ros
import tf2_msgs.msg
import geometry_msgs.msg

firstIteration = True

#data.header.stamp.secs + data.header.stamp.nsecs for time
#len(data.points) for the length of the data = number of points
#data.points[i].(x y or z for the specific point)
#callback = where it reads the data from the topic
#The x,y,z is the point in free space (http://docs.ros.org/melodic/api/geometry_msgs/html/msg/Point32.html)
#will need the pose of the ardrone to get accurate localization (does 100 in the bottom row, then works up the 16 rows)
def callback(data):
	startTime = time.time()
	global firstIteration
	if firstIteration:
		firstIteration = False
		for i in range(100):
			print "data point: " + str(i)
			print "x: " + str(data.points[i].x)
			print "y: " + str(data.points[i].y)
			print "z: " + str(data.points[i].z)
			print	
	print ("Time to spin = %s" % (time.time() - startTime))
		

#Used to read the pose of the base link
def position(data):
	print "xpose: " + str(data.transforms[0].transform.translation.x)
	print "ypose: " + str(data.transforms[0].transform.translation.y)
	print "zpose: " + str(data.transforms[0].transform.translation.z)

def listener():
	#used to connect to the ROS Master node (replace 10.145.236.187:11311 with Master host IP)
	rospy.init_node('10.145.236.187:11311', anonymous=True)

	#should be the name of the subscriber 
	# rospy.Subscriber('/radar', PointCloud, callback)

	rospy.Subscriber('/tf', tf2_msgs.msg.TFMessage, position)

	#keep reading ths subscriber continuously
	rospy.spin()

		

if __name__ == '__main__':
	listener()
