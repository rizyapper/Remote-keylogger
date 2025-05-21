import socket
from pynput.keyboard import Key,Controller, Listener

host="192.168.0.101"
port=65501
keystroke=None
def pressaction(key):
    global keystroke
    if(key==Key.esc):
        exit()
    elif(key==Key.space):
        key=" "
    elif(key==Key.enter):
        key="\n"
    elif(key==Key.shift):
        key=""
    elif(key==Key.ctrl):
        key="<ctrl>"
    stroke=str(key)
    stroke=stroke.replace("'", "")
    keystroke=stroke
    print(keystroke)
    return False
def listening():
    global keystroke
    keystroke=None
    with Listener(on_press=pressaction) as listener:
        listener.join()
    return keystroke
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    print("started")
    conn, addr=s.accept()
    # conn=list(conn)
    try:
        with conn as conn:
            print("reached")
            conn.send(b"YUP")
            while True:
                data=listening()
                print(f"sending data{data}")
                if not data:
                    break
                conn.sendall(data.encode())
    finally:
        conn.close()
