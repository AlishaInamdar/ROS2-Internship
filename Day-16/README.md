# Day 16 — ROS 2 Parameters

## Overview

Day 16 focuses on understanding and using **ROS 2 Parameters** with Python.

Parameters provide configuration values associated with a ROS 2 node. They allow node behavior and configuration to be changed at runtime without modifying the source code.

This task was completed using simulation and terminal-based ROS 2 tools.

---

## Objective

The objectives of Day 16 were:

- Understand ROS 2 Parameters.
- Learn the architecture and purpose of parameters.
- Create a Python ROS 2 node using parameters.
- Use ROS 2 parameter commands.
- Change parameter values at runtime.
- Understand parameter types.
- Debug a parameter type error.
- Capture implementation and testing evidence.

---

## Technologies Used

- Ubuntu 24.04
- ROS 2 Jazzy
- Python 3
- `rclpy`
- `colcon`
- WSL2
- Git and GitHub

---

## Package Information

Package name:

```text
day16_parameters_package


PROJECT STRUCTURE:

Day-16/
├── README.md
├── concepts.md
├── commands.md
├── summary.md
├── error_solution.md
├── screenshots/
│   ├── Successful_build.png
│   ├── Parameter_node.png
│   ├── Parameter_verification.png
│   ├── Parameter_changes.png
│   └── error_and_solution.png
└── ros2_ws/
    └── src/
        └── day16_parameters_package/
            ├── package.xml
            ├── setup.py
            ├── setup.cfg
            ├── resource/
            └── day16_parameters_package/
                ├── __init__.py
                └── parameter_demo.py


Parameters Used

The node declares three parameters:

self.declare_parameter('robot_name', 'ros_bot')
self.declare_parameter('speed', 1.5)
self.declare_parameter('enabled', True)

Their types are:

Parameter	Type	Default Value
robot_name	String	ros_bot
speed	Double	1.5
enabled	Boolean	True
Python Implementation

The node uses rclpy and the ROS 2 Node class.

The important parameter operations are:

Declare
self.declare_parameter('speed', 1.5)
Read
self.get_parameter('speed').value

The node prints the current parameter values when it starts.

Building the Package

The package was built using:

cd ~/ROS2-Internship/Day-16/ros2_ws
colcon build

The build completed successfully:

Summary: 1 package finished

The executable was verified using:

ros2 pkg executables day16_parameters_package

Result:

day16_parameters_package parameter_demo
Running the Node

The node was started using:

ros2 run day16_parameters_package parameter_demo

Initial output:

Robot Name: ros_bot
Speed: 1.5
Enabled: True
Inspecting Parameters

The parameters were listed using:

ros2 param list /parameter_demo_node

The parameter values were read using:

ros2 param get /parameter_demo_node robot_name
ros2 param get /parameter_demo_node speed
ros2 param get /parameter_demo_node enabled

Initial values were:

robot_name = ros_bot
speed = 1.5
enabled = True
Changing Parameters at Runtime

Parameters were successfully changed while the node was running.

Commands used:

ros2 param set /parameter_demo_node speed 3.0
ros2 param set /parameter_demo_node robot_name "fast_bot"
ros2 param set /parameter_demo_node enabled false

The updated values were verified as:

speed = 3.0
robot_name = fast_bot
enabled = False

This demonstrated that parameters can be changed without modifying or rebuilding the source code.

Error Encountered

A real parameter type error was encountered during testing.

Command:

ros2 param set /parameter_demo_node speed hello

Error:

Setting parameter failed: Wrong parameter type,
expected 'Type.DOUBLE' got 'Type.STRING'
Cause

The speed parameter was declared using:

self.declare_parameter('speed', 1.5)

Therefore, ROS 2 treated it as a DOUBLE parameter.

The value hello is a STRING, so ROS 2 rejected the update.

Solution

A numeric value was provided:

ros2 param set /parameter_demo_node speed 2.5

The update succeeded.

Verification:

ros2 param get /parameter_demo_node speed

Result:

Double value is: 2.5
Key Concepts Learned
ROS 2 Parameters are configuration values associated with nodes.
Parameters can be declared in Python using declare_parameter().
Parameter values can be read using get_parameter().
Parameters can be inspected using ros2 param.
Parameters can be changed at runtime.
ROS 2 Parameters are strongly typed.
Incorrect parameter types are rejected.
Parameters separate configuration from program logic.
Parameters vs Other ROS 2 Communication Mechanisms
Mechanism	Purpose
Parameter	Node configuration
Topic	Continuous data exchange
Service	Request-response communication
Action	Long-running goal with feedback and result
Real-World Applications

ROS 2 Parameters can be used for:

Robot speed configuration
Sensor settings
Camera configuration
Navigation settings
Controller parameters
Safety thresholds
Feature enable/disable settings
Simulation configuration
Screenshots

The screenshots/ directory contains evidence of:

Successful package build.
Parameter node execution.
Parameter listing and value verification.
Runtime parameter changes.
Real parameter type error and its solution.
Final Result

Day 16 was completed successfully.

The Python ROS 2 parameter node was created, built, executed, and tested. Parameters were inspected and changed at runtime, and a real parameter type error was identified and fixed.

The main takeaway is that ROS 2 Parameters provide strongly typed runtime configuration for nodes without requiring source-code changes or rebuilding the package.
