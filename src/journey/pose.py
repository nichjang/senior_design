#! /usr/bin/env python

from std_msgs.msg import Bool
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist, Vector3, PoseStamped
from ardrone_joy.msg import AutoPilotCmd
import math
import time
import tf
from tf.broadcaster import TransformBroadcaster
import numpy as np
import csv

class pose:
    def __init__(self):
        rospy.init_node('pose', anonymous=True)

        self.listener = tf.TransformListener()
        self.pos_publisher = rospy.Publisher('/ardrone/current_position', PoseStamped, queue_size=10)
        self.publish_pose()
    
    def publish_pose(self):
        while not rospy.is_shutdown():
            try:
                self.listener.waitForTransform("nav", "base_stabilized", rospy.Time(), rospy.Duration(0.1))
                (trans,quaternion) = self.listener.lookupTransform("nav", "base_stabilized", rospy.Time())
            except:
                continue

            pose = PoseStamped()

            pose.header.stamp = rospy.Time.now()
            pose.header.frame_id = "world"
            pose.pose.position.x = trans[0]
            pose.pose.position.y = trans[1]
            pose.pose.position.z = trans[2]

            pose.pose.orientation.x = quaternion[0]
            pose.pose.orientation.y = quaternion[1]
            pose.pose.orientation.z = quaternion[2]
            pose.pose.orientation.w = quaternion[3]
            
            self.pos_publisher.publish(pose)
            
    
if __name__ == '__main__':
    pose()
    rospy.spin()
