from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    publisher_node = Node(
        package='day17_launch_package',
        executable='publisher_node',
        name='publisher_node',
        output='screen'
    )

    subscriber_node = Node(
        package='day17_launch_package',
        executable='subscriber_node',
        name='subscriber_node',
        output='screen'
    )

    return LaunchDescription([
        publisher_node,
        subscriber_node
    ])
