# Day 17 — ROS 2 Launch Files

## Overview

Day 17 focuses on understanding and using ROS 2 Launch Files.

A launch file allows multiple ROS 2 nodes and processes to be started and configured using a single command.

In this practical, a Python launch file was created to start a publisher node and a subscriber node together.

---

## Objective

- Understand ROS 2 Launch Files.
- Understand launch-file architecture.
- Create a Python launch file.
- Start multiple ROS 2 nodes using one command.
- Verify node and topic communication.
- Understand common launch-file errors.

---

## Technologies Used

- Ubuntu 24.04
- ROS 2 Jazzy
- Python
- rclpy
- ROS 2 Launch
- WSL2

---

## Package Information

Package name:

```text id="2z7kna"
day17_launch_package

Project Structure
Day-17/
├── README.md
├── concepts.md
├── commands.md
├── error_solution.md
├── summary.md
├── screenshots/
│   └── Day 17 screenshots
└── ros2_ws/
    └── src/
        └── day17_launch_package/
            ├── day17_launch_package/
            │   ├── __init__.py
            │   ├── publisher_node.py
            │   └── subscriber_node.py
            ├── launch/
            │   └── launch_demo.py
            ├── resource/
            ├── test/
            ├── package.xml
            ├── setup.py
            └── setup.cfg
How the System Works

The launch file starts two nodes:

             launch_demo.py
                    |
          +---------+---------+
          |                   |
          ↓                   ↓
   publisher_node       subscriber_node
          |                   ↑
          |                   |
          +-- /launch_demo_topic --+

The publisher sends messages through /launch_demo_topic.

The subscriber receives the messages from the same topic.

Launch File

The launch file uses:

from launch import LaunchDescription
from launch_ros.actions import Node

Each node is defined using the Node action.

Example:

Node(
    package='day17_launch_package',
    executable='publisher_node',
    name='publisher_node',
    output='screen'
)

Both nodes are returned using:

return LaunchDescription([
    publisher_node,
    subscriber_node
])
Build the Package
cd ~/ROS2-Internship/Day-17/ros2_ws

source /opt/ros/jazzy/setup.bash

colcon build

source install/setup.bash
Run the Launch File
ros2 launch day17_launch_package launch_demo.py

The command starts both nodes.

Example output:

[publisher_node-1] Published: Launch demo message 0
[subscriber_node-2] Received: Launch demo message 0

[publisher_node-1] Published: Launch demo message 1
[subscriber_node-2] Received: Launch demo message 1
Verification
Check Nodes
ros2 node list

Expected:

/publisher_node
/subscriber_node
Check Topics
ros2 topic list

Expected to include:

/launch_demo_topic
Observe Messages
ros2 topic echo /launch_demo_topic

Example:

data: Launch demo message 25
---
data: Launch demo message 26
---
data: Launch demo message 27
---

Important Concepts Learned
LaunchDescription

Represents the collection of actions that the launch system executes.

Node Action

Used to start a ROS 2 node from a launch file.

Package

Specifies the ROS 2 package containing the executable.

Executable

Specifies the executable that should be started.

Output

Controls where the node's output is displayed.

Launch Files vs Manual Node Execution

Without a launch file:

ros2 run day17_launch_package publisher_node
ros2 run day17_launch_package subscriber_node

With a launch file:

ros2 launch day17_launch_package launch_demo.py

The launch approach is more convenient for applications containing multiple nodes.

Real-World Applications

ROS 2 launch files are useful in:

Autonomous robots
Navigation systems
SLAM
Robot perception
Camera and LiDAR systems
Manipulator robots
Simulation environments
Multi-node AI and robotics applications
