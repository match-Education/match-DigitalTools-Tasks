#!/usr/bin/env python3
from time import sleep

import rclpy
from rclpy.node import Node

#############################################################################################
# Start of student import section

from geometry_msgs.msg import Twist

# End of student import section
#############################################################################################

#############################################################################################
# Start of student function section



# End of student function section
#############################################################################################

def main(args = None):
    # Initialize ROS2 node and ROS2 communication (e.g. topics)
    rclpy.init(args = args) 

    # Create ROS2 Node. This is used to create for example a topic publisher.
    task_1a_node = Node("task_1a")  

    #############################################################################################
    # Start of student code section

    task_1a_node.get_logger().info("Solution 1a node started.")

    cmd_vel_publisher = task_1a_node.create_publisher(Twist, '/cmd_vel', 10)

    constant_velocity: Twist = Twist()
    constant_velocity.linear.x = 1.0
    cmd_vel_publisher.publish(constant_velocity)

    task_1a_node.get_logger().info("Solution 1a node finished.")   
    
    # End of student code section
    #############################################################################################
    
    # Pause the programm until its killed. All tasks still will be processed in the background.
    rclpy.spin(task_1a_node) 

    # Stops all communication and should always be called last in a node before finishing.
    rclpy.shutdown()

if __name__ == "__main__":
    main()