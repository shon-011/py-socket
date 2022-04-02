from ensurepip import version
import socket
from urllib import response

def view(raw_request):
    try:
        request = get_request(raw_request)
        if request["path"] == '/test':
            body = "Welcome to my server!"
            response = create_response(200, body)
        else:
            body = "指定したページは存在しません。"
            response = create_response(404, body)
    except Exception as e:
        body = f"サーバーに異常が起きています。\n{e}"
        response = create_response(500, body)
    return response

def get_request(raw_request):
    header, body = raw_request.split("\r\n\r\n", 1)
    header = header.splitlines()
    method, path, version = header[0].split()
    request = {
        "method": method,
        "path": path,
        "version": version,
        "body": body,
    }
    return request

def create_response(status_code, body):
    status = {200: "200 OK", 404: "404 Not Found", 500: "500 Internal Server Error"}
    header = "Content-Type:text/plain; charset=utf-8"
    status_line = "HTTP/1.1 " + status[status_code]
    response = f"{status_line}\n{header}\n\n{body}" 
    return response

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