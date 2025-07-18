#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import math

class SimpleMove(Node):
    def init(self, robot_namespace):
        super().init('simple_move_node')
        self.publisher_ = self.create_publisher(
            Twist,
            f'/{robot_namespace}/cmd_vel',
            10
        )
        self.timer = self.create_timer(0.1, self.move_forward)
        self.distance_moved = 0.0

    def move_forward(self):
        msg = Twist()
        if self.distance_moved < 5.0:
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            self.distance_moved += 0.02
        else:
            msg.linear.x = 0.0
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    robot_namespace = 'robot1' 
    node = SimpleMove(robot_namespace)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if name == 'main':
    main()