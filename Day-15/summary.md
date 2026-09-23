# Day 15 — ROS 2 Actions Summary

## Topic

ROS 2 Actions

## Objective

The objective of Day 15 was to understand ROS 2 Actions and implement a simple Action Server and Action Client using Python.

## Work Completed

* Created a ROS 2 Python package named `day15_actions_package`.
* Implemented a Fibonacci Action Server.
* Implemented a Fibonacci Action Client.
* Used `example_interfaces/action/Fibonacci`.
* Tested Action communication using Goal, Feedback, and Result.
* Verified the `/fibonacci` Action using ROS 2 CLI commands.
* Successfully built and executed the package.
* Captured screenshots of the build, Action verification, server, client, and debugging process.

## Practical Demonstration

The Action Client sent the following goal:

```text
order = 6
```

The server generated Fibonacci feedback:

```text
[0, 1, 1]
[0, 1, 1, 2]
[0, 1, 1, 2, 3]
[0, 1, 1, 2, 3, 5]
[0, 1, 1, 2, 3, 5, 8]
```

The final result was:

```text
[0, 1, 1, 2, 3, 5, 8]
```

## Error Encountered

During testing, the Action Server initially produced this error:

```text
AttributeError:
'Fibonacci_Feedback' object has no attribute 'partial_sequence'
```

The client also initially used the same incorrect field name.

## Cause

The code assumed that the Fibonacci Feedback message contained a field named `partial_sequence`.

However, the actual ROS 2 Jazzy interface is:

```text
# Feedback
int32[] sequence
```

This was verified using:

```bash
ros2 interface show example_interfaces/action/Fibonacci
```

## Solution

The incorrect field:

```python
partial_sequence
```

was changed to:

```python
sequence
```

For example:

```python
feedback_msg.sequence = [0, 1]
```

and:

```python
feedback = feedback_msg.feedback.sequence
```

After rebuilding the package and testing again, the Action Server and Client communicated successfully.

## What I Learned

* An Action is suitable for long-running tasks.
* Actions provide Goal, Feedback, and Result.
* `ActionServer` handles goals and performs the task.
* `ActionClient` sends goals and receives feedback/results.
* `send_goal_async()` sends a goal asynchronously.
* `publish_feedback()` sends progress updates.
* `get_result_async()` obtains the final result.
* `ros2 action list` can be used to discover available Actions.
* `ros2 action info` provides information about Action Clients and Servers.
* `ros2 interface show` is useful for inspecting the exact structure of ROS 2 interfaces.
* Checking the actual interface is important before assuming message field names.

## Final Status

Day 15 was successfully completed using simulation-only ROS 2 communication.

The Fibonacci Action Server and Action Client were successfully tested with:

**Goal → Feedback → Final Result**
