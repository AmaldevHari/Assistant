#!/usr/bin/env python

import rospy,os,sys

from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
from std_msgs.msg import String

rospy.init_node("aiml_soundplay_client",anonymous=True)

sound_handle= SoundClient()
rospy.sleep(1)
sound_handle.stopAll()
print('Starting TTS')

def get_response(data):
                
        response=data.data
	rospy.loginfo("Response is:%s",response)
	sound_handle.say(response)

def listener():
	
	rospy.loginfo("Starting listening to response")
	rospy.Subscriber("response",String,get_response,queue_size=10)
	rospy.spin()

if __name__=='__main__':
	
	listener()

	
	
