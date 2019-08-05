#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + " I heard {}".format(data.data))


def subscriber_node():

    rospy.init_node('subscriber_plane', anonymous=True)
    rospy.Subscriber('vectorABC', String, callback)
    
    # spin keeps the node running until it is shutdown
    rospy.spin()


if __name__ == '__main__':
    subscriber_node()
