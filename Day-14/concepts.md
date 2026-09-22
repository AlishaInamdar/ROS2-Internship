# Day 14 - ROS 2 Clients

## What is a ROS 2 Client?

A ROS 2 Client is a node that sends a request to a ROS 2 Service and receives a response from the Service Server.

## Client Communication

The communication follows a request-response pattern:

Client -> Request -> Service Server
Client <- Response <- Service Server

## Important Client Functions

### create_client()

Creates a ROS 2 service client.

```python
self.client = self.create_client(
    AddTwoInts,
    'add_two_ints'
)

wait_for_service()

Checks whether the required service is available.

self.client.wait_for_service(timeout_sec=1.0)
call_async()

Sends the request asynchronously and returns a Future.

future = self.client.call_async(request)
Future

A Future represents the result of an asynchronous operation that will become available later.

spin_until_future_complete()

Allows ROS 2 to process callbacks until the requested Future is completed.

rclpy.spin_until_future_complete(node, future)
Day 14 Example

The client sends three requests to the /add_two_ints service:

10 + 20 = 30
50 + 25 = 75
100 + 200 = 300

This demonstrates that one client can communicate with the same service multiple times.

Client vs Service Server
Client	Service Server
Sends requests	Receives requests
Receives responses	Creates responses
Uses create_client()	Uses create_service()
Uses call_async()	Uses a service callback
Waits for service availability	Provides the service
