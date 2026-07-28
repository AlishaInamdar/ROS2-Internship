import subprocess

print("=== ROS 2 Topics Information ===\n")

try:
    result = subprocess.run(
        ["ros2", "topic", "list"],
        capture_output=True,
        text=True
    )

    print("Available Topics:")
    print(result.stdout)

except Exception as e:
    print(f"Error: {e}")
