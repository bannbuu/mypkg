#!/usr/bin/env python3

import rclpy  # ROS 2 のクライアント用ライブラリ
from rclpy.node import Node  # ノードを作るためのクラス
from mypkg.srv import SetAngle  # 通信の型（16ビット符号付き整数）

def cb(request, response):
    if 0.0 <= request.target_angle <= 180.0:
        response.success = True
        response.current_angle = request.target_angle
    else:
        response.success = False
        response.current_angle = -1.0
    return response

def main():
    rclpy.init()
    node = rclpy.create_node('servo_server')
    node.create_service(SetAngle, 'set_servo_angle', cb)
    
    node.get_logger().info('Servo Service Server is ready.')
    
    try:
        rclpy.spin(node)
        except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
