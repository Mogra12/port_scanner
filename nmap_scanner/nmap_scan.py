import nmap

scanner = nmap.PortScanner()

print("Welcome, this is an nmap automation tool")
print("-------------------------------------------")

ip_address = input("Enter IP Address: ")
type(ip_address)

resp = input("""\nPlease enter the type of scan you want to run
                  1 - SYN ACK scan
                  2 - UDP scan
                  3 - Comprehensive scan\n""")

if resp == '1':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
elif resp == '2':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sU', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['udp'].keys())
elif resp == '3':
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_address, '1-1024', '-v -sS -sV -sC -A -O', sudo=True)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip_address].state())
    print(scanner[ip_address].all_protocols())
    print("Open Ports: ", scanner[ip_address]['tcp'].keys())
else:
    print('Enter a valid option!')