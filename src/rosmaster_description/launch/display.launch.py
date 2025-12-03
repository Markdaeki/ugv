from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch_ros.parameter_descriptions import ParameterValue  # ★ 추가


def generate_launch_description():
    pkg_share = FindPackageShare('rosmaster_description').find('rosmaster_description')

    urdf_file = PathJoinSubstitution([
        pkg_share,
        'urdf',
        'ugv.urdf.xacro'
    ])

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': ParameterValue(          # ★ 여기
                Command(['xacro ', urdf_file]),           # ★ 공백 없이 ['xacro', urdf_file]
                value_type=str
            ),
        }]
    )

    return LaunchDescription([
        robot_state_publisher_node
    ])

