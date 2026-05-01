import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus

class HardwarePublisher(Node):
    def __init__(self):
        super().__init__('hardware_publisher')

        self.publisher_ = self.create_publisher(
            HardwareStatus,
            'hardware_status',
            10
        )

        self.timer = self.create_timer(1.0, self.publish_data)

    def publish_data(self):
        msg = HardwareStatus()
        msg.version = 1
        msg.temperature = 36.5
        msg.are_motors_ready = True
        msg.debug_message = "System running"

        self.publisher_.publish(msg)
        self.get_logger().info("Publishing data")

def main(args=None):
    rclpy.init(args=args)
    node = HardwarePublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
