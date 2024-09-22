import nmap
import socket

# Initialize the Nmap scanner
scanner = nmap.PortScanner()

def validate_ip(ip):
    """
    Validates the provided IP address.
    
    Parameters:
        ip (str): The IP address to validate.

    Returns:
        bool: True if the IP address is valid, False otherwise.
    """
    try:
        socket.inet_aton(ip)  # Validate IP format
        return True
    except socket.error:
        return False

# Prompt user for the IP address
ip = input("Enter the IP address: ")

# Validate the entered IP address
if not validate_ip(ip):
    print("Invalid IP address")
    exit()

print("Entered IP address:", ip)

# Prompt user for the scan type
choice = input("""\nEnter the type of scan you want to perform:
                1) SYN ACK Scan
                2) UDP Scan
                3) Comprehensive Scan\n""")

print("Selected Choice:", choice)

# SYN ACK Scan
if choice == "1":
    try:
        print("Nmap version:", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-sS')  # Perform SYN ACK scan
        
        print(scanner.scaninfo())
        print("IP status:", scanner[ip].state())
        print("Available Protocols:", scanner[ip].all_protocols())
        
        if 'tcp' in scanner[ip].all_protocols():
            print("Open TCP Ports:", scanner[ip]['tcp'].keys())
        else:
            print("No open TCP ports found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# UDP Scan
elif choice == "2":
    try:
        print("Nmap version:", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-sU')  # Perform UDP scan
        
        print(scanner.scaninfo())
        print("IP status:", scanner[ip].state())
        print("Available Protocols:", scanner[ip].all_protocols())
        
        if 'udp' in scanner[ip].all_protocols():
            print("Open UDP Ports:", scanner[ip]['udp'].keys())
        else:
            print("No open UDP ports found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Comprehensive Scan
elif choice == "3":
    try:
        print("Nmap version:", scanner.nmap_version())
        scanner.scan(ip, '1-1024', '-sS -sV -sC -A -O')  # Comprehensive scan
        
        print(scanner.scaninfo())
        print("IP status:", scanner[ip].state())
        print("Available Protocols:", scanner[ip].all_protocols())
        
        if 'tcp' in scanner[ip].all_protocols():
            print("Open TCP Ports:", scanner[ip]['tcp'].keys())
        else:
            print("No open TCP ports found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Handle invalid scan choice
else:
    print("Enter a valid option.")
