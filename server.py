import socket

def view(request):
    header, body = request.split("\n\n", 1)
    headers = header.splitlines()
    method, path, version = headers[0].split()

    response_body = ""
    if path == '/test':
        response_header = "HTTP/1.1 200 OK\nContent-Type:text/plain; charset=utf-8\n\n" 
        response_body = "Hello"
    else:
        response_header = "HTTP/1.1 404 Not Found\n\n" 
        response_body = f"127.0.0.1/{path}が見つかりません"
    return response_header + response_body 

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