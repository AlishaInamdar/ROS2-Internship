# ROS 2 Publisher - Concepts

## What is a Publisher?

A Publisher is a ROS 2 communication entity that sends messages to a topic. A node can contain one or more publishers.

The Publisher does not communicate directly with a Subscriber. Instead, messages are sent through a ROS 2 topic.

## Basic Communication Flow

Publisher Node
      |
      | Message
      v
    Topic
      |
      | Message
      v
Subscriber Node

## Publisher Architecture

In this practical, the Python node `simple_publisher` creates a publisher for the topic `/my_topic`.

The publisher uses the message type:

`std_msgs/msg/String`

The publisher periodically creates a String message and publishes it to `/my_topic`.

## Important Components

### Node
A process that performs a specific function in a ROS 2 system.

### Publisher
Sends messages to a topic.

### Topic
A named communication channel used to exchange messages.

### Message
Defines the structure and data type of information being exchanged.

### Timer
The Python example uses a timer to publish a message at regular intervals.

## Where Publishers Are Used

Publishers are commonly used in robotics for:

- Sending sensor data
- Publishing robot velocity commands
- Sending navigation information
- Publishing camera or LiDAR data
- Sending robot status information
- Communicating commands between ROS 2 nodes

## Practical Example

The Python Publisher created during this task publishes messages such as:

`Hello from Python Publisher: 0`

`Hello from Python Publisher: 1`

The messages are published once every second to `/my_topic`.

## Key Learning

A Publisher is responsible for producing and sending data, while a Subscriber receives that data. Topics provide the communication channel between them.O
