
from launch import LaunchDescription

from launch.actions import (
    IncludeLaunchDescription,
    TimerAction
)

from launch.substitutions import (
    PathJoinSubstitution,
    TextSubstitution,
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
            "x": TextSubstitution(text=str(0.0)),
            "y": TextSubstitution(text=str(0.0)),
            "Y": TextSubstitution(text=str(0.0)),
        }.items()
    )

    milestone_2_node = Node(
        package="match_dt_task_2",
        executable="milestone_2_node",
        name="milestone_2_node",
        output="screen"
    )
    milestone_2_node_delayed = TimerAction(period=12.0,
                                            actions=[milestone_2_node])

    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            milestone_2_node_delayed
        ]
    )