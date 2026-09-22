# Day 13 — ROS 2 Services: Commands

## 1. Navigate to the Day 13 Workspace

```bash
cd ~/ROS2-Internship/Day-13/ros2_ws
2. Build the Package
colcon build

Expected result:

Finished <<< day13_services_package
Summary: 1 package finished
3. Source the Workspace
source ~/ROS2-Internship/Day-13/ros2_ws/install/setup.bash
4. Verify Package Executables
ros2 pkg executables day13_services_package

Expected:

day13_services_package service_client
day13_services_package service_server
5. Start the Service Server
ros2 run day13_services_package service_server

Expected:

Add Two Ints Service Server is ready.

Keep this terminal running.

6. Check Available Services

Open another terminal and source ROS 2 and the workspace:

source /opt/ros/jazzy/setup.bash
source ~/ROS2-Internship/Day-13/ros2_ws/install/setup.bash

Then:

ros2 service list

The custom service should appear:

/add_two_ints
7. Check the Service Type
ros2 service type /add_two_ints

Expected:

example_interfaces/srv/AddTwoInts
8. Check Service Information
ros2 service info /add_two_ints

This provides information about the service type and connected nodes.

9. Run the Python Service Client
ros2 run day13_services_package service_client 10 20

Expected:

Result: 10 + 20 = 30

The service server should also display:

Request received: 10 + 20 = 30
10. Call the Service Directly from the Terminal
ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 5, b: 7}"

Expected response:

sum: 12
11. Stop the Service Server

When testing is complete, return to the server terminal and press:

Ctrl + C
12. Useful Package Commands

Check package information:

ros2 pkg list | grep day13_services_package

Check available executables:

ros2 pkg executables day13_services_package
13. Important Commands Summary
Command	Purpose
colcon build	Builds the ROS 2 workspace
source install/setup.bash	Sources the workspace
ros2 pkg executables	Lists package executables
ros2 run	Runs a ROS 2 executable
ros2 service list	Lists available services
ros2 service type	Shows a service type
ros2 service info	Shows service information
ros2 service call	Calls a service manually
