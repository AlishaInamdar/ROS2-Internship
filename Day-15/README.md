# Day 15 — ROS 2 Actions

## Overview

Day 15 focused on understanding **ROS 2 Actions** and implementing Action communication using Python.

Actions are useful for long-running tasks because they support:

* Goal
* Feedback
* Final Result

A Fibonacci calculation was used as a simple simulation example.

---

## Objective

The objectives of Day 15 were:

* Understand ROS 2 Actions.
* Understand Action Server and Action Client.
* Understand Goal, Feedback, and Result.
* Implement an Action Server in Python.
* Implement an Action Client in Python.
* Use ROS 2 CLI commands to inspect and verify an Action.
* Debug an actual ROS 2 interface error.

---

## Technologies Used

* Ubuntu 24.04
* ROS 2 Jazzy
* Python 3
* `rclpy`
* `example_interfaces`
* WSL2
* Git/GitHub

---

## Package

Package name:

```text id="e6m4yt"
day15_actions_package
```

Package type:

```text id="5m0y2x"
ament_python
```

Dependencies:

```text id="9df3vy"
rclpy
example_interfaces
```

---

## Project Structure

```text id="l1h4w6"
Day-15/
├── README.md
├── concepts.md
├── commands.md
├── summary.md
├── screenshots/
│   ├── Successful_build.png
│   ├── action_verification.png
│   ├── Action_server.png
│   ├── Action_client.png
│   └── error_and_solution.png
│
└── ros2_ws/
    └── src/
        └── day15_actions_package/
            ├── package.xml
            ├── setup.py
            ├── resource/
            │   └── day15_actions_package
            └── day15_actions_package/
                ├── __init__.py
                ├── action_server.py
                └── action_client.py
```

---

## Action Architecture

```text
                Goal
Action Client -----------> Action Server
     ^                         |
     |                         |
     |      Feedback           |
     <-------------------------|
     |                         |
     |      Final Result       |
     <-------------------------|
```

The client sends a Fibonacci goal with:

```text id="yq1n2j"
order = 6
```

The server processes the goal and continuously publishes feedback.

---

## ROS 2 Action Interface

The project uses:

```text id="9mbw2g"
example_interfaces/action/Fibonacci
```

The actual ROS 2 Jazzy interface is:

```text id="4f9v8p"
# Goal
int32 order
---
# Result
int32[] sequence
---
# Feedback
int32[] sequence
```

---

## Testing

The Action was verified using:

```bash id="5fr2f8"
ros2 action list
```

Output:

```text id="p6qj34"
/fibonacci
```

Action information was checked using:

```bash id="5z8vha"
ros2 action info /fibonacci
```

The Action type was checked using:

```bash id="c1xq9n"
ros2 action type /fibonacci
```

Output:

```text id="x8r7cd"
example_interfaces/action/Fibonacci
```

---

## Successful Client Result

The Action Client successfully sent:

```text id="3y9m1p"
Sending Fibonacci goal: order=6
```

The goal was accepted and feedback was received:

```text id="f1x2v8"
Feedback received: [0, 1, 1]
Feedback received: [0, 1, 1, 2]
Feedback received: [0, 1, 1, 2, 3]
Feedback received: [0, 1, 1, 2, 3, 5]
Feedback received: [0, 1, 1, 2, 3, 5, 8]
```

Final result:

```text id="q8c3n5"
Final result: [0, 1, 1, 2, 3, 5, 8]
```

---

## Debugging

### Error

During the first test, the Action Server produced
