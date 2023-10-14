#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args = None):
    # Initialize ROS2 node and ROS2 communication (e.g. topics)
    rclpy.init(args = args) 

    # Create ROS2 Node. This is used to create for example a topic publisher.
    task_1a_node = Node("task_1a")  

    #############################################################################################
    # Start of student code section

    task_1a_node.get_logger().info("Task 1a node was started.")
    
    # End of student code section
    #############################################################################################
    
    # Pause the programm until its killed. All tasks still will be processed in the background.
    rclpy.spin(task_1a_node) 

    # Stops all communication and should always be called last in a node before finishing.
    rclpy.shutdown()

if __name__ == "__main__":
    main()