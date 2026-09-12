# Day 10 – Publisher and Subscriber

## Objective

To understand how a Publisher and Subscriber communicate with each other in ROS 2 using a topic and a message.

## Concepts Covered

- Publisher and Subscriber communication
- ROS 2 Nodes
- Topics
- Messages
- Callbacks
- Timers
- QoS queue depth
- Asynchronous communication
- Python ROS 2 using `rclpy`

## Practical

A Python Publisher and Subscriber were created.

### Publisher

- Node: `/publisher_node`
- Topic: `/chat_topic`
- Message Type: `std_msgs/msg/String`
- Publishes one message every second.

Example:

```text
Hello from Publisher: 171
