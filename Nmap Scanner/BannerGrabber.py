import socket

def main():
    ip = input("Enter the IP you want to scan: ")
    port = input("Enter the port: ")
    banner(ip, port)

def banner(ip, port):
    try:
        # Initialize a socket and connect to the given IP and port
        s = socket.socket()
        s.settimeout(5)  # Optional: Timeout in case the connection takes too long
        s.connect((ip, int(port)))

        # Receive the banner and decode it to a string
        banner = s.recv(1024).decode().strip()
        print(f"Banner for {ip}:{port} -> {banner}")

    except socket.error as e:
        print(f"Error: {e}")
    finally:
        # Ensure the socket is closed after the operation
        s.close()

main()
