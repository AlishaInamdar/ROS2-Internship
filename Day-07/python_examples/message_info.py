import subprocess

print("=== ROS 2 Message Information ===\n")

try:
    result = subprocess.run(
        ["ros2", "interface", "show", "std_msgs/msg/String"],
        capture_output=True,
        text=True
    )

    print("Message Type: std_msgs/msg/String")
    print("Message Structure:")
    print(result.stdout)

except Exception as e:
    print(f"Error: {e}")
