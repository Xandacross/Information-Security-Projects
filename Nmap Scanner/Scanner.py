import nmap
import socket

# Initialize the Nmap scanner
scanner = nmap.PortScanner()

def validate_ip_or_domain(input_str):
    """
    Validates the provided input, checking if it's an IP address or a domain name.
    
    Parameters:
        input_str (str): The input to validate.

    Returns:
        str: The resolved IP address if valid, or None if invalid.
    """
    try:
        # Try to resolve a domain name to an IP address
        ip = socket.gethostbyname(input_str)
        return ip
    except socket.error:
        # If that fails, try validating as an IP address
        try:
            socket.inet_aton(input_str)  # Validate IP format
            return input_str
        except socket.error:
            return None

def perform_scan(ip, scan_type):
    """
    Performs a scan based on the scan type.
    
    Parameters:
        ip (str): The IP address to scan.
        scan_type (str): The type of scan to perform.
    """
    try:
        print("Nmap version:", scanner.nmap_version())
        
        # Dictionary to map scan types to Nmap arguments
        scan_commands = {
            "1": '-sS',  # SYN ACK Scan
            "2": '-sU',  # UDP Scan
            "3": '-sS -sV -sC -A -O'  # Comprehensive Scan with service version detection
        }
        
        if scan_type in scan_commands:
            scanner.scan(ip, '1-1024', scan_commands[scan_type])
            print(scanner.scaninfo())
            
            # Check if IP is present in the scan result
            if ip not in scanner.all_hosts():
                print(f"No results for IP: {ip}")
                return
            
            print("IP status:", scanner[ip].state())
            print("Available Protocols:", scanner[ip].all_protocols())

            # Check for TCP and UDP protocols
            if 'tcp' in scanner[ip]:
                print("\nOpen TCP Ports and Services:")
                for port in scanner[ip]['tcp'].keys():
                    state = scanner[ip]['tcp'][port]['state']
                    service = scanner[ip]['tcp'][port].get('name', 'Unknown')
                    product = scanner[ip]['tcp'][port].get('product', 'Unknown')
                    version = scanner[ip]['tcp'][port].get('version', 'Unknown')
                    print(f"Port {port}: {state} - Service: {service} (Product: {product}, Version: {version})")
            else:
                print("No open TCP ports found.")
                
            if 'udp' in scanner[ip]:
                print("\nOpen UDP Ports and Services:")
                for port in scanner[ip]['udp'].keys():
                    state = scanner[ip]['udp'][port]['state']
                    service = scanner[ip]['udp'][port].get('name', 'Unknown')
                    product = scanner[ip]['udp'][port].get('product', 'Unknown')
                    version = scanner[ip]['udp'][port].get('version', 'Unknown')
                    print(f"Port {port}: {state} - Service: {service} (Product: {product}, Version: {version})")
            else:
                print("No open UDP ports found.")
        else:
            print("Invalid scan type selected.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Prompt user for the IP address or domain name
    input_str = input("Enter the IP address or domain name: ")

    # Validate the entered input and resolve to IP address
    ip = validate_ip_or_domain(input_str)
    if not ip:
        print("Invalid IP address or domain name")
        return

    print("Resolved IP address:", ip)

    # Prompt user for the scan type
    choice = input("""\nEnter the type of scan you want to perform:
                    1) SYN ACK Scan
                    2) UDP Scan
                    3) Comprehensive Scan\n""")

    print("Selected Choice:", choice)

    # Perform the scan
    perform_scan(ip, choice)

# Run the main function
main()
