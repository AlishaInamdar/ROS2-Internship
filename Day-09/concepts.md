# Day 9: ROS 2 Subscriber

## 1. What is a Subscriber?

A Subscriber is a ROS 2 communication entity that receives messages from a specific topic.

A Subscriber does not directly communicate with a Publisher. Instead, messages are transferred through a **Topic**.

```text
Publisher → Topic → Subscriber
```

For example, in today's practical:

```text
Python Publisher
      ↓
   /my_topic
      ↓
Python Subscriber
```

---

## 2. How a Subscriber Works

A Subscriber is created with:

```python
self.create_subscription(
    String,
    'my_topic',
    self.listener_callback,
    10
)
```

This tells ROS 2 to:

* Listen to `/my_topic`
* Expect `std_msgs/msg/String` messages
* Call `listener_callback()` whenever a message is received
* Maintain a queue depth of 10

---

## 3. Callback

A callback is a function that ROS 2 automatically executes when a subscribed message arrives.

Example:

```python
def listener_callback(self, msg):
    self.get_logger().info(f'Received: {msg.data}')
```

Here, `msg` contains the received ROS 2 message and `msg.data` contains the actual String data.

The callback is important because it allows the Subscriber to process incoming data without continuously checking the topic manually.

---

## 4. Publisher and Subscriber Relationship

A Publisher sends messages while a Subscriber receives them.

```text
             std_msgs/msg/String
                    ↓
Publisher → /my_topic → Subscriber
                    ↓
              Callback
```

Multiple Subscribers can receive messages from the same topic, and a topic can have multiple Publishers.

---

## 5. Python ROS 2 Subscriber

The Python Subscriber was created using `rclpy`.

Important components used were:

* `rclpy` — Python client library for ROS 2
* `Node` — base class for creating a ROS 2 node
* `create_subscription()` — creates the Subscriber
* `listener_callback()` — processes received messages
* `rclpy.spin()` — keeps the node running and allows callbacks to execute
* `rclpy.shutdown()` — shuts down ROS 2 cleanly

---

## 6. Practical Understanding

During the practical, a Python Publisher from Day 8 published String messages on `/my_topic`.

The Day 9 Python Subscriber received those messages and displayed them in the terminal.

Example:

```text
Publisher:
Hello from Python Publisher: 250

Subscriber:
Received: Hello from Python Publisher: 250
```

This demonstrated the complete ROS 2 communication flow:

```text
Node → Publisher → Topic → Subscriber → Callback
```

## Key Takeaway

The main concept learned today was that ROS 2 uses topics for asynchronous communication between nodes. A Subscriber registers a callback, and ROS 2 automatically calls that callback whenever a matching message is received.
