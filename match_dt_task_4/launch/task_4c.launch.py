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

    side_selector: int = randint(0,3)
    x_position: float = 0.0
    y_position: float = 0.0
    if side_selector == 0: # back
        # The gap is on the left side. 
        # Therefore only pick a random spot on the right side of the back wall
        x_position = -1
        y_position = -random() * 0.8 - 0.2 # Only choose the wall a little away from the gap
    elif side_selector == 1: # left
        x_position = random() * 1.5 - 0.5 # Prevent close spawning to the gap
        y_position = 1
    elif side_selector == 2: # front
        x_position = 1
        y_position = random() * 2.0 - 1.0
    elif side_selector == 3: # right
        x_position = random() * 2.0 - 1.0
        y_position = -1

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
            "x": TextSubstitution(text=str(x_position)),
            "y": TextSubstitution(text=str(y_position)),
            "Y": TextSubstitution(text=str(random()*(2*pi))),
        }.items()
    )

    task_4c_node = Node(
        package="match_dt_task_4",
        executable="task_4c_node",
        name="task_4c_node",
        output="screen"
    )
    task_4c_node_delayed = TimerAction(period=12.0,
                                        actions=[task_4c_node])
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_4c_node_delayed
        ]
    )