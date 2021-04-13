#!/usr/bin/env python3

import rospy
import message_filters # To Achieve Multiple subscriber
from std_msgs.msg import Float32
from std_msgs.msg import String

class VESC_Node(object):
    def __init__(self):

        rospy.init_node("test_sub_py", anonymous=True)

        # Rate
        self.loop_rate = rospy.Rate(60)

        # Node is subscribing to the topic
        self.vesc1_sub = message_filters.Subscriber('steve_vesc1', Float32)
        self.vesc2_sub = message_filters.Subscriber('steve_vesc2', Float32)
        #self.vesc1_sub = rospy.Subscriber('steve_vesc1', Float32, self.callback)
        #self.vesc2_sub = rospy.Subscriber('steve_vesc2', Float32, self.callback)


        # Node is publishing to the topic
        #self.vesc1_pub = rospy.Publisher('/steve_vesc1', Float32, queue_size=10)
        #self.vesc2_pub = rospy.Publisher('/steve_vesc2', Float32, queue_size=10)

    def callback(self,vesc1_data, vesc2_data):
        rospy.loginfo("I heard %s", vesc1_data.data)
        rospy.loginfo("I heard %s", vesc2_data.data)

    def start(self):

        # Tells rospy the name of the node.
        # Anonymous = True makes sure the node has a unique name. Random
        # numbers are added to the end of the name. 

        #Only for multiple subscribers
        ts = message_filters.ApproximateTimeSynchronizer([self.vesc1_sub, self.vesc2_sub], 10, 0.01, allow_headerless=True)
        ts.registerCallback(self.callback)

        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
        
        #while not rospy.is_shutdown():
            #self.vesc1_pub.publish(1.0324)
            #self.vesc2_pub.publish(9.7777)

        #    self.loop_rate.sleep()
        

if __name__ == '__main__':
    my_node = VESC_Node()
    my_node.start()
    
