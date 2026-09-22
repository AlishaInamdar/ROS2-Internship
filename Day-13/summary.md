# Day 13 — Summary

## Topic

ROS 2 Services

## Summary

Today I learned about **Services in ROS 2** and the request-response communication model.

I created a ROS 2 Python package using `ament_python` and implemented a Service Server and Service Client using `rclpy`.

The project uses the predefined `example_interfaces/srv/AddTwoInts` service. The client sends two integers to the `/add_two_ints` service, and the server calculates and returns their sum.

For testing, the client sent `10` and `20`, and the server successfully returned `30`.

## Practical Work Completed

- Created a ROS 2 Python package for Services.
- Implemented a Python Service Server.
- Implemented a Python Service Client.
- Used the `AddTwoInts` service interface.
- Built the package successfully using `colcon`.
- Verified the `/add_two_ints` service using ROS 2 CLI commands.
- Tested client-server communication successfully.
- Captured screenshots as evidence.

## Result

```text
Request:
10 + 20

Response:
30
