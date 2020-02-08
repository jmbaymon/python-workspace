#existing server 
import socket
import sys

try: 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket has been created")

except socket.error as err:
    print("XXXXXXXXXXXOn") 

port = 80

try: 
    host  = socket.gethostbyname('www.google.com')
except: 
    print('Cannot connect to server ')
    sys.exit()

s.connect((host,port))
print("Connected")


    