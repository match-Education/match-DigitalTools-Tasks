
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
                    "match_empty_world.launch.py"
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
        )
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