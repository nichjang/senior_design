import rospy
import time
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from pprint import pprint
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseWithCovarianceStamped

NANOSECONDS = 10**9

true_pos_stamps = []
true_pos_x = []
true_pos_y = []

amcl_pos_stamps = []
amcl_pos_x = []
amcl_pos_y = []


def true_pos(data):
	time_stamp = data.header.stamp
	seconds = float(time_stamp.secs) + time_stamp.nsecs/NANOSECONDS
	
	true_pos_stamps.append(seconds)
	true_pos_x.append(data.pose.pose.position.x)
	true_pos_y.append(data.pose.pose.position.y)

def amcl_pos(data):
	time_stamp = data.header.stamp
	seconds = float(time_stamp.secs) + time_stamp.nsecs/NANOSECONDS

	amcl_pos_stamps.append(seconds)
	amcl_pos_x.append(data.pose.pose.position.x)
	amcl_pos_y.append(data.pose.pose.position.y)

def publish_data():
	fig = plt.figure()
	ax = fig.gca(projection='3d')
	ax.plot(np.array(true_pos_stamps), np.array(true_pos_x), np.array(true_pos_y), label='true position')
	ax.legend()

	plt.show()

def listener():
	rospy.init_node('position_error', anonymous=True, disable_signals=True)

	rospy.Subscriber('/ground_truth/state', Odometry, true_pos)
	rospy.Subscriber('/amcl_pose', PoseWithCovarianceStamped, amcl_pos)
	
	t_end = time.time() + 5
	while time.time() < t_end:
		pass
	publish_data()
	rospy.signal_shutdown('end')

def plot_data():
	pass


if __name__ == '__main__':
	listener()

	

	
