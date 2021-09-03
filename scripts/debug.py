#!/usr/bin/env python
import rospy
from commun.msg import commu

def talker():
    pub = rospy.Publisher('commu', commu, queue_size=10)
    rospy.init_node('debug', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    i=0
    msg = commu(x=1,y=1,isUnload=True)
    while not rospy.is_shutdown():
        rospy.loginfo(msg)
        pub.publish(msg)
        i=i+1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass