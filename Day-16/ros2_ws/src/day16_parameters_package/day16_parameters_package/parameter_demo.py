import rclpy
from rclpy.node import Node


class ParameterDemoNode(Node):

    def __init__(self):
        super().__init__('parameter_demo_node')

        # Declare ROS 2 parameters with default values
        self.declare_parameter('robot_name', 'ros_bot')
        self.declare_parameter('speed', 1.5)
        self.declare_parameter('enabled', True)

        # Read parameter values
        robot_name = self.get_parameter('robot_name').value
        speed = self.get_parameter('speed').value
        enabled = self.get_parameter('enabled').value

        self.get_logger().info(
            f'Robot Name: {robot_name}'
        )
        self.get_logger().info(
            f'Speed: {speed}'
        )
        self.get_logger().info(
            f'Enabled: {enabled}'
        )


def main(args=None):
    rclpy.init(args=args)

    node = ParameterDemoNode()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
