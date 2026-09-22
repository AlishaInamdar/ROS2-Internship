# Day 13 — ROS 2 Services

## Objective

Understand and implement **Services in ROS 2** using Python.

The task demonstrates request-response communication between a ROS 2 Service Client and Service Server.

---

## Technologies Used

- Ubuntu 24.04
- ROS 2 Jazzy
- Python
- `rclpy`
- `example_interfaces`
- `ament_python`
- WSL2

---

## Project Structure

```text
Day-13/
├── ros2_ws/
│   └── src/
│       └── day13_services_package/
│           ├── day13_services_package/
│           │   ├── __init__.py
│           │   ├── service_server.py
│           │   └── service_client.py
│           ├── resource/
│           │   └── day13_services_package
│           ├── test/
│           ├── package.xml
│           ├── setup.py
│           └── setup.cfg
│
├── screenshots/
├── concepts.md
├── commands.md
└── summary.md

Service Architecture
             Request
Client ───────────────────► Service Server
       /add_two_ints

             Response
Client ◄─────────────────── Service Server
              30

The client sends two integers to the /add_two_ints service.

The server calculates their sum and returns the result.

Service Interface

The project uses the predefined ROS 2 service:

example_interfaces/srv/AddTwoInts

Conceptually:

Request:
int64 a
int64 b
---
Response:
int64 sum
Python Service Server

The service server:

Creates the /add_two_ints service.
Waits for requests.
Executes the service callback.
Adds the two input values.
Returns the result.

Example:

Request: 10 + 20
Response: 30
Python Service Client

The service client:

Creates a client for /add_two_ints.
Waits for the service to become available.
Creates a request.
Sends the request asynchronously.
Waits for the response.
Displays the result.
Verification

The package was successfully built using:

colcon build

The service was verified using:

ros2 service list

and:

ros2 service type /add_two_ints

The service type was:

example_interfaces/srv/AddTwoInts

The Python client was tested using:

ros2 run day13_services_package service_client 10 20

Result:

Result: 10 + 20 = 30

The server confirmed that it received the request:

Request received: 10 + 20 = 30
