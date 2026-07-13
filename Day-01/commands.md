# Important Commands Used

| Command | Purpose |
|----------|---------|
| sudo apt update | Update package list |
| sudo apt install ros-jazzy-desktop | Install ROS2 Jazzy |
| source /opt/ros/jazzy/setup.bash | Load ROS2 environment |
| ros2 pkg list | List installed ROS2 packages |
| ros2 run demo_nodes_cpp talker | Start publisher node |
| ros2 run demo_nodes_cpp listener | Start subscriber node |
| mkdir -p ~/ros2_ws/src | Create workspace |
| colcon build | Build workspace |
| source install/setup.bash | Source workspace |
| ros2 pkg create --build-type ament_python my_first_package | Create Python package |
| ros2 run my_first_package hello_node | Execute custom node |
| rviz2 | Launch RViz2 |
