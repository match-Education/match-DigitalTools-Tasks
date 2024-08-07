from math import pi
from random import random, randint

from launch import LaunchDescription

from launch.actions import (
    IncludeLaunchDescription,
    TimerAction
)

from launch.substitutions import (
    PathJoinSubstitution,
    TextSubstitution
)
from launch_ros.substitutions import FindPackageShare

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("dt_gazebo"),
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
                    FindPackageShare("dt_robot_bringup"),
                    "launch",
                    "rosbot_2_sim.launch.py",
                ]
            )
        ),
        launch_arguments={
            "x": TextSubstitution(text=str(2.8)),
            "y": TextSubstitution(text=str(0.0)),
            "Y": TextSubstitution(text=str(float(randint(0,3))*(pi/2))),
        }.items()
    )

    task_3a_node = Node(
        package="match_dt_task_3",
        executable="task_3a_node",
        name="task_3a_node",
        output="screen"
    )
    task_3a_node_delayed = TimerAction(period=12.0,
                                        actions=[task_3a_node])
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_3a_node_delayed
        ]
    )