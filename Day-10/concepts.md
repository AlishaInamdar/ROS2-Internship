# Day 10 – Publisher and Subscriber

## 1. Publisher and Subscriber

Publisher and Subscriber is a communication mechanism in ROS 2.

- **Publisher:** Sends messages to a topic.
- **Subscriber:** Receives messages from a topic.
- **Topic:** Communication channel between nodes.
- **Message:** Data transferred through the topic.

### Communication Flow

Publisher Node → Topic → Subscriber Node

In this practical:

- Publisher Node: `/publisher_node`
- Subscriber Node: `/subscriber_node`
- Topic: `/chat_topic`
- Message Type: `std_msgs/msg/String`

---

## 2. Publisher

A Publisher creates messages and sends them to a topic.

In Python, a publisher is created using:

`create_publisher()`

The publisher in this practical sends a message every 1 second.

Example:

`Hello from Publisher: 10`

---

## 3. Subscriber

A Subscriber listens to a topic and receives messages from the Publisher.

In Python, a subscriber is created using:

`create_subscription()`

When a message arrives, a callback function is executed.

Example:

`Received: Hello from Publisher: 10`

---

## 4. Callback Function

A callback is a function that runs automatically when a new message is received.

In our subscriber:

`listener_callback(self, msg)`

The received message is available through:

`msg.data`

---

## 5. Topic

A topic is a named communication channel used by ROS 2 nodes.

Our topic is:

`/chat_topic`

One or more publishers can publish to a topic and one or more subscribers can subscribe to it.

---

## 6. QoS Queue Depth

The value `10` in:

`create_publisher(String, 'chat_topic', 10)`

and

`create_subscription(String, 'chat_topic', callback, 10)`

represents the queue depth.

It determines how many messages can be stored temporarily when they cannot be processed immediately.

---

## 7. ROS 2 Python Functions Used

- `rclpy.init()` – Initializes ROS 2.
- `Node` – Base class for creating a ROS 2 node.
- `create_publisher()` – Creates a publisher.
- `create_subscription()` – Creates a subscriber.
- `create_timer()` – Executes a function periodically.
- `publish()` – Sends a message.
- `rclpy.spin()` – Keeps the node running and processes ROS 2 events.
- `destroy_node()` – Destroys the node.
- `rclpy.shutdown()` – Shuts down ROS 2.

---

## 8. Applications

Publisher-Subscriber communication is used for:

- Sensor data
- Robot movement commands
- Camera and LiDAR data
- Robot status information
- Autonomous navigation
- Communication between different ROS 2 nodes

---

## 9. Interview Point

Publisher and Subscriber communication in ROS 2 is asynchronous. The Publisher does not directly call the Subscriber. Instead, both communicate through a named topic using ROS 2's communication middleware.
