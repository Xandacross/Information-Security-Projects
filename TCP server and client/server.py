import socket

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket has been created successfully.")
except socket.error as err:
    print(f"Socket could not be created! {err}")

port = 8080
host = socket.gethostbyname("localhost")  # Or use '0.0.0.0' to accept external connections

server.bind((host, port))
server.listen()

print(f"Server is listening on {host}:{port}...")

while True:
    client, client_address = server.accept()  # Accept connection from client
    print(f"Connection established with {client_address}")

    message = "Connection established with the server"
    try:
        client.send(message.encode('ascii'))  # Send message to the client
    except socket.error as err:
        print(f"Failed to send message to {client_address}: {err}")
    
    client.close()  # Close the connection
