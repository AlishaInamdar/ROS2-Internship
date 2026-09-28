# ROS 2 Launch Files — Concepts

## 1. What is a Launch File?

A ROS 2 launch file is used to start and configure multiple ROS 2 nodes and processes using a single command.

Instead of opening separate terminals and starting each node manually, a launch file can start the complete system together.

Example:

```bash
ros2 launch day17_launch_package launch_demo.py

2. Why Launch Files are Used

Launch files are useful because they:

Start multiple nodes together.
Reduce the number of manual commands.
Configure nodes in one place.
Support parameters and remappings.
Make large robot applications easier to manage.
Provide a repeatable way to start a ROS 2 system.
3. ROS 2 Launch Architecture

Basic architecture:

Launch File
↓
ROS 2 Launch System
↓
Launch Actions
↓
ROS 2 Nodes
↓
Topics / Services / Actions

A launch file describes what processes should be started and how they should be configured.

4. Python Launch Files

ROS 2 supports Python launch files.

Common imports are:

from launch import LaunchDescription
from launch_ros.actions import Node

A node is created using:

Node(
    package='package_name',
    executable='executable_name',
    name='node_name',
    output='screen'
)

The nodes are returned using:

return LaunchDescription([
    node1,
    node2
])
5. Important Launch File Components
LaunchDescription

Represents the collection of actions that the launch system should execute.

Node

Used to start a ROS 2 node.

package

Specifies the ROS 2 package containing the executable.

executable

Specifies which executable should be started.

name

Specifies the node name.

output

Controls where node output is displayed.

6. Day 17 Example

Our launch file starts two nodes:

publisher_node
subscriber_node

The publisher sends messages through:

/launch_demo_topic

The subscriber receives those messages.

Architecture:

publisher_node
↓
/launch_demo_topic
↓
subscriber_node

Both nodes are started using:

ros2 launch day17_launch_package launch_demo.py
7. Launch File vs Manual Execution
Manual execution

Each node must be started separately:

ros2 run day17_launch_package publisher_node
ros2 run day17_launch_package subscriber_node
Launch file

Both nodes can be started using:

ros2 launch day17_launch_package launch_demo.py

Therefore, launch files make multi-node systems easier to start and manage.
