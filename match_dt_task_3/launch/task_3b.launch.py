
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
                    "match_blocked_world.launch.py"
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
            "activate_obstacle_detection": str(True)
        }.items(),
    )

    task_3b_node = Node(
        package="match_dt_task_3",
        executable="task_3b_node",
        name="task_3b_node",
        output="screen"
    )
    task_3b_node_delayed = TimerAction(period=12.0,
                                        actions=[task_3b_node])

    return LaunchDescription(
        [
            gz_sim,
            rosbot2_sim,
            task_3b_node_delayed
        ]
    )