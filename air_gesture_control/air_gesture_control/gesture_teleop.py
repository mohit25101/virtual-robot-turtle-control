import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class GestureTeleop(Node):
    def __init__(self):
        super().__init__('gesture_teleop')
        self.pub = self.create_publisher(Twist, '/cmd_vel', 10)

    def send_cmd(self, x=0.0, z=0.0):
        msg = Twist()
        msg.linear.x = x
        msg.angular.z = z
        self.pub.publish(msg)

def main():
    rclpy.init()
    node = GestureTeleop()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

