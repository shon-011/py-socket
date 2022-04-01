import socket

def main(body):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 8800))
    
    s.send(body.encode('utf-8'))
    res = s.recv(1024)
    print('===========response=========')
    print(res.decode('utf-8'))
    
if __name__ == '__main__': 
    print('input message...')
    mes = str(input())
    main(mes)