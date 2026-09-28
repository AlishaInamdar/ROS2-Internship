# ROS 2 Parameters — Concepts

## 1. What are Parameters?

ROS 2 Parameters are configuration values associated with a ROS 2 node.

They allow us to configure or change a node's behavior without modifying its source code.

Examples:

- Robot speed
- Robot name
- Sensor configuration
- Enable/disable a feature
- Threshold values
- Operating modes

---

## 2. Why are Parameters Used?

Parameters separate configuration from program logic.

For example, instead of hardcoding:

```python
speed = 1.5

we can declare speed as a ROS 2 parameter.

The value can then be changed using ROS 2 commands.

This makes the node more flexible and reusable.

3. Parameter Architecture

The basic architecture is:

          ROS 2 Node
              |
       declares parameters
              |
              v
      ROS 2 Parameter System
              |
       +------+------+
       |             |
    Get value     Set value
       |             |
       v             v
   ros2 param    ros2 param
       get           set

Parameters belong to individual nodes.

4. Declaring a Parameter in Python

In our Day 16 example:

self.declare_parameter('robot_name', 'ros_bot')
self.declare_parameter('speed', 1.5)
self.declare_parameter('enabled', True)

The first argument is the parameter name.

The second argument is the default value.

The default value also determines the parameter type.

For example:

self.declare_parameter('speed', 1.5)

creates a DOUBLE parameter.

5. Reading a Parameter

A parameter can be read from Python using:

self.get_parameter('speed').value

This returns the current value of the parameter.

Example:

speed = self.get_parameter('speed').value
6. Changing Parameters at Runtime

ROS 2 allows parameters to be changed while the node is running.

Example:

ros2 param set /parameter_demo_node speed 3.0

The parameter was changed from:

1.5

to:

3.0

No source-code modification or rebuild was required.

7. Parameter Types

ROS 2 parameters are strongly typed.

Common parameter types include:

Boolean
Integer
Double
String
Arrays of supported types

In our example:

robot_name → String
speed      → Double
enabled    → Boolean
8. Parameter Commands

List parameters:

ros2 param list /parameter_demo_node

Get a parameter:

ros2 param get /parameter_demo_node speed

Set a parameter:

ros2 param set /parameter_demo_node speed 3.0
9. Parameter Error Handling

During testing, we attempted:

ros2 param set /parameter_demo_node speed hello

This produced:

Setting parameter failed: Wrong parameter type,
expected 'Type.DOUBLE' got 'Type.STRING'

The reason was that speed was declared as a DOUBLE parameter, but hello is a STRING.

The correct command was:

ros2 param set /parameter_demo_node speed 2.5

The update was successful.
