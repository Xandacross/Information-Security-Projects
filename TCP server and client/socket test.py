import socket
import sys

domain=input("Enter the Domain name:")

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("The socket has been created!")
except socket.error as err:
    print(f"socket creation failed! {err}")
    sys.exit()

port=80

try:
    hostip=socket.gethostbyname(domain)
except socket.gaierror: #error will be raised if there are problems with address or hostname resolution // gaierror means "Get address info error"
    print("Failed to get IP address.")
    sys.exit()

try:
    s.connect((hostip,port))
    print(f"The socket has been successfully Connected to {domain}")
except socket.error as e:
    print(f"Connection to {domain} is not possible because of {e}")
    sys.exit()