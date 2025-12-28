# mypkg

![test](https://github.com/bannbuu/mypkg/actions/workflows/test.yml/badge.svg)

サーボモーターの角度制御をシミュレーションするためのROS 2パッケージです。

## 概要
独自のサービス定義を用いて、指定された角度(90度)にサーボモーターを動作させるための通信（Service/Client）を提供します。

- '$servo_server.py' (servo_node): クライアントからの角度リクエストを処理します。
- '$servo_client.py (servo_request_node): 起動時に自動的に角度リクエスト（90度）を送信します。


