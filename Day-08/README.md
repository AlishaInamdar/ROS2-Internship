# Day 8: ROS 2 Publisher

## Objective

The objective of Day 8 was to understand ROS 2 Publishers, their role in ROS 2 communication, and how a Publisher sends messages through a topic.

All practical activities were performed using simulation and software-based ROS 2 tools.

## Topics Covered

* Understanding ROS 2 Publishers
* Publisher and Topic relationship
* ROS 2 nodes and publishers
* Message types
* Publishing messages using Python
* Inspecting nodes using ROS 2 CLI
* Inspecting topics using ROS 2 CLI
* Monitoring published messages
* Identifying and fixing a Publisher error

## Environment

* Operating System: Ubuntu 24.04 LTS
* ROS 2 Distribution: Jazzy
* Programming Language: Python 3
* ROS 2 Python Library: `rclpy`
* Message Type: `std_msgs/msg/String`

## Practical Work

### 1. Standard ROS 2 Publisher

The standard ROS 2 `talker` node was executed using:

```bash
ros2 run demo_nodes_cpp talker
```

The node publishes String messages on the `/chatter` topic.

The node and topic were inspected using ROS 2 CLI commands.

### 2. Custom Python Publisher

A custom Python Publisher named `simple_publisher.py` was created.

The Publisher uses `rclpy` and `std_msgs/msg/String` to publish messages to the `/my_topic` topic.

Example messages:

```text
Hello from Python Publisher: 0
Hello from Python Publisher: 1
Hello from Python Publisher: 2
```

The Publisher was monitored using:

```bash
ros2 topic echo /my_topic
```

### 3. ROS 2 CLI Verification

The following commands were used to verify the Publisher:

```bash
ros2 node list
ros2 topic list
ros2 topic info /my_topic
ros2 topic type /my_topic
ros2 topic echo /my_topic
```

These commands helped verify the running node, available topic, message type, and published data.

### 4. Error Handling

A controlled error was introduced by changing the valid message import:

```python
from std_msgs.msg import String
```

to:

```python
from std_msgs.msg import Strings
```

The resulting import error was analyzed and corrected by restoring the valid message type.

## Key Learning

A ROS 2 Publisher is responsible for producing and sending messages to a topic. Subscribers can receive these messages from the same topic.

The practical demonstrated how Python can be used to create a ROS 2 Publisher and how ROS 2 CLI commands can be used to inspect and verify the communication.

## Deliverables

* Python Publisher example
* ROS 2 CLI command documentation
* Concepts documentation
* Error and solution documentation
* Screenshots of practical execution
* Day 8 summary

## Screenshots

The `screenshots` directory contains evidence of:

* Python Publisher output
* Publisher node information
* Topic information and message type
* Published topic data
* ROS 2 Publisher execution
* Error encountered during testing

## Conclusion

Day 8 provided practical experience with ROS 2 Publishers and topic-based communication. The exercise demonstrated how a Python node can publish structured ROS 2 messages and how the ROS 2 CLI can be used to monitor and troubleshoot the Publisher.
