import os

workspace = os.path.expanduser("~/ros2_ws")

print("ROS 2 Workspace Information")
print("---------------------------")
print("Workspace :", workspace)
print("Exists    :", os.path.exists(workspace))

if os.path.exists(workspace):
    print("Folders:")
    for item in sorted(os.listdir(workspace)):
        print("-", item)
