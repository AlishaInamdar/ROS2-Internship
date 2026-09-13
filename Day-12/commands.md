# Day 12 – ROS 2 C++ Package Commands

## 1. Source ROS 2

```bash
source /opt/ros/jazzy/setup.bash

2. Create Workspace
cd ~/ROS2-Internship/Day-12
mkdir -p ros2_ws/src
cd ros2_ws/src

3. Create C++ Package
ros2 pkg create --build-type ament_cmake day12_cpp_package

4. Go to Package Directory
cd ~/ROS2-Internship/Day-12/ros2_ws/src/day12_cpp_package

5. Check Package Structure
find . -maxdepth 3 -type f | sort

6. Build the Package
cd ~/ROS2-Internship/Day-12/ros2_ws
colcon build

7. Source the Workspace
source install/setup.bash

8. Check Package
ros2 pkg list | grep day12_cpp_package

9. Check Package Executables
ros2 pkg executables day12_cpp_package

Expected output:

day12_cpp_package publisher
day12_cpp_package subscriber


10. Run Publisher

In one terminal:

source /opt/ros/jazzy/setup.bash
cd ~/ROS2-Internship/Day-12/ros2_ws
source install/setup.bash
ros2 run day12_cpp_package publisher


11. Run Subscriber

In another terminal:

source /opt/ros/jazzy/setup.bash
cd ~/ROS2-Internship/Day-12/ros2_ws
source install/setup.bash
ros2 run day12_cpp_package subscriber


12. Check Topic Information
ros2 topic info /cpp_topic

Expected result:

Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1


13. Display Topic Messages
ros2 topic echo /cpp_topic


14. Stop a Running Node

Press:

Ctrl + C

15. Rebuild After Code Changes
cd ~/ROS2-Internship/Day-12/ros2_ws
colcon build
source install/setup.bash

16. Useful Package Commands

List all ROS 2 packages:

ros2 pkg list

Find information about a package:

ros2 pkg prefix day12_cpp_package

List available topics:

ros2 topic list

Check topic type:

ros2 topic type /cpp_topic

Check active nodes:

ros2 node list
