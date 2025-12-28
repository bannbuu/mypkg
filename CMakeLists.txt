cmake_minimum_required(VERSION 3.8)
project(mypkg)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# 必要なパッケージを読み込む
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# 1. サービス(SetAngle.srv)から型を生成する
rosidl_generate_interfaces(${PROJECT_NAME}
  "srv/SetAngle.srv"
)

# Pythonプログラムのインストール
install(PROGRAMS
  mypkg/servo_server.py
  mypkg/servo_client.py
  DESTINATION lib/${PROJECT_NAME}
)

# 3.（launch用）
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
