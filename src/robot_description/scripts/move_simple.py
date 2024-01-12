#!/usr/bin/env python3

import rospy

"""provide velocity(angular and linear) messages for twist
   geometry messages provide geometric messages such as velocity
   navigation messages, provide odometry including dynamic state and location info."""

from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry

def odom_callback():
   msgs=Odometry()
   """ %s:string X, Y coordinate form, string->input(msg.???) """
   rospy.loginfo('X:%s/Y:%s' % (round(msg.pose.pose.position.x,2), round(msg.pose.pose.position.y,2)))

def main():
    #(name, type, message) call_back: conduct logic and subscribed message
    odom_sub= rospy.Subscriber('odom', Odometry, odom_callback)
    twist_pub=rospy.Publisher('cmd_vel', Twist, queue_size=10)

    rospy.init_node('move_simple_node', anonymous=True)
    rate=rospy.Rate(10) #10Hz

    while not rospy.is_shutdown():
        vel_msg =Twist()
        vel_msg.linear.x=0.3
        vel_msg.angular.z=0.3

        twist_pub.publish(vel_msg)
        rate.sleep()

if __name__=='__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
