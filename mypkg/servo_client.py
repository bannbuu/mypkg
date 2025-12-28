#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Yoshiaki Naruse <zhengyit364@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from mypkg.srv import SetAngle

def main():
    rclpy.init()
    node = Node("servo_client")
    client = node.create_client(SetAngle, 'set_servo_angle')

    while not client.wait_for_service(timeout_sec=2.0):
     node.get_logger().info('waiting for service...')

    req = SetAngle.Request()
    req.target_angle = 90.0

    future = client.call_async(req)

    while rclpy.ok():
        rclpy.spin_once(node)
        if future.done():
            try:
                response = future.result()
                node.get_logger().info(f'Result: {response.success}, Angle: {response.current_angle}')

            except Exception as e:
                node.get_logger().info('Service call failed')
            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
