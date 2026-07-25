# Error Faced

## BrokenPipeError

### Cause
Using `ros2 pkg list | head` or `ros2 interface list | head` causes a BrokenPipeError because the `head` command stops after reading a few lines while ROS 2 is still writing output.

### Solution
Run the command without `| head` to display the complete output. This is expected Linux behaviour and not a ROS 2 installation issue.
