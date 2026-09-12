# Day 11 – Summary

Today I learned how to create and use a Python package in ROS 2. I created an `ament_python` package named `day11_python_package` and configured it using `package.xml` and `setup.py`.

I created Publisher and Subscriber nodes that communicate through the `/package_topic` topic using `std_msgs/msg/String`. I built the package using `colcon build`, sourced the workspace, and ran both nodes successfully.

I verified the package executables and confirmed that the topic had one publisher and one subscriber. I also used `ros2 topic echo` to observe the messages being transmitted.

Overall, I learned how ROS 2 Python packages organize nodes and how Python nodes are built, installed, executed, and connected through topics.
