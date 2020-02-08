import socket

HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# IPV4 stream of data
s.connect((socket.gethostbyname(""), 1234))#ip and port
full_msg = ''
new_msg = True
while True: #buffers data     
    msg = s.recv(16)
    if new_msg:
        print(f"new message length:{msg[:HEADERSIZE]}")
        msglen = int(msg[:HEADERSIZE])
        new_msg= False
    print(f"full message length: {msglen}")

    full_msg += msg.decode("utf-8")
print(len(full_msg))

if len(full_msg) - HEADERSIZE == msglen:
    print("full msg revcd")
    print(full_msg[HEADERSIZE:])
    new_msg = True
    full_msg = ''