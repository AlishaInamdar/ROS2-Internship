# Day 15 — ROS 2 Actions: Error and Solution

## Error Encountered

While testing the Fibonacci Action Server, the following error occurred:

```text
AttributeError:
'Fibonacci_Feedback' object has no attribute 'partial_sequence'
```

The Action Client also produced the same error when trying to read the feedback.

---

## Cause

The Python code initially used:

```python
feedback_msg.partial_sequence
```

However, the actual ROS 2 Jazzy Fibonacci Action interface does not contain a field named `partial_sequence`.

The actual interface was checked using:

```bash
ros2 interface show example_interfaces/action/Fibonacci
```

It showed:

```text
# Goal
int32 order
---
# Result
int32[] sequence
---
# Feedback
int32[] sequence
```

Therefore, the correct Feedback field is:

```text
sequence
```

---

## Solution

The Action Server was changed from:

```python
feedback_msg.partial_sequence
```

to:

```python
feedback_msg.sequence
```

The Action Client was also changed from:

```python
feedback_msg.feedback.partial_sequence
```

to:

```python
feedback_msg.feedback.sequence
```

The package was then rebuilt:

```bash
colcon build
```

and the workspace was sourced again:

```bash
source install/setup.bash
```

---

## Verification

After applying the fix, the Action Client successfully received feedback:

```text
Feedback received: [0, 1, 1]
Feedback received: [0, 1, 1, 2]
Feedback received: [0, 1, 1, 2, 3]
Feedback received: [0, 1, 1, 2, 3, 5]
Feedback received: [0, 1, 1, 2, 3, 5, 8]
```

The final result was:

```text
Final result: [0, 1, 1, 2, 3, 5, 8]
```

The client also returned successfully to the terminal prompt.

---

## Lesson Learned

When working with ROS 2 interfaces, do not assume the names of Goal, Feedback, or Result fields.

Use:

```bash
ros2 interface show <interface_name>
```

to inspect the actual interface definition.

For this problem:

```bash
ros2 interface show example_interfaces/action/Fibonacci
```

helped identify the correct field name.

**Conclusion:** The error was caused by using an incorrect field name, and inspecting the ROS 2 interface provided the correct field and resolved the problem.
