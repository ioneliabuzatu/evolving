#!/usr/bin/env python

import numpy as np
import rosbag
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge
import cv2
import matplotlib.pyplot as plt
from disparityPlaneRos import disparityPlane
from rospy.numpy_msg import numpy_msg
import rospy
    

def reading(bag, left, right, totimages, config_camera_path):
    pub = rospy.Publisher('vectorABC', String, queue_size=10)
    rospy.init_node('publisher_node', anonymous=True)
    rate = rospy.Rate(10)

    for id in range(totimages):
        topic_left, msg_left, ts_left = list(bag.read_messages(images_left))[id]
        topic_right, msg_right,ts_right = list(bag.read_messages(images_right))[id]
        # print(dir(msg_left))
        # print(msg_left.data)
        
        cv_img_left = bridge.imgmsg_to_cv2(msg_left, desired_encoding="passthrough")      
        cv_img_right = bridge.imgmsg_to_cv2(msg_right, desired_encoding="passthrough")   
        
        name = ts_left
        #print(name)
        
        vectorABC = disparityPlane(leftImage=cv_img_left, rightImage=cv_img_right, configFilePath=config_camera_path, name=name, SAVE=True)
        # print(vectorABC)
        vectorABC = str(vectorABC)
        rospy.loginfo(vectorABC)
        pub.publish(vectorABC)
        rate.sleep()


if __name__ == '__main__':
    try:

        config_camera_path = '/home/lia/catkin-ws/src/plane/scripts/input/cam_oxford.yml'
        bag = rosbag.Bag('/home/lia/catkin-ws/src/plane/scripts/kitti_2011_09_26_drive_0001_synced.bag')
        bridge = CvBridge()
        tot_images = bag.get_message_count(topic_filters=['/kitti/camera_gray_left/image_raw'])
        # print(tot_images)

        images_left = '/kitti/camera_gray_left/image_raw'
        images_right = '/kitti/camera_gray_right/image_raw'    

        reading(bag, images_left, images_right, tot_images, config_camera_path)
    except rospy.ROSInterruptException:
        pass








