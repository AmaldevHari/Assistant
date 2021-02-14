#!/usr/bin/env python

import rospy

from std_msgs.msg import String

publisher=rospy.Publisher('chatter',String,queue_size=10)
rospy.init_node("aiml_client")
rate=rospy.Rate(1)
# 10Hz
while not rospy.is_shutdown():
	
	input=raw_input("Enter  your text:")
	publisher.publish(input)
	rate.sleep()
	

