# Day 13 — ROS 2 Services: Concepts

## 1. What is a ROS 2 Service?

A Service in ROS 2 is a communication mechanism based on the **request-response model**.

A Service consists of:

- **Service Server** — receives requests and sends responses.
- **Service Client** — sends requests and receives responses.

Example:

```text
Client
   |
   | Request
   v
Service Server
   |
   | Response
   v
Client

2. Service vs Topic
Topic	Service
Uses publish-subscribe communication	Uses request-response communication
Suitable for continuous data	Suitable for specific operations
Publisher does not directly wait for a response	Client receives a response
Example: sensor data	Example: add two numbers

A sensor continuously publishing temperature data is a good example of a Topic, while requesting a calculation from another node is a good example of a Service.

3. Service Interface

This project uses the predefined ROS 2 service:

example_interfaces/srv/AddTwoInts

Its structure is conceptually:

Request:
int64 a
int64 b
---
Response:
int64 sum

The --- separates the request fields from the response fields.

For example:

Request:
a = 10
b = 20

Response:
sum = 30
4. Python ROS 2 Library

This project uses:

rclpy

rclpy is the Python client library for ROS 2.

It provides Python APIs for creating nodes, services, clients, publishers, subscribers, timers, and other ROS 2 functionality.

The equivalent C++ library is:

rclcpp
5. Service Server

The service server creates the /add_two_ints service using:

self.create_service(
    AddTwoInts,
    'add_two_ints',
    self.add_two_ints_callback
)

The server waits for incoming requests.

When a request arrives, the callback is executed:

def add_two_ints_callback(self, request, response):
    response.sum = request.a + request.b
    return response

The callback calculates the sum and returns the response.

6. Service Client

The service client creates a client for:

/add_two_ints

It creates a request:

request = AddTwoInts.Request()
request.a = a
request.b = b

The request is sent using:

self.client.call_async(request)

The asynchronous call returns a Future, which represents the response that will become available later.

7. Future

A Future represents the result of an asynchronous operation.

The client waits for the service response using:

rclpy.spin_until_future_complete(node, future)

After the operation completes, the response can be accessed using:

future.result()
8. Service Availability

Before sending a request, the client checks whether the service is available:

self.client.wait_for_service(timeout_sec=1.0)

If the server is not available, the client waits until the service becomes available.

9. ROS 2 Service Commands

Useful commands include:

ros2 service list

Lists available services.

ros2 service type /add_two_ints

Displays the type of the service.

ros2 service info /add_two_ints

Displays information about the service.

A service can also be called directly from the terminal:

ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts "{a: 5, b: 7}"
10. Execution Flow

The complete communication flow in this task is:

Python Service Client
        |
        | Request: a=10, b=20
        v
   /add_two_ints
        |
        v
Python Service Server
        |
        | Calculate 10 + 20
        v
   Response: 30
        |
        v
Python Service Client
