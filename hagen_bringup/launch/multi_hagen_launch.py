

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import GroupAction
from launch_ros.substitutions import FindPackageShare
import os

def generate_robot_group(robot_name, x_pose, y_pose):
    robot_description_pkg = FindPackageShare('hagen_description').find('hagen_description')
    urdf_file = os.path.join(robot_description_pkg, 'urdf', 'hagen.urdf')

    return GroupAction([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            namespace=robot_name,
            name='robot_state_publisher',
            parameters=[{'robot_description': open(urdf_file).read()}],
            output='screen'
        ),

        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', robot_name,
                       '-x', str(x_pose), '-y', str(y_pose),
                       '-topic', f'/{robot_name}/robot_description'],
            output='screen'
        ),

        Node(
            package='teleop_twist_keyboard',
            executable='teleop_twist_keyboard',
            name=f'{robot_name}_teleop',
            remappings=[('/cmd_vel', f'/{robot_name}/cmd_vel')],
            prefix='xterm -e '
        )
    ])

def generate_launch_description():
    return LaunchDescription([
        generate_robot_group('robot1', 0.0, 0.0),
        generate_robot_group('robot2', 2.0, 0.0),
    ])