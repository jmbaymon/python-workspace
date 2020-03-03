import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# IPV4 and TCP

s.bind((socket.gethostbyname(""), 1234))#ip and port

s.listen(5)


while True:
    clientsocket, address = s.accept()
    msg = "Welcome to the Server!"
    msg = f'{len(msg):<{HEADERSIZE}}'+ msg# header and msg 


    clientsocket.send(bytes(msg, "utf-8"))
    # clientsocket.close()
