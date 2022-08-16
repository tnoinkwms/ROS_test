import rclpy
from rclpy.node import Node
from std_msgs.msg import Int64MultiArray
import numpy as np

class Publisher(Node):
    def __init__(self):
        super().__init__('publisher')
        self.i = 0
        self.pub = self.create_publisher(Int64MultiArray, 'chatter', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
    def timer_callback(self):
        self.i += 1
        self.axis = 11
        array  = [self.axis , int(np.sin(self.i)*230+10)]
        array_forPublish = Int64MultiArray(data=array)
        self.get_logger().info(f'Publishing:"{array}')
        self.pub.publish(array_forPublish)
    
def main(args = None):
    rclpy.init(args=args)
    try:
        publisher = Publisher()
        rclpy.spin(publisher)
    finally:
        publisher.destory_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()