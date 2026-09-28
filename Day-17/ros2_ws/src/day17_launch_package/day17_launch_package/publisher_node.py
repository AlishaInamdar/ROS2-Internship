import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class PublisherNode(Node):

    def __init__(self):
        super().__init__('publisher_node')

        self.publisher = self.create_publisher(
            String,
            'launch_demo_topic',
            10
        )

        self.timer = self.create_timer(
            1.0,
            self.publish_message
        )

        self.count = 0

    def publish_message(self):
        message = String()
        message.data = f'Launch demo message {self.count}'

        self.publisher.publish(message)

        self.get_logger().info(
            f'Published: {message.data}'
        )

        self.count += 1


def main(args=None):
    rclpy.init(args=args)

    node = PublisherNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
