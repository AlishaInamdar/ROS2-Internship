import sys
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class AddTwoIntsClient(Node):

    def __init__(self):
        super().__init__('add_two_ints_client')

        self.client = self.create_client(
            AddTwoInts,
            'add_two_ints'
        )

    def send_request(self, a, b):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Service not available, waiting...'
            )

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    node = AddTwoIntsClient()

    if len(sys.argv) != 3:
        node.get_logger().info(
            'Usage: ros2 run day13_services_package service_client <a> <b>'
        )
        node.destroy_node()
        rclpy.shutdown()
        return

    a = int(sys.argv[1])
    b = int(sys.argv[2])

    future = node.send_request(a, b)

    rclpy.spin_until_future_complete(node, future)

    if future.result() is not None:
        node.get_logger().info(
            f'Result: {a} + {b} = {future.result().sum}'
        )
    else:
        node.get_logger().error('Service call failed')

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
