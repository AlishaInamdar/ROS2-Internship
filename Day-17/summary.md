# Day 17 — ROS 2 Launch Files

## Objective

Understand ROS 2 Launch Files and learn how to start and configure multiple ROS 2 nodes using a single command.

## Work Completed

- Studied ROS 2 Launch Files and their architecture.
- Created a Python ROS 2 package named `day17_launch_package`.
- Created a publisher node.
- Created a subscriber node.
- Created a Python launch file.
- Configured the launch file to start both nodes.
- Built the ROS 2 workspace successfully.
- Verified both executables using ROS 2 commands.
- Started both nodes using a single `ros2 launch` command.
- Verified communication through `/launch_demo_topic`.
- Used `ros2 node list` to verify running nodes.
- Used `ros2 topic list` to verify the topic.
- Used `ros2 topic echo` to observe published messages.
- Studied a common executable-name mismatch error and its solution.

## Launch Command

```bash
ros2 launch day17_launch_package launch_demo.py
