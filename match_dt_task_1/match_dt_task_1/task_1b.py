#!/usr/bin/env python3
from time import sleep

import rclpy
from rclpy.node import Node

#############################################################################################
# Start of student code section



# End of student code section
#############################################################################################

def main(args = None):
    # Initialize ROS2 node and ROS2 communication (e.g. topics)
    rclpy.init(args = args) 

    # Create ROS2 Node. This is used to create for example a topic publisher.
    task_1b_node = Node("task_1b")  

    # Initial sleep to wait for everything to boot properly.
    sleep(10)

    #############################################################################################
    # Start of student code section

    
    
    # End of student code section
    #############################################################################################
    
    # Pause the programm until its killed. All tasks still will be processed in the background.
    rclpy.spin(task_1b_node) 

    # Stops all communication and should always be called last in a node before finishing.
    rclpy.shutdown()

if __name__ == "__main__":
    main()