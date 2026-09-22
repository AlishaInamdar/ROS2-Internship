import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts


class MultiRequestClient(Node):

    def __init__(self):
        super().__init__('multi_request_client')

        self.client = self.create_client(
            AddTwoInts,
            'add_two_ints'
        )

        self.get_logger().info(
            'Multi-Request Client is ready.'
        )

    def send_request(self, a, b):
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Waiting for Add Two Ints service...'
            )

        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        return self.client.call_async(request)


def main(args=None):
    rclpy.init(args=args)

    node = MultiRequestClient()

    requests = [
        (10, 20),
        (50, 25),
        (100, 200)
    ]

    futures = []

    for a, b in requests:
        future = node.send_request(a, b)
        futures.append((a, b, future))

    for a, b, future in futures:
        rclpy.spin_until_future_complete(node, future)

        if future.result() is not None:
            node.get_logger().info(
                f'Result: {a} + {b} = {future.result().sum}'
            )
        else:
            node.get_logger().error(
                f'Service call failed for {a} + {b}'
            )

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
