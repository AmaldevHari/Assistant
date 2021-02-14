#!/usr/bin/env python

import aiml
import sys
import os
import rospy
from std_msgs.msg import String

bot= aiml.Kernel()
rospy.init_node("aiml_server")
response_publisher =rospy.Publisher("response",String,queue_size=10)
def load_aiml(xml_file):
	
#loads aiml data set given the xml file and command required to invoke learning

	data_path=rospy.get_param("aiml_path")
	print(data_path)
	os.chdir(data_path)
		
	if os.path.isfile("standard.brn"):
		bot.bootstrap(brainFile="standard.brn")
	else:
		bot.bootstrap(learnFiles=xml_file,commands='load aiml b')
		bot.saveBrain("standard.brn")

def callback(data):
	
	input= data.data
	response= bot.respond(input)
	rospy.loginfo("I heard: %s",input)
	rospy.loginfo("I replied: %s",response)
	response_publisher.publish(response)

def listener():
	
	rospy.loginfo("Starting ROS AIML server")
	# subscribe to topic named chatter and  send the String data through callback function
	rospy.Subscriber("chatter",String,callback)
	# endless while loop
	rospy.spin()

# run loop only if executed directly and this module is not imported by other modules
if  __name__ =='__main__' :

	load_aiml("startup.xml")
	listener()
	
