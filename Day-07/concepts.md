# ROS 2 Messages - Concepts

## What is a ROS 2 Message?

A ROS 2 Message is a structured data format used by nodes to exchange information through topics.

A topic acts as the communication channel, while the message defines the type and structure of the data being transmitted.

## Message Communication

The basic communication flow is:

Publisher Node → Topic → Subscriber Node

The publisher sends messages to a topic and the subscriber receives messages from that topic.

## Message Types

Some commonly used ROS 2 message types include:

- `std_msgs/msg/String` - Text data
- `geometry_msgs/msg/Twist` - Linear and angular velocity
- `sensor_msgs/msg/Image` - Camera image data
- `sensor_msgs/msg/LaserScan` - LiDAR scan data
- `nav_msgs/msg/Odometry` - Robot odometry information

## Message Structure

The command:

`ros2 interface show std_msgs/msg/String`

shows that the message contains:

`string data`

This means the message has a field named `data` that stores a string.

## Important Observation

The ROS 2 interface output indicates that `std_msgs/msg/String` is deprecated for new development and recommends using semantically meaningful message definitions or the equivalent interface in `example_msgs`.

## Industry Relevance

Messages are fundamental to ROS 2 communication. Real robotic systems use different message types to transfer sensor data, robot position, velocity, camera images, LiDAR information, and other data between nodes.
