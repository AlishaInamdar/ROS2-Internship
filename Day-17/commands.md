# ROS 2 Launch Files — Commands

## 1. Create Day 17 Workspace

```bash
mkdir -p ~/ROS2-Internship/Day-17/ros2_ws/src
cd ~/ROS2-Internship/Day-17/ros2_ws/src

2. Create Python Package
ros2 pkg create --build-type ament_python day17_launch_package --dependencies rclpy
3. Build Workspace
cd ~/ROS2-Internship/Day-17/ros2_ws
source /opt/ros/jazzy/setup.bash
colcon build
4. Source Workspace
source install/setup.bash
5. Check Package Executables
ros2 pkg executables day17_launch_package

Expected:

day17_launch_package publisher_node
day17_launch_package subscriber_node
6. Run Launch File
ros2 launch day17_launch_package launch_demo.py

This starts both the publisher and subscriber nodes.

7. Check Running Nodes
ros2 node list

Expected:

/publisher_node
/subscriber_node
8. Check Topics
ros2 topic list

Expected:

/launch_demo_topic

along with standard ROS 2 topics such as /parameter_events and /rosout.

9. Observe Topic Messages
ros2 topic echo /launch_demo_topic

Example:

data: Launch demo message 25
---
data: Launch demo message 26
---

Press Ctrl+C to stop the command.

10. Useful Launch Commands

Display launch-file information:

ros2 launch --help

List available packages:

ros2 pkg list

Check available executables:

ros2 pkg executables day17_launch_package
11. Possible Launch Error

If the executable name in the launch file is incorrect, the corresponding node may fail to start.

Check the registered executable names:

ros2 pkg executables day17_launch_package

Then verify the executable field in the launch file.
