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
                    "match_room_with_gap_world.launch.py"
                ]
            )
        )
    )

    side_selector: int = randint(0,3)
    x_position: float = 0.0
    y_position: float = 0.0
    if side_selector == 0:
        x_position = -1
        y_position = random() * 2.0 - 1.0
    elif side_selector == 1:
        x_position = random() * 2.0 - 1.0
        y_position = 1
    elif side_selector == 2:
        x_position = 1
        y_position = random() * 2.0 - 1.0
    elif side_selector == 3:
        # The gap is on the left side. 
        # Therefore only pick a random spot on the right side of the back wall
        x_position = random() * 1.0 - 1.0 
        y_position = -1

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
            "x": str(x_position),
            "y": str(y_position),
            "Y": str(random()*(2*pi)),
            "activate_obstacle_detection": str(True)
        }.items(),
    )

    task_4c_node = Node(
        package="match_dt_task_4",
        executable="task_4c_node",
        name="task_4c_node",
        output="screen"
    )
    
    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_4c_node
        ]
    )