#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16


rclpy.init()
node = Node("listener")  # ノード作成


def cb(msg):  # /countup からメッセージをもらったときに呼ばれる関数
    global node
    node.get_logger().info("Listen: %d" % msg.data)


def main():
    # /countup を購読するサブスクライバを作成
    sub = node.create_subscription(Int16, "countup", cb, 10)
    # 変数を使わないと警告が出るので、あえて参照だけしておく
    _ = sub
    rclpy.spin(node)


if __name__ == "__main__":
    main()
