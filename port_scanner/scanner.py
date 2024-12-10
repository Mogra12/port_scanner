import socket

def port_scanner(target_ip, start_port, end_port):
    print(f"Scanning {target_ip}")
    print(f"Start port: {start_port} - End port: {end_port}")
    print("-"*50)
    
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            result = s.connect_ex((target_ip, port))
            
            if result == 0:
                print(f"Port {port} OPEN")

target_IP = input("Target IP: ")
start_PORT = int(input("Start Port: "))
end_PORT = int(input("End Port: "))

try:
    target_ip = socket.gethostbyname(target_IP)[2][0]
except socket.gaierror:
    print("Invalid target.")
    exit()
    
port_scanner(target_IP,start_PORT,end_PORT)
print("-"*50)