import socket

class TCPServer:
  def serve(self):
    print('サーバーを起動します')

    try:
      # socketを生成 インターネット上で通信をするためのライブラリ ※TCP通信が簡単にできるようになる
      server_socket = socket.socket()
      # SO_REUSEADDRオプションを有効化 https://linuxjm.osdn.jp/html/LDP_man-pages/man7/socket.7.html
      server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

      # socketにlocalhostのポート8080を割り当てる(bindでportを紐付け、linstenでbind済みのportを実際にプログラムに割り当てる)
      server_socket.bind(('localhost', 8080))
      server_socket.listen(5)

      # 外部からの接続を待ち、接続があったらコネクションを確立（クライアントとの接続の受付が完了）する
      # コネクションが確立すると新しいsocketインスタンスと接続したクライアントのadressが返される
      print('クライアントからの接続を待ちます。')
      (client_socket, address) = server_socket.accept()
      print(f'クライアントとの接続が完了しました remote_adress: {address}')

      # クライアントから送られてきたデータを取得する 4096はバイト数
      request = client_socket.recv(4096)

      # クライアントから送られてきたデータファイルを書き出す
      with open('server_recv.txt', 'wb') as f:
        f.write(request)

      # クライアントへ送信するレスポンスデータをファイルから取得する
      with open("server_send.txt", "rb") as f:
          response = f.read()

      # クライアントへレスポンスを送信する
      client_socket.send(response)

      # 通信を終了させる
      client_socket.close()

    finally:
      print('サーバーを停止します。')

if __name__ == '__main__':
  server = TCPServer()
  server.serve()