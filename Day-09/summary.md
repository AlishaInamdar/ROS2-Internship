# Day 9 Summary

Today I learned how a ROS 2 Subscriber receives messages from a topic. I first practiced the standard `talker` and `listener` nodes and used ROS 2 CLI commands to inspect the nodes and topic communication.

I then created a Python Subscriber using `rclpy` and `create_subscription()`. The Subscriber received String messages from `/my_topic` and processed them using a callback function.

The main concept I understood today was the communication flow:

**Publisher → Topic → Subscriber → Callback**

This helped me understand how ROS 2 nodes communicate asynchronously and how Python can be used to implement ROS 2 Subscribers.
