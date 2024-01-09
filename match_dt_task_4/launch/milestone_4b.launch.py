from math import pi
from random import random, randint

from launch import LaunchDescription

from launch.actions import (
    IncludeLaunchDescription,
)

from launch.substitutions import (
    PathJoinSubstitution,
)

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    get_package_share_directory("dt_gazebo"),
                    "launch",
                    "match_labyrinth_b_world.launch.py"
                ]
            )
        )
    )

    rosbot2_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    get_package_share_directory("dt_robot_bringup"),
                    "launch",
                    "rosbot_2_sim.launch.py",
                ]
            )
        ),
        launch_arguments={
            "x": str(0.55),
            "y": str(-2.55), 
            "Y": str(random()*(2*pi)),
            "activate_obstacle_detection": str(True)
        }.items(),
    )

    milestone_4_node = Node(
        package="match_dt_task_4",
        executable="milestone_4_node",
        name="milestone_4_node",
        output="screen"
    )
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            milestone_4_node
        ]
    )