#!/bin/bash
if [ -f /opt/ros/humble/setup.bash ]; then
    source /opt/ros/humble/setup.bash
elif [ -f /opt/ros/foxy/setup.bash ]; then
    source /opt/ros/foxy/setup.bash
fi

dir="$HOME"
[ "$1" != "" ] && dir="$1"
cd "$dir/ros2_ws"

colcon build

source install/setup.bash
timeout 15 ros2 launch mypkg talker_listener.launch.py > /tmp/mypkg.log 2>&1 || true
cat /tmp/mypkg.log
grep -q 'Result: True, Angle: 90.0' /tmp/mypkg.log
