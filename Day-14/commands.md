# Day 14 - ROS 2 Client Commands

## Navigate to Workspace

```bash
cd ~/ROS2-Internship/Day-14/ros2_ws
Build Package
colcon build
Source ROS 2
source /opt/ros/jazzy/setup.bash
Source Day 14 Workspace
source ~/ROS2-Internship/Day-14/ros2_ws/install/setup.bash
Verify Executable
ros2 pkg executables day14_clients_package
Start Service Server
source ~/ROS2-Internship/Day-13/ros2_ws/install/setup.bash
ros2 run day13_services_package service_server
Run Day 14 Client
ros2 run day14_clients_package service_client
Check Available Services
ros2 service list
Check Service Type
ros2 service type /add_two_ints
Check Service Information
ros2 service info /add_two_ints
Main Client Functions
create_client()
wait_for_service()
call_async()
spin_until_future_complete()
