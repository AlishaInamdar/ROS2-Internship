# Day 12 – ROS 2 C++ Package

## Objective

To understand how to create and use a C++ package in ROS 2 using the `ament_cmake` build system.

## Introduction

ROS 2 supports both Python and C++ for developing nodes. C++ is commonly used in robotics applications where performance and efficient resource usage are important.

In this task, I created a C++ package named `day12_cpp_package`. The package contains a Publisher node and a Subscriber node that communicate through a ROS 2 topic.

## ROS 2 C++ Package

A ROS 2 C++ package contains source code, dependency information, and build configuration required to create ROS 2 applications.

The main files and folders used in this package are:

- `package.xml` – Contains package information and dependencies.
- `CMakeLists.txt` – Contains instructions for building the C++ package.
- `src/` – Contains the C++ source files.
- `include/` – Used for C++ header files.

## Package Structure

```text
day12_cpp_package/
├── CMakeLists.txt
├── package.xml
├── include/
│   └── day12_cpp_package/
└── src/
    ├── publisher.cpp
    └── subscriber.cpp

ament_cmake

ament_cmake is the ROS 2 build system commonly used for C++ packages.

It is used to:

Find required dependencies.
Compile C++ source files.
Create executable nodes.
Install executables.
Integrate the package with the ROS 2 workspace.

The package was created using:

ros2 pkg create --build-type ament_cmake day12_cpp_package
package.xml

The package.xml file contains the metadata and dependencies of the ROS 2 package.

The important dependencies used in this package are:

ament_cmake
rclcpp
std_msgs
CMakeLists.txt

CMakeLists.txt contains the build instructions for the C++ package.

In this project, it is used to:

Find ROS 2 dependencies.
Compile publisher.cpp.
Compile subscriber.cpp.
Link the required ROS 2 libraries.
Install the publisher and subscriber executables.
rclcpp

rclcpp is the C++ client library for ROS 2.

It provides APIs for creating and working with ROS 2:

Nodes
Publishers
Subscribers
Timers
Services
Actions
Parameters

The C++ nodes in this task use rclcpp.

Publisher

The Publisher node creates a publisher for the /cpp_topic topic.

It uses a timer to publish a message every second.

Example output:

Published: Hello from Day 12 C++ Package: 0
Published: Hello from Day 12 C++ Package: 1
Published: Hello from Day 12 C++ Package: 2
Subscriber

The Subscriber node subscribes to the /cpp_topic topic.

Whenever a message is received, the subscriber callback function is executed.

Example:

Received: Hello from Day 12 C++ Package: 123
Topic Communication

The Publisher and Subscriber communicate using:

Topic: /cpp_topic
Message Type: std_msgs/msg/String

The communication flow is:

Publisher Node
      |
      | std_msgs/msg/String
      v
  /cpp_topic
      |
      v
Subscriber Node

The topic was verified using:

ros2 topic info /cpp_topic

The result showed:

Type: std_msgs/msg/String
Publisher count: 1
Subscription count: 1

This confirmed that the Publisher and Subscriber were communicating successfully.

Build Process

The package was built using:

colcon build

After a successful build, the workspace was sourced using:

source install/setup.bash

The package executables were verified using:

ros2 pkg executables day12_cpp_package

The following executables were available:

day12_cpp_package publisher
day12_cpp_package subscriber
Python and C++ in ROS 2

ROS 2 supports both Python and C++.

Python	C++
Uses rclpy	Uses rclcpp
Easier to learn and write	More performance-oriented
Good for rapid development	Good for performance-critical applications
Interpreted	Compiled

Both languages use the same basic ROS 2 concepts such as nodes, topics, publishers and subscribers.

Applications of C++ in ROS 2

C++ packages are commonly used in:

Autonomous robots
Industrial robotics
Navigation
Motion planning
Sensor processing
Computer vision
Performance-critical robotics applications
Key Learning

From this task, I learned:

How to create a ROS 2 C++ package.
How ament_cmake is used to build C++ packages.
The purpose of package.xml and CMakeLists.txt.
How to create Publisher and Subscriber nodes using rclcpp.
How C++ nodes communicate using ROS 2 topics.
How to build and run C++ packages using colcon.
How to verify ROS 2 topic communication using command-line tools.
Conclusion

In this task, I created and tested a ROS 2 C++ package using ament_cmake. I implemented Publisher and Subscriber nodes using rclcpp and verified their communication through the /cpp_topic topic. This helped me understand the structure, build process, and basic communication mechanism of C++ packages in ROS 2.
