# Day 15 — ROS 2 Actions Commands

## 1. Source ROS 2

```bash
source /opt/ros/jazzy/setup.bash
```

## 2. Build the Package

```bash
cd ~/ROS2-Internship/Day-15/ros2_ws
colcon build
```

## 3. Source the Workspace

```bash
source install/setup.bash
```

## 4. Check Package Executables

```bash
ros2 pkg executables day15_actions_package
```

Expected:

```text
day15_actions_package action_client
day15_actions_package action_server
```

## 5. Run the Action Server

```bash
ros2 run day15_actions_package action_server
```

The server should display:

```text
Fibonacci Action Server is ready.
```

## 6. List Available Actions

```bash
ros2 action list
```

Expected:

```text
/fibonacci
```

## 7. Check Action Information

```bash
ros2 action info /fibonacci
```

This shows the number of Action Clients and Action Servers.

## 8. Check Action Type

```bash
ros2 action type /fibonacci
```

Expected:

```text
example_interfaces/action/Fibonacci
```

## 9. Inspect the Action Interface

```bash
ros2 interface show example_interfaces/action/Fibonacci
```

Output:

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

## 10. Run the Python Action Client

```bash
ros2 run day15_actions_package action_client
```

The client sends:

```text
order = 6
```

and receives feedback and the final Fibonacci sequence.

## 11. Check the Git Status

```bash
cd ~/ROS2-Internship
git status
```

## 12. Add Day 15 Files

```bash
git add Day-15
```

## 13. Commit Day 15

```bash
git commit -m "Day 15: ROS 2 Actions"
```

## 14. Push to GitHub

```bash
git push origin main
```

## 15. Useful Action Debugging Command

When an Action interface is unclear, inspect it directly:

```bash
ros2 interface show example_interfaces/action/Fibonacci
```

This helped identify the correct Feedback field during Day 15 debugging.

