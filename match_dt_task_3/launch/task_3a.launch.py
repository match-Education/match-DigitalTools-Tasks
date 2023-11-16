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
                    "match_blocked_world.launch.py"
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
            "x": str(2.8),
            "y": str(0.0),
            "Y": str(float(randint(0,3))*(pi/2)),
            "activate_obstacle_detection": str(True)
        }.items(),
    )

    task_3a_node = Node(
        package="match_dt_task_3",
        executable="task_3a_node",
        name="task_3a_node",
        output="screen"
    )
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_3a_node
        ]
    )