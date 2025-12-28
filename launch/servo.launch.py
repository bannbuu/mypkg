import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        # サーボサーバーを起動
        launch_ros.actions.Node(
            package='mypkg',
            executable='servo_server',  
            name='servo_node'
        ),
        # サーボクライアントを起動（90度送るやつ）
        launch_ros.actions.Node(
            package='mypkg',
            executable='servo_client',  
            name='servo_request_node'
        ),
    ])
