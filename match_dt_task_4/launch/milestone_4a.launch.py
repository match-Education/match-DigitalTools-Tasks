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
    LaunchConfiguration
)

from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    x = LaunchConfiguration("x")
    declare_x_arg = DeclareLaunchArgument(
        "x",
        default_value="0.0",
        description="x-position of the mobile robot.",
    )

    y = LaunchConfiguration("y")
    declare_y_arg = DeclareLaunchArgument(
        "y",
        default_value="0.0",
        description="y-position of the mobile robot.",
    )

    yaw = LaunchConfiguration("yaw")
    declare_yaw_arg = DeclareLaunchArgument(
        "yaw",
        default_value="0.0",
        description="yaw-orientation of the mobile robot.",
    )

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            PathJoinSubstitution(
                [
                    get_package_share_directory("dt_gazebo"),
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
                    get_package_share_directory("dt_robot_bringup"),
                    "launch",
                    "rosbot_2_sim.launch.py",
                ]
            )
        ),
        launch_arguments={
            "x": str(0.5),
            "y": str(-0.5), 
            "Y": str((random()*((4/3)*pi)) + (1/4)*pi),
            "activate_obstacle_detection": str(True)
        }.items(),
    )

    # launch_arguments={
    #     "x": x
    # }.items(),

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