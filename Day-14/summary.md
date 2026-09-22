# Day 14 - Summary

## Topic

ROS 2 Clients

## Objective

To understand how a ROS 2 Python Client communicates with a Service Server using request-response communication.

## Practical Work

A Python client was created using `rclpy` and `example_interfaces/srv/AddTwoInts`.

The client connects to the `/add_two_ints` service and sends multiple requests asynchronously.

## Test Results

- 10 + 20 = 30
- 50 + 25 = 75
- 100 + 200 = 300

## Key Learning

I learned how to create a ROS 2 service client using `create_client()`, wait for a service using `wait_for_service()`, send requests using `call_async()`, and process asynchronous results using a Future.

## Result

The Day 14 Python client successfully communicated with the ROS 2 service server and received correct responses for multiple requests.
