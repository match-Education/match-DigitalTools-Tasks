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
                    "match_right_turn_world.launch.py"
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
            "x": str(0.0),
            "y": str(0.0),
            "Y": TextSubstitution(text=str((random() * 2 * pi) - pi)),
        }.items()
    )

    milestone_3_node = Node(
        package="match_dt_task_3",
        executable="milestone_3_node",
        name="milestone_3_node",
        output="screen"
    )
    milestone_3_node_delayed = TimerAction(period=12.0,
                                            actions=[milestone_3_node])
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            milestone_3_node_delayed
        ]
    )