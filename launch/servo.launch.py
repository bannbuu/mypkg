#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Yoshiaki Naruse <zhengyit364@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # サーボサーバーを起動
        launch_ros.actions.Node(
            package='mypkg',
            executable='servo_server.py',  
            name='servo_node'
        ),
        # サーボクライアントを起動（90度送るやつ）
        launch_ros.actions.Node(
            package='mypkg',
            executable='servo_client.py',  
            name='servo_request_node'
        ),
    ])
