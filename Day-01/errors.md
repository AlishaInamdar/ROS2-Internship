# Day 1 Error Log

## Error 1

**Problem**
source install/setup.bash : No such file or directory

### Reason

Workspace had not been built.

### Solution
colcon build
source install/setup.bash
---

## Error 2

**Problem**
colcon: command not found


### Reason

colcon package was missing.

### Solution
sudo apt install colcon
---

## Error 3

**Problem**

gazebo: command not found


### Reason

Gazebo is not installed with ROS2 Jazzy Desktop.

### Solution

Install Gazebo separately when required.

