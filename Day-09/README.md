# Day 9: ROS 2 Subscriber

## Goal

Understand ROS 2 Subscribers and learn how nodes receive messages from topics using both ROS 2 CLI tools and Python.

## Topics Covered

* ROS 2 Subscriber
* Publisher-Subscriber communication
* Topics
* Message types
* Subscription callbacks
* `create_subscription()`
* `rclpy.spin()`
* Python ROS 2 nodes
* Basic Subscriber debugging and verification

## Practical Work

### 1. ROS 2 CLI Subscriber

Used the standard ROS 2 `talker` and `listener` nodes to understand:

```text
/talker → /chatter → /listener
```

Verified the communication using:

```bash
ros2 node list
ros2 node info /listener
ros2 topic info /chatter
ros2 topic echo /chatter
```

### 2. Python Subscriber

Created a custom Python Subscriber:

```text
Day-09/python_examples/subscriber.py
```

The Subscriber listens to `/my_topic` using:

```text
std_msgs/msg/String
```

and processes incoming messages using a callback function.

### 3. Verification

Verified the Python Subscriber using ROS 2 CLI commands and observed messages published by the Day 8 Python Publisher.

Communication flow:

```text
Python Publisher
       ↓
   /my_topic
       ↓
Python Subscriber
       ↓
listener_callback()
```

## Learning Outcome

Understood how ROS 2 Subscribers receive messages through topics and how Python callbacks are used to process incoming messages.

The practical also improved understanding of the relationship between Nodes, Publishers, Topics, Messages, and Subscribers.
