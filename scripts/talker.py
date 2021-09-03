#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('state_id', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i=0
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        if i%100==0:
            hello_str='Idle'
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        i=i+1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass