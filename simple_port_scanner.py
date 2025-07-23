import socket
target = input("Enter target IP: ")

ports = [21,22,23,25,53,80,443,8080]

print(f"Scanning {target}...")

for port in ports:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((target,port))
    if result == 0:
        print(f"port {port} is OPEN")
    s.close()