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

    req = SetAngle.Request(target_angle=90.0)
    future = client.call_async(req)

    rclpy.spin_until_future_complete(node, future)

    try:
        response = future.result()
        node.get_logger().info(f'Success: {response.success}')
    except Exception as e:
        node.get_logger().error(f'Service call failed: {e}')

    node.destroy_node()
    rclpy.shutdown()
