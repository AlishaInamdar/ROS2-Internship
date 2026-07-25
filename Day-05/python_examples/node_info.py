import subprocess

print("=== ROS 2 Node Information ===\n")

result = subprocess.run(
    ["ros2", "node", "list"],
    capture_output=True,
    text=True
)

nodes = result.stdout.strip()

if nodes:
    print("Running Nodes:")
    print(nodes)
else:
    print("No nodes are running.")
