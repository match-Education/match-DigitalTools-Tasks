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
                    "match_labyrinth_b_world.launch.py"
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
            "x": TextSubstitution(text=str(0.5)),
            "y": TextSubstitution(text=str(-2.8)),
            "Y": TextSubstitution(text=str((random()*((4/3)*pi)) - (5/4)*pi)),
        }.items()
    )

    milestone_4_node = Node(
        package="match_dt_task_4",
        executable="milestone_4_node",
        name="milestone_4_node",
        output="screen"
    )
    milestone_4_node_delayed = TimerAction(period=12.0,
                                        actions=[milestone_4_node])
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            milestone_4_node_delayed
        ]
    )