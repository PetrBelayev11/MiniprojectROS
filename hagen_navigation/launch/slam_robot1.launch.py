from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='slam_toolbox',
            executable='sync_slam_toolbox_node',
            namespace='robot1',
            parameters=['config/slam_config.yaml'],
            remappings=[('/scan', '/robot1/scan')]
        )
    ])