import socket


def main(request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 8800))

    s.send(request.encode("utf-8"))
    res = s.recv(1024)
    print("===========response=========")
    print(res.decode("utf-8"))


if __name__ == "__main__":
    header = "GET /test HTTP/1.1\nHost:127.0.0.1\nConnection:close\r\n\r\n"
    body = ""
    request = header + body
    main(request)
