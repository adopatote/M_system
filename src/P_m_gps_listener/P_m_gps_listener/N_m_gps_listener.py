'''
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import NavSatFix

class GPSListener(Node):
    def __init__(self):
        super().__init__('gps_listener')
        self.subscription = self.create_subscription(
            NavSatFix,
            'gps/fix',  # GPSデータが公開されているトピック名
            self.listener_callback,
            10
        )
        self.subscription

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
'''


import rclpy
from rclpy.node import Node
import csv
from sensor_msgs.msg import NavSatFix
import os

class GPSToCSVWriter(Node):
    def __init__(self):
        super().__init__('gps_to_csv_writer')
        
        # GPS_saveフォルダのパスを指定
        self.save_directory = '/home/user/M_system/src/P_m_gps_listener/GPS_save'
        
        # ディレクトリが存在しない場合は作成
        os.makedirs(self.save_directory, exist_ok=True)
        
        # CSVファイルの初期化
        csv_file_path = os.path.join(self.save_directory, 'gps_data.csv')
        
        try:
            self.csv_file = open(csv_file_path, mode='w', newline='')
            self.csv_writer = csv.writer(self.csv_file)
            # ヘッダーを書き込む
            self.csv_writer.writerow(['Latitude', 'Longitude'])
        except Exception as e:
            self.get_logger().error(f'Failed to open CSV file: {e}')
        
        self.subscription = self.create_subscription(
            NavSatFix,
            '/gps/fix',  # GPSデータのトピック名
            self.gps_callback,
            10
        )
        
    def gps_callback(self, msg):
        latitude = msg.latitude
        longitude = msg.longitude

        # 緯度経度をCSVに書き込む前にログを出力
        self.get_logger().info(f'Saving Latitude: {latitude}, Longitude: {longitude} to CSV')

        # 緯度経度をCSVに書き込む
        try:
            self.csv_writer.writerow([latitude, longitude])
        except Exception as e:
            self.get_logger().error(f'Failed to write to CSV file: {e}')

    def destroy_node(self):
        # ノードの終了時にCSVファイルを閉じる
        self.csv_file.close()
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    gps_to_csv_writer = GPSToCSVWriter()
    rclpy.spin(gps_to_csv_writer)
    gps_to_csv_writer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()



