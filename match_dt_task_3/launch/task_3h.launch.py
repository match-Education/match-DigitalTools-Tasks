from math import pi
from random import random, randint

from launch import LaunchDescription

from launch.actions import (
    IncludeLaunchDescription,
    TimerAction
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
                    "match_empty_hallway_world.launch.py"
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
            "Y": str((random() * 2 * pi) - pi),
            "activate_obstacle_detection": str(True)
        }.items(),
    )

    task_3h_node = Node(
        package="match_dt_task_3",
        executable="task_3h_node",
        name="task_3h_node",
        output="screen"
    )
    task_3h_node_delayed = TimerAction(period=12.0,
                                        actions=[task_3h_node])

    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_3h_node_delayed
        ]
    )