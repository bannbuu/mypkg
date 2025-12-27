#!/usr/bin/env python3

import launch
import launch_ros.actions

def generate_launch_description():
    # サーバー側 (talker.py)
    talker = launch_ros.actions.Node(
        package='mypkg',
        executable='talker.py',
    )
    # クライアント側 (listener.py)
    listener = launch_ros.actions.Node(
        package='mypkg',
        executable='listener.py',
        output='screen'
    )

    return launch.LaunchDescription([talker, listener])
