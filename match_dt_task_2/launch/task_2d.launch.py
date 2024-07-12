
from launch import LaunchDescription

from launch.actions import (
    IncludeLaunchDescription,
    TimerAction
)

from launch.substitutions import (
    PathJoinSubstitution,
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
                    "match_empty_world.launch.py"
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
            "yaw": str(0.0),
        }.items()
    )

    task_2d_node = Node(
        package="match_dt_task_2",
        executable="task_2d_node",
        name="task_2d_node",
        output="screen"
    )
    task_2d_node_delayed = TimerAction(period=12.0,
                                        actions=[task_2d_node])

    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_2d_node_delayed
        ]
    )