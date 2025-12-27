#!/bin/bash

source /opt/ros/foxy/setup.bash

dir="$HOME"
[ "$1" != "" ] && dir="$1"

cd "$dir/ros2_ws"

colcon build

source install/setup.bash

timeout 15 ros2 launch mypkg talker_listener.launch.py > /tmp/mypkg.log || true

cat /tmp/mypkg.log | grep 'Result: True, Angle: 90.0'
