# mypkg

![test](https://github.com/bannbuu/mypkg/actions/workflows/test.yml/badge.svg)

サーボモーターの角度制御をシミュレーションするためのROS 2パッケージです。

## 概要
独自のサービス定義を用いて、指定された角度(90度)にサーボモーターを動作させるための通信（Service/Client）を提供します。

- `$servo_server.py` (servo_node): クライアントからの角度リクエストを処理します。
- `$servo_client.py` (servo_request_node): 起動時に自動的に角度リクエスト（90度）を送信します。

## 実行方法
```bash
ros2 launch mypkg servo.launch.py
```

## 実行例
```bash
[INFO] [servo_server.py-1]: process started with pid [xxxx]
[INFO] [servo_client.py-2]: process started with pid [xxxx]
[servo_server.py-1] [INFO] [servo_node]: Servo Service Server is ready.
[servo_client.py-2] [INFO] [servo_request_node]: Result: True, Angle: 90.0
[INFO] [servo_client.py-2]: process has finished cleanly
```

## ノードと通信
### サービス型
####mypkg/srv/SetAngle
 - リクエスト:```bashfloat32 angle(目標角度)```
 - レスポンス:```bashbool success(動作確認)```
### 通信詳細
- Service名:```bash/set_servo_angle```
- Node名:```bashservo_node, servo_request_node```


