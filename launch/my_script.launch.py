import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

roomba_launch_file_dir = os.path.join(get_package_share_directory('roomba_600_driver'), 'launch')
darknet_launch_file_dir = os.path.join(get_package_share_directory('darknet_ros'), 'launch')
test_launch_file_dir = os.path.join(get_package_share_directory('test_pkg'), 'launch')

def generate_launch_description():
    return launch.LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([nav2_launch_file_dir, '/roomba_600_driver.launch.py']),
        ),
        Node(
            package='usb_camera_driver', node_executable='usb_camera_driver_node', output='screen'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([darknet_launch_file_dir, '/darknet_ros.launch.py']),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([test_launch_file_dir, '/melody.launch.py']),
        ),
    ])