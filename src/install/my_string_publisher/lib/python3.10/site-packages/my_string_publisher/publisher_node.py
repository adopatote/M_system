import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class StringPublisher(Node):
    def __init__(self):
        super().__init__('string_publisher')
        self.publisher_ = self.create_publisher(String, 'string_topic', 10)
        timer_period = 2  # 2秒ごとに送信
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, ROS 2! Count: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    string_publisher = StringPublisher()
    rclpy.spin(string_publisher)
    string_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

