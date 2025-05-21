import socket


host="127.0.0.1"
port=65501
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("started")
    s.connect((host, port))
    print("reached")
    status=s.recv(1024)
    if(status==b"YUP"):
        print("connected")
        with open("logged.txt", 'a')as f:
            while(True):
                reade=s.recv(1024).decode()
                if not reade:
                    break
                f.write(str(reade))
