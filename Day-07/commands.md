# ROS 2 Messages - Commands

## Source ROS 2

```bash
source /opt/ros/jazzy/setup.bash

List Available Interfaces :-
ros2 interface list

Display a Message Structure :-
ros2 interface show std_msgs/msg/String

Display Twist Message Structure :-
ros2 interface show geometry_msgs/msg/Twist

Find Topics Using a Message Type :-
ros2 topic find std_msgs/msg/String

Check the Type of a Topic :-
ros2 topic type /chatter

Publish a Message :-
ros2 topic pub /my_message std_msgs/msg/String "{data: 'Hello ROS2'}"

Display Messages Published on a Topic :-
ros2 topic echo /my_message
