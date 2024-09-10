import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostbyname('localhost')
port = 8080

try:
    client.connect((host, port))  # Connect to the server
    message = client.recv(1024)  # Receive message from the server
    print(message.decode('ascii'))  # Print received message
except socket.error as err:
    print(f"Failed to connect to server: {err}")
finally:
    client.close()  # Close the client socket
