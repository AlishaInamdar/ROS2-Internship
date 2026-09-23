# Day 15 — ROS 2 Actions Concepts

## 1. What is an Action in ROS 2?

An Action is a ROS 2 communication mechanism used for tasks that:

* Take some time to complete.
* Need continuous feedback while running.
* Produce a final result.

An Action has three main parts:

1. **Goal** — tells the server what task to perform.
2. **Feedback** — provides progress information while the task is running.
3. **Result** — provides the final output after the task finishes.

Example:

For a Fibonacci Action:

* Goal: calculate Fibonacci sequence up to a given order.
* Feedback: current Fibonacci sequence while calculating.
* Result: final Fibonacci sequence.

---

## 2. Action Server

The Action Server receives goals from Action Clients and performs the requested task.

In this project, the server is:

```text
fibonacci_action_server
```

The server uses:

```python
ActionServer(
    self,
    Fibonacci,
    'fibonacci',
    self.execute_callback
)
```

The `execute_callback()` function performs the Fibonacci calculation.

---

## 3. Action Client

The Action Client sends a goal to the Action Server and receives:

* Goal acceptance/rejection.
* Feedback.
* Final result.

The client uses:

```python
ActionClient(
    self,
    Fibonacci,
    'fibonacci'
)
```

A goal is sent using:

```python
send_goal_async()
```

---

## 4. Goal

The goal contains the input required by the Action Server.

For this project:

```text
int32 order
```

The client sends:

```python
goal_msg = Fibonacci.Goal()
goal_msg.order = 6
```

This asks the server to calculate the Fibonacci sequence for order 6.

---

## 5. Feedback

Feedback provides intermediate progress while the Action is executing.

The ROS 2 Jazzy Fibonacci Action interface defines:

```text
# Feedback
int32[] sequence
```

The server publishes feedback using:

```python
goal_handle.publish_feedback(feedback_msg)
```

The client receives it through:

```python
feedback_callback()
```

---

## 6. Result

The Result contains the final output after the Action completes.

The Fibonacci Action defines:

```text
# Result
int32[] sequence
```

The server creates the result using:

```python
result = Fibonacci.Result()
result.sequence = feedback_msg.sequence
```

The client receives the result after the goal completes.

---

## 7. Action Communication Flow

```text
Action Client
     |
     |  Goal
     v
Action Server
     |
     |  Goal Accepted
     v
Task Execution
     |
     |  Feedback
     v
Action Client
     |
     |  Feedback updates
     |
     v
Task Completed
     |
     |  Final Result
     v
Action Client
```

---

## 8. Important Python ROS 2 Functions

### ActionServer

Creates an Action Server.

```python
ActionServer(...)
```

### ActionClient

Creates an Action Client.

```python
ActionClient(...)
```

### send_goal_async()

Sends an Action goal asynchronously.

```python
self.action_client.send_goal_async(...)
```

### publish_feedback()

Publishes intermediate feedback from the server.

```python
goal_handle.publish_feedback(feedback_msg)
```

### get_result_async()

Requests the final result asynchronously.

```python
goal_handle.get_result_async()
```

### spin_until_future_complete()

Waits for an asynchronous operation to finish while allowing ROS 2 callbacks to execute.

```python
rclpy.spin_until_future_complete(
    self,
    future
)
```

---

## 9. Action vs Service vs Topic

| Feature             | Topic             | Service          | Action               |
| ------------------- | ----------------- | ---------------- | -------------------- |
| Communication       | Publish/Subscribe | Request/Response | Goal/Feedback/Result |
| Long-running task   | Not specifically  | Not suitable     | Suitable             |
| Feedback            | No                | No               | Yes                  |
| Final result        | No                | Yes              | Yes                  |
| Example             | Sensor data       | Add two numbers  | Navigation           |
| Communication style | Continuous        | One request      | Goal-based           |

---

## 10. Real-World Uses of Actions

Actions are commonly useful for tasks such as:

* Robot navigation
* Moving a robot arm
* Gripper operations
* Long-running calculations
* Autonomous robot movement
* Planning and execution tasks

---

## 11. Interview Point

A simple way to remember the difference is:

**Topic → continuous data**

**Service → quick request and response**

**Action → long-running task with feedback and final result**
