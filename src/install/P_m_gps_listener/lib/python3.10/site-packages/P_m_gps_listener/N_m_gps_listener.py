import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix  # GPSデータのメッセージ型

class GPSListener(Node):
    def __init__(self):
        super().__init__('gps_listener')
        self.subscription = self.create_subscription(
            NavSatFix,
            'gps/fix',  # GPSデータが公開されているトピック名
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Latitude: {msg.latitude}, Longitude: {msg.longitude}, Altitude: {msg.altitude}')

def main(args=None):
    rclpy.init(args=args)
    gps_listener = GPSListener()
    rclpy.spin(gps_listener)
    gps_listener.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

