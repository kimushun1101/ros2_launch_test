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
teleop_launch_file_dir = os.path.join(get_package_share_directory('teleop_twist_joy'), 'launch')
cbf_launch_file_dir = os.path.join(get_package_share_directory('cbf_assist'), 'launch')

def generate_launch_description():
    return launch.LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([roomba_launch_file_dir, '/roomba_600_driver.launch.py']),
        ),
        Node(
            package='usb_camera_driver', node_executable='usb_camera_driver_node', output='screen'),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([darknet_launch_file_dir, '/darknet_ros.launch.py']),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([test_launch_file_dir, '/melody.launch.py']),
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([teleop_launch_file_dir, '/teleop-launch.py']),
            launch_arguments={
                'joy_dev': '/dev/input/js0'}.items(),
        ),
        # IncludeLaunchDescription(
        #     PythonLaunchDescriptionSource([cbf_launch_file_dir, '/controller_with_teleop_twist_joy_launch.py']),
        #     launch_arguments={
        #         'joy_dev': '/dev/input/js0'}.items(),
        # ),
    ])