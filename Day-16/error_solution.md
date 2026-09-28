# Day 16 — ROS 2 Parameters Error and Solution

## Error

While testing runtime parameter changes, the following command was executed:

```bash
ros2 param set /parameter_demo_node speed hello

The command failed with:

Setting parameter failed: Wrong parameter type, expected 'Type.DOUBLE' got 'Type.STRING'
Cause

The speed parameter was declared in Python as:

self.declare_parameter('speed', 1.5)

The default value 1.5 is a floating-point number, so ROS 2 created speed as a DOUBLE parameter.

However, the value:

hello

is a string.

Therefore, ROS 2 rejected the parameter update because the supplied value had an incompatible type.

Solution

A numeric value was provided instead:

ros2 param set /parameter_demo_node speed 2.5

The command returned:

Set parameter successful

The parameter was then verified:

ros2 param get /parameter_demo_node speed

Result:

Double value is: 2.5
Technical Lesson

ROS 2 Parameters are strongly typed.

The parameter type is determined when the parameter is declared.

For example:

self.declare_parameter('speed', 1.5)

creates a DOUBLE parameter.

Therefore, compatible numeric values should be provided when changing it.

Debugging Approach

The issue was diagnosed by examining the error message:

expected 'Type.DOUBLE' got 'Type.STRING'

This clearly indicated that the parameter expected a DOUBLE but received a STRING.

The value was corrected to a floating-point number and the parameter update succeeded.
