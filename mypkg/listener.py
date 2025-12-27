#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from mypkg.srv import SetAngle

def main():
    rclpy.init()
    node = Node("servo_client")
    client = node.create_client(SetAngle, 'set_servo_angle')

    while not client.wait_for_service(timeout_sec=1.0):
        node.get_logger().info('waiting...')
