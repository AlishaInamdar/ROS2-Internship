# Day 12 – ROS 2 C++ Package

## Objective

To understand the structure and working of a ROS 2 C++ package and create a simple Publisher and Subscriber using C++.

## Overview

ROS 2 supports C++ for developing robotic applications. C++ packages generally use the `ament_cmake` build system and the `rclcpp` client library.

In this task, I created a package named `day12_cpp_package` containing:

- C++ Publisher node
- C++ Subscriber node
- `package.xml`
- `CMakeLists.txt`

The Publisher and Subscriber communicate using the `/cpp_topic` topic.

## Package Structure

```text
Day-12/
└── ros2_ws/
    └── src/
        └── day12_cpp_package/
            ├── CMakeLists.txt
            ├── package.xml
            ├── include/
            └── src/
                ├── publisher.cpp
                └── subscriber.cpp
