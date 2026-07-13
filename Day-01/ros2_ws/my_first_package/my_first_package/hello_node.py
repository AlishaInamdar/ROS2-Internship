import rclpy
from rclpy.node import Node

class HelloNode(Node):

    def __init__(self):
        super().__init__('hello_node')
        self.get_logger().info("Hello! My first ROS2 Python node is running.")

def main(args=None):
    rclpy.init(args=args)

    node = HelloNode()

    rclpy.shutdown()

if __name__ == '__main__':
    main()
