
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

    task_1a_node = Node(
        package="match_dt_task_1",
        executable="task_1a_node",
        name="task_1a_node",
        output="screen"
    )
    task_1a_node_delayed = TimerAction(period=12.0,
                                        actions=[task_1a_node])

    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            #task_1a_node
            task_1a_node_delayed
        ]
    )