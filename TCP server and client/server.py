import socket

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket has been created successfully.")
except socket.error as err:
    print(f"Socket could not be created! {err}")

port = 8080
host = socket.gethostbyname("localhost") 

server.bind((host, port))
server.listen()

while True:
    client, client_address = server.accept()
    print(f"Connection established with {client_address}")
