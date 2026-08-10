# Day 9: ROS 2 Subscriber - Commands

## 1. Source ROS 2 Jazzy

```bash
source /opt/ros/jazzy/setup.bash
```

Loads the ROS 2 Jazzy environment into the current terminal.

---

## 2. Run the Standard Publisher

```bash
ros2 run demo_nodes_cpp talker
```

Starts the standard ROS 2 talker node and publishes messages on `/chatter`.

---

## 3. Run the Standard Subscriber

```bash
ros2 run demo_nodes_cpp listener
```

Starts the standard ROS 2 listener node and receives messages from `/chatter`.

---

## 4. List Running Nodes

```bash
ros2 node list
```

Displays the currently running ROS 2 nodes.

Expected nodes:

```text
/listener
/talker
```

---

## 5. Inspect the Subscriber Node

```bash
ros2 node info /listener
```

Displays information about the `/listener` node, including its subscriptions, publishers, services, and actions.

The Subscriber should show:

```text
/chatter: std_msgs/msg/String
```

---

## 6. Check Topic Information

```bash
ros2 topic info /chatter
```

Displays the message type and the number of Publishers and Subscribers connected to `/chatter`.

---

## 7. Display Messages from a Topic

```bash
ros2 topic echo /chatter
```

Displays messages currently being published on `/chatter`.

---

# Python Subscriber

## 8. Navigate to the Python Example

```bash
cd ~/ROS2-Internship/Day-09/python_examples
```

---

## 9. Run the Python Subscriber

```bash
source /opt/ros/jazzy/setup.bash
python3 subscriber.py
```

Starts the custom Python Subscriber.

The Subscriber listens to `/my_topic` and processes incoming `std_msgs/msg/String` messages.

---

## 10. List Nodes

```bash
ros2 node list
```

The custom Subscriber should appear as:

```text
/simple_subscriber
```

---

## 11. Inspect the Python Subscriber

```bash
ros2 node info /simple_subscriber
```

Shows that the node is subscribed to:

```text
/my_topic: std_msgs/msg/String
```

---

## 12. Check Custom Topic Information

```bash
ros2 topic info /my_topic
```

Displays the message type and Publisher/Subscriber count for `/my_topic`.

Expected message type:

```text
std_msgs/msg/String
```

---

## 13. Check Topic Type

```bash
ros2 topic type /my_topic
```

Expected output:

```text
std_msgs/msg/String
```

---

## 14. Observe Messages

```bash
ros2 topic echo /my_topic
```

Displays the messages being published on `/my_topic`.

Example:

```text
data: 'Hello from Python Publisher: 244'
---
data: 'Hello from Python Publisher: 245'
---
```

---

## 15. Stop a Running Node

Press:

```text
Ctrl + C
```

This stops the currently running ROS 2 node or Python program.

---

## Summary

These commands were used to start, inspect, verify, and monitor ROS 2 Subscribers and their topics using both the standard ROS 2 nodes and a custom Python Subscriber.
