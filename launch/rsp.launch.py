from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_name = 'rover'  # Your package name
    urdf_file_name = 'model.urdf'  # URDF file of your robot

    urdf_path = os.path.join(
        get_package_share_directory(package_name),
        'urdf',
        urdf_file_name
    )

    # Robot state publisher node
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': urdf_path}],
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Simulated time default to false'
        ), 
        robot_state_publisher_node,
    ])
