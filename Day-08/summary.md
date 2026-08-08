# Day 8 Summary: ROS 2 Publisher

Today I learned how a Publisher works in ROS 2 and how it sends messages through a topic. I practiced using ROS 2 CLI commands to inspect nodes and topics and created a simple Python Publisher using `rclpy`.

My Python Publisher published String messages on `/my_topic`, which I verified using `ros2 topic echo`. I also introduced and fixed an incorrect message-type import to understand how small errors can affect a ROS 2 node.

Overall, this practice helped me understand the basic flow of **Node → Publisher → Topic → Message** in ROS 2.
