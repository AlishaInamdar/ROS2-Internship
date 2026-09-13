# Day 12 – Summary

Today I learned about C++ packages in ROS 2 and how they are structured and built using `ament_cmake`.

I created a package named `day12_cpp_package` and configured its dependencies using `package.xml` and `CMakeLists.txt`. I implemented a C++ Publisher and Subscriber using `rclcpp`.

The Publisher sends messages on the `/cpp_topic` topic using `std_msgs/msg/String`, and the Subscriber receives and displays those messages.

I successfully built the package using `colcon build`, ran both nodes, and verified the communication using ROS 2 topic commands.

Overall, this task helped me understand the basic structure, build process, and topic communication of C++ packages in ROS 2.
