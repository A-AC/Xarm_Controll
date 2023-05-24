#!/usr/bin/env python
import rospy
from xarm_planner.srv import pose_plan
from xarm_planner.srv import exec_plan
from geometry_msgs.msg import Pose


#rosservice call /xarm/move_line [250,100,300,3.14,0,0] 200 2000 0 0
# /xarm/move_line
# [x, y, z, 3.14, 0, 0] {max speed} {max acceleration}

main_pose = Pose()

if __name__ == '__main__':
    print("Xarm Controller Running")
    rospy.init_node("Controller")
    rate = rospy.Rate(100)

    while not rospy.is_shutdown():
        rospy.wait_for_service('xarm_pose_plan')
        rospy.wait_for_service('xarm_exec_plan')
        planner = rospy.ServiceProxy('xarm_pose_plan', pose_plan)
        executor = rospy.ServiceProxy('xarm_exec_plan', exec_plan)

        x = input("x: ")
        y = input("y: ")
        z = input("z: ")

        main_pose.position.x=x
        main_pose.position.y=y
        main_pose.position.z=z

        main_pose.orientation.x=1.0
        main_pose.orientation.y=0.0
        main_pose.orientation.z=0.0
        main_pose.orientation.w=0.0

        planner.call(main_pose)
        executor.call(True)
    
        rate.sleep()