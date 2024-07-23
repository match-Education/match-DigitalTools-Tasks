from math import pi
from random import random, randint

from launch import LaunchDescription

from launch.actions import (
    IncludeLaunchDescription,
    DeclareLaunchArgument,
    TimerAction
)

from launch.substitutions import (
    PathJoinSubstitution,
    LaunchConfiguration,
    TextSubstitution
)
from launch_ros.substitutions import FindPackageShare

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    x = LaunchConfiguration("x")
    declare_x_arg = DeclareLaunchArgument(
        "x",
        default_value=TextSubstitution(text=str(0.5)),
        description="x-position of the mobile robot.",
    )

    y = LaunchConfiguration("y")
    declare_y_arg = DeclareLaunchArgument(
        "y",
        default_value=TextSubstitution(text=str(-0.5)),
        description="y-position of the mobile robot.",
    )

    yaw = LaunchConfiguration("yaw")
    declare_yaw_arg = DeclareLaunchArgument(
        "yaw",
        default_value=TextSubstitution(text=str((random()*((4/3)*pi)) + (1/4)*pi)),
        description="yaw-orientation of the mobile robot.",
    )

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    FindPackageShare("dt_gazebo"),
                    "launch",
                    "match_labyrinth_a_world.launch.py"
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
            "x": x,
            "y": y,
            "Y": yaw,
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
            declare_x_arg,
            declare_y_arg,
            declare_yaw_arg,
            gz_sim,
            rosbot2_sim,
            milestone_4_node_delayed
        ]
    )