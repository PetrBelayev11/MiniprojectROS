import os
from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_dir = get_package_share_directory('hagen_robot_diff_drive')
    world_file = os.path.join(pkg_dir, 'worlds', 'hagen_world.world')
    model_path = os.path.join(pkg_dir, 'models')


    os.environ['GAZEBO_MODEL_PATH'] = model_path

    gazebo = ExecuteProcess(
        cmd=['gazebo', '--verbose', world_file,
             '-s', 'libgazebo_ros_init.so',
             '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )
    spawn_entity = Node(
        package='hagen_robot_diff_drive',
        executable='spawn_robot',
        arguments=['HagenRobot', 'hagen_robot', '0.0', '0.0', '0.0'],
        output='screen'
    )


    diff_drive_control = Node(
        package='hagen_robot_diff_drive',
        executable='diff_drive_control',
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        spawn_entity,
        diff_drive_control
    ])