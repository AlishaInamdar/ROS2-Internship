# Day 11 – ROS 2 Python Package Commands

## 1. Create a ROS 2 Python Package

```bash
ros2 pkg create --build-type ament_python day11_python_package

2. Build the Workspace
cd ~/ROS2-Internship/Day-11/ros2_ws
colcon build

Builds the ROS 2 packages present in the workspace.

Successful output:

Starting >>> day11_python_package
Finished <<< day11_python_package
Summary: 1 package finished
3. Source the ROS 2 Environment
source /opt/ros/jazzy/setup.bash

Loads the ROS 2 Jazzy environment into the current terminal.

4. Source the Workspace
source install/setup.bash

Makes the packages and executables built in the current workspace available to the terminal.

5. List ROS 2 Packages
ros2 pkg list

Displays the ROS 2 packages available in the current environment.

To find our package:

ros2 pkg list | grep day11_python_package

Output:

day11_python_package
6. Check Package Executables
ros2 pkg executables day11_python_package

Displays the executables registered inside the package.

Output:

day11_python_package publisher
day11_python_package subscriber
7. Run the Publisher
ros2 run day11_python_package publisher

Runs the publisher executable from the package.

The publisher sends String messages to /package_topic.

8. Run the Subscriber
ros2 run day11_python_package subscriber

Runs the subscriber executable.

The subscriber receives messages from /package_topic.

9. Check Topic Information
ros2 topic info /package_topic

Displays information about the topic.

Output:

Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1

This confirms that one publisher and one subscriber are connected.

10. Display Topic Messages
ros2 topic echo /package_topic

Displays the messages being published on the topic.

Example:

data: 'Hello from Day 11 Package: 273'
---
data: 'Hello from Day 11 Package: 274'
---

This command is useful for observing and debugging topic communication.

11. View Package Structure
cd ~/ROS2-Internship/Day-11/ros2_ws/src/day11_python_package
find . -maxdepth 3 -type f | sort

Displays the files present in the ROS 2 Python package.
