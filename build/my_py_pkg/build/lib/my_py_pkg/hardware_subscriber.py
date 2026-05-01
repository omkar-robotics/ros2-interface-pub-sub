import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwareSubscriber(Node):
    def __init__(self):
        super().__init__('hardware_subscriber')

        self.subscription = self.create_subscription(
            HardwareStatus,
            'hardware_status',
            self.callback,
            10
        )

    def callback(self, msg):
        self.get_logger().info(
            f"Received -> Temp: {msg.temperature}, Status: {msg.debug_message}"
        )

def main(args=None):
    rclpy.init(args=args)
    node = HardwareSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
