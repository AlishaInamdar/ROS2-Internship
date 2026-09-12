import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):

    def __init__(self):
        super().__init__('day11_publisher')

        self.publisher = self.create_publisher(
            String,
            'package_topic',
            10
        )

        self.counter = 0

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

    def publish_message(self):
        msg = String()
        msg.data = f'Hello from Day 11 Package: {self.counter}'

        self.publisher.publish(msg)

        self.get_logger().info(
            f'Published: {msg.data}'
        )

        self.counter += 1


def main(args=None):

    rclpy.init(args=args)

    node = PublisherNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
