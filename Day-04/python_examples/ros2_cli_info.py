import subprocess

print("=== ROS 2 CLI Information ===")

result = subprocess.run(
    ["ros2", "node", "list"],
    capture_output=True,
    text=True
)

print("\nRunning Nodes:")
print(result.stdout if result.stdout else "No nodes are running.")
