import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from example_interfaces.action import Fibonacci


class FibonacciActionClient(Node):

    def __init__(self):
        super().__init__('fibonacci_action_client')

        self.action_client = ActionClient(
            self,
            Fibonacci,
            'fibonacci'
        )

    def send_goal(self, order):
        self.action_client.wait_for_server()

        goal_msg = Fibonacci.Goal()
        goal_msg.order = order

        self.get_logger().info(
            f'Sending Fibonacci goal: order={order}'
        )

        send_goal_future = self.action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )

        rclpy.spin_until_future_complete(
            self,
            send_goal_future
        )

        goal_handle = send_goal_future.result()

        if not goal_handle.accepted:
            self.get_logger().info(
                'Goal was rejected by the server.'
            )
            return

        self.get_logger().info(
            'Goal accepted by the server.'
        )

        result_future = goal_handle.get_result_async()

        rclpy.spin_until_future_complete(
            self,
            result_future
        )

        result = result_future.result().result.sequence

        self.get_logger().info(
            f'Final result: {list(result)}'
        )

    def feedback_callback(self, feedback_msg):
        feedback = feedback_msg.feedback.sequence

        self.get_logger().info(
            f'Feedback received: {list(feedback)}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = FibonacciActionClient()

    node.send_goal(6)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
