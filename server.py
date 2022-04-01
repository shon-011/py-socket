import socket

def view(request):
    return request

def main():
    # AF_INET = ipv4, SOCK_STREAM = tcp
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 8800))
        s.listen()
        print("Server: Waiting for connections...")

        while True:
            client, addr = s.accept()
            rcvmsg = client.recv(1024) # 受け取るデータのバイト数
            
            # データが存在しない　＝　接続がない　
            if not rcvmsg:
                print("receive data don't exist")
                break
            else:
                print(f"Received: {rcvmsg}")
                response = view(rcvmsg.decode('utf-8'))
                # クライアントにレスポンスを送信
                client.sendall(response.encode('utf-8'))
        client.close()

if __name__ == '__main__':
    main()