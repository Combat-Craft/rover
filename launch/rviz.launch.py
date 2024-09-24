import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare
from launch.substitutions import LaunchConfiguration
from launch.conditions import IfCondition
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_path = FindPackageShare(package='rover').find('rover')
    urdf_model_path = os.path.join(pkg_path, 'urdf', 'model.urdf')
    rviz_config_path = os.path.join(pkg_path, 'config', 'config.rviz')
    
    print(f"Loading URDF from path : {urdf_model_path}")
    
    with open(urdf_model_path, 'r') as infp:
        robot_desc = infp.read()
    
    params = {'robot_description': robot_desc}
    
    rsp = IncludeLaunchDescription(
                PythonLaunchDescriptionSource([os.path.join(
                    get_package_share_directory('rover'),'launch','rsp.launch.py'
                )]), launch_arguments={'use_sim_time': 'true'}.items()
    )  
    joint_state_publisher_node = Node(
        package='joint_state_publisher',
        executable='joint_state_publisher',
        name='joint_state_publisher',
        parameters=[params]
    )

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui',
        condition=IfCondition(LaunchConfiguration('gui'))
    )

    rviz2_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', rviz_config_path]
    )

    return LaunchDescription([
        DeclareLaunchArgument(name='gui', default_value='True',
                              description='Flag to enable joint_state_publisher_gui'),
        rsp,
        joint_state_publisher_node,
        joint_state_publisher_gui_node,
        rviz2_node
    ])
