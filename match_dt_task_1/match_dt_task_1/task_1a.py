#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args = None):
    # Initialize ROS2 node. 
    rclpy.init(args = args)

    task_1a_node = Node("task_1a")
    task_1a_node.get_logger().info("test")

    
    rclpy.spin(task_1a_node)

    # Last line
    rclpy.shutdown()

if __name__ == "__main__":
    main()