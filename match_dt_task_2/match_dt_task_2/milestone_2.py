#!/usr/bin/env python3
from time import sleep

import rclpy
from rclpy.node import Node

#############################################################################################
# Start of student import section



# End of student import section
#############################################################################################

#############################################################################################
# Start of student class section
class Milestone2Node(Node):
    def __init__(self) -> None:
        super().__init__('milestone_1')



# End of student class section
#############################################################################################

def main(args = None):
    # Initialize ROS2 node and ROS2 communication (e.g. topics)
    rclpy.init(args = args) 

    milestone_2_node: Milestone2Node = Milestone2Node()

    #############################################################################################
    # Start of student code section


    
    # End of student code section
    #############################################################################################
    
    # Pause the programm until its killed. All tasks still will be processed in the background.
    rclpy.spin(milestone_2_node) 

    # Destroy the node explicitly, otherwise garbage collector should do it.
    milestone_2_node.destroy_node()

    # Stops all communication and should always be called last in a node before finishing.
    rclpy.shutdown()

if __name__ == "__main__":
    main()