import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("127.0.0.1",5000))
s.listen(5)
conn,addr=s.accept()
print("Got connection from",addr)

while True:

    data = "Tamim=>" + input(" ")
    conn.send(bytes(data, encoding="utf-8"))
    print(conn.recv(1024))

