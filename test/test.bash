#!/bin/bash

# デフォルトでは自分のホームディレクトリを使う
dir="$HOME"
# 引数が1つ渡されたら、それをホームディレクトリとして扱う
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws"
colcon build
source "$dir/.bashrc"

# 10秒間だけ talker と listener を起動してログを取る
timeout 10 ros2 launch mypkg talker_listener.launch.py > /tmp/mypkg.log

# ログの中に「Listen: 10」という行があればOKというテスト
cat /tmp/mypkg.log | grep 'Listen: 10'

