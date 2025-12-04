#!/usr/bin/env python3

import rclpy  # ROS 2 のクライアント用ライブラリ
from rclpy.node import Node  # ノードを作るためのクラス
from std_msgs.msg import Int16  # 通信の型（16ビット符号付き整数）

rclpy.init()  # ROS 2 を使う準備

node = Node("talker")  # ノード作成（node という「オブジェクト」を作成）
pub = node.create_publisher(Int16, "countup", 10)  # パブリッシャのオブジェクト作成
n = 0  # カウント用変数


def cb():  # タイマーで定期実行されるコールバック関数
    global n  # 関数を抜けても n がリセットされないようにする
    msg = Int16()  # メッセージの「オブジェクト」
    msg.data = n  # msg オブジェクトの data に n をセット
    pub.publish(msg)  # pub の publish でメッセージ送信
    node.get_logger().info(f"Publishing: {msg.data}")  # ログ出力（おまけ）
    n += 1


def main():
    node.create_timer(0.5, cb)  # タイマー設定（0.5秒ごとに cb を呼ぶ）
    rclpy.spin(node)  # 実行（無限ループ）


if __name__ == "__main__":
    main()

