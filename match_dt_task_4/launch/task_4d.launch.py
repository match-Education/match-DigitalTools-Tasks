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
                    "match_room_with_gap_world.launch.py"
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
            "x": TextSubstitution(text=str(0.5 * random())),
            "y": TextSubstitution(text=str(0.5 * random())),
            "Y": TextSubstitution(text=str((random()*((4/3)*pi)) - (4/3)*pi/2)),
        }.items()
    )

    task_4d_node = Node(
        package="match_dt_task_4",
        executable="task_4d_node",
        name="task_4d_node",
        output="screen"
    )
    task_4d_node_delayed = TimerAction(period=12.0,
                                        actions=[task_4d_node])
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_4d_node_delayed
        ]
    )