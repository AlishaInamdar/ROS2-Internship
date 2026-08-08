# Day 7 - ROS 2 Messages

## Objective

Understand ROS 2 Messages, their structure, message types, and how messages are exchanged between ROS 2 nodes through topics.

## Activities Completed

- Explored available ROS 2 message interfaces.
- Inspected the structure of `std_msgs/msg/String`.
- Inspected the structure of `geometry_msgs/msg/Twist`.
- Found topics using a particular message type.
- Checked the message type of a ROS 2 topic.
- Published a String message using the ROS 2 CLI.
- Observed published messages using `ros2 topic echo`.
- Created a Python example to inspect a ROS 2 message interface.

## Python Example

`python_examples/message_info.py`

The Python program uses the ROS 2 CLI to display the structure of `std_msgs/msg/String`.

## Screenshots

The screenshots document the message interface listing, message structures, topic type, message publishing, message echo, and Python example.

## Key Learning

ROS 2 Messages define the structure of data exchanged between nodes. Topics provide the communication channel through which these messages are transmitted.

## Important Observation

The interface output indicated that `std_msgs/msg/String` is deprecated for new development and recommends using semantically meaningful message definitions or the equivalent interface in `example_msgs`.
