#!/bin/bash

# デフォルトでは自分のホームディレクトリを使う
dir="$HOME"
# 引数が1つ渡されたら、それをホームディレクトリとして扱う
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws"
colcon build
source /opt/ros/foxy/setup.bash  

# launchファイルを test.launch.py に変更
timeout 15 ros2 launch mypkg talker_listener.launch.py > /tmp/mypkg.log

# 判定条件をサーボ通信の成功ログに変更
cat /tmp/mypkg.log | grep 'Result: True, Angle: 90.0'
