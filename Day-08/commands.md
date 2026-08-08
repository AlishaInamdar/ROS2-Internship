# ROS 2 Publisher - Commands

## 1. Source ROS 2

```bash
source /opt/ros/jazzy/setup.bash
```

Loads the ROS 2 Jazzy environment into the current terminal.

## 2. Run the Standard Publisher

```bash
ros2 run demo_nodes_cpp talker
```

Starts the standard ROS 2 talker node, which publishes messages to `/chatter`.

## 3. List Running Nodes

```bash
ros2 node list
```

Displays all currently running ROS 2 nodes.

## 4. Inspect the Publisher Node

```bash
ros2 node info /talker
```

Displays information about the `/talker` node, including its publishers, subscribers, services, and actions.

## 5. List Topics

```bash
ros2 topic list
```

Displays all currently available ROS 2 topics.

## 6. Check Topic Information

```bash
ros2 topic info /chatter
```

Displays the message type and the number of publishers and subscribers connected to `/chatter`.

## 7. Check Topic Type

```bash
ros2 topic type /chatter
```

Displays the message type used by `/chatter`.

Expected output:

std_msgs/msg/String

## 8. Display Published Messages

```bash
ros2 topic echo /chatter
```

Displays messages currently being published on `/chatter`.

## 9. Run the Custom Python Publisher

```bash
cd ~/ROS2-Internship/Day-08/python_examples
source /opt/ros/jazzy/setup.bash
python3 simple_publisher.py
```

Runs the custom Python Publisher created during the practical.

The Publisher sends String messages to `/my_topic`.

## 10. List Nodes After Starting the Python Publisher

```bash
ros2 node list
```

The custom node should appear as:

/simple_publisher

## 11. List Topics

```bash
ros2 topic list
```

The custom topic should appear as:

/my_topic

## 12. Check Custom Topic Information

```bash
ros2 topic info /my_topic
```

Displays the message type and publisher/subscriber count for `/my_topic`.

Expected message type:

std_msgs/msg/String

## 13. Check Custom Topic Type

```bash
ros2 topic type /my_topic
```

Expected output:

std_msgs/msg/String

## 14. Observe Messages from the Python Publisher

```bash
ros2 topic echo /my_topic
```

Displays the messages being published by the custom Python Publisher.

Example:

```text
data: 'Hello from Python Publisher: 0'
---
data: 'Hello from Python Publisher: 1'
---
data: 'Hello from Python Publisher: 2'
---
```

## 15. Stop a Running Node

Press:

Ctrl + C

This stops the currently running ROS 2 node or Python program.

## Summary

These commands were used to start, inspect, verify, and monitor a ROS 2 Publisher and its topic.
