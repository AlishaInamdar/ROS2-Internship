# Day 14 - ROS 2 Clients

## Objective

To understand ROS 2 Clients and implement a Python client that communicates with a ROS 2 Service Server.

## Technologies

- Ubuntu 24.04
- ROS 2 Jazzy
- Python
- rclpy
- example_interfaces

## Package

`day14_clients_package`

## Project Structure

```text
Day-14/
├── README.md
├── concepts.md
├── commands.md
├── summary.md
├── screenshots/
│   ├── package_structure.png
│   ├── successful_build.png
│   ├── client_results.png
│   └── service_client_verification.png
└── ros2_ws/
    └── src/
        └── day14_clients_package/
            ├── day14_clients_package/
            │   ├── __init__.py
            │   └── service_client.py
            ├── package.xml
            ├── setup.py
            └── setup.cfg

Client Architecture
Python Client
     |
     | Request
     v
/add_two_ints Service
     |
     | Response
     v
Python Client
Implementation

The client uses:

create_client() to create the service client.
wait_for_service() to check service availability.
call_async() to send requests asynchronously.
Future objects to represent pending responses.
spin_until_future_complete() to wait for each response.
Test Results

The client successfully processed:

10 + 20 = 30
50 + 25 = 75
100 + 200 = 300
Learning Outcome

This exercise demonstrated the client side of ROS 2 Service communication and showed how one client can send multiple asynchronous service requests.
