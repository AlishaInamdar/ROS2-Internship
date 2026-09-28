# ROS 2 Parameters — Commands

## 1. Create the Workspace

```bash
mkdir -p ~/ROS2-Internship/Day-16/ros2_ws/src
cd ~/ROS2-Internship/Day-16/ros2_ws/src
2. Create the Package
ros2 pkg create --build-type ament_python day16_parameters_package --dependencies rclpy
3. Build the Package
cd ~/ROS2-Internship/Day-16/ros2_ws
colcon build

Expected result:

Summary: 1 package finished
4. Source the Workspace
source install/setup.bash
5. Check the Executable
ros2 pkg executables day16_parameters_package

Expected:

day16_parameters_package parameter_demo
6. Run the Parameter Node
ros2 run day16_parameters_package parameter_demo

The node displays:

Robot Name: ros_bot
Speed: 1.5
Enabled: True
7. List Node Parameters
ros2 param list /parameter_demo_node

This displays the parameters available for the node.

8. Get a Parameter

Get the robot name:

ros2 param get /parameter_demo_node robot_name

Get the speed:

ros2 param get /parameter_demo_node speed

Get the enabled state:

ros2 param get /parameter_demo_node enabled
9. Change a Parameter

Change speed:

ros2 param set /parameter_demo_node speed 3.0

Change robot name:

ros2 param set /parameter_demo_node robot_name "fast_bot"

Change enabled state:

ros2 param set /parameter_demo_node enabled false

Expected response:

Set parameter successful
10. Verify Changed Parameters
ros2 param get /parameter_demo_node speed
ros2 param get /parameter_demo_node robot_name
ros2 param get /parameter_demo_node enabled

The values should be:

speed      → 3.0
robot_name → fast_bot
enabled    → False
11. Error Testing

An incorrect parameter type was intentionally tested:

ros2 param set /parameter_demo_node speed hello

Result:

Setting parameter failed: Wrong parameter type,
expected 'Type.DOUBLE' got 'Type.STRING'
12. Fix the Error

The correct type for speed is DOUBLE.

Therefore, a numeric value was provided:

ros2 param set /parameter_demo_node speed 2.5

Expected:

Set parameter successful

Verify:

ros2 param get /parameter_demo_node speed

Expected:

Double value is: 2.5
13. Useful Parameter Commands

List parameters:

ros2 param list /node_name

Get a parameter:

ros2 param get /node_name parameter_name

Set a parameter:

ros2 param set /node_name parameter_name value

Describe a parameter:

ros2 param describe /node_name parameter_name

Dump node parameters:

ros2 param dump /node_name

Load parameters from a YAML file:

ros2 param load /node_name parameters.yaml
