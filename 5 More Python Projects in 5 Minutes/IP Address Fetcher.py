import socket

hostname = socket.gethostname()
IP = socket.gethostbyname(hostname)

print("Computer Name:" + hostname)
print("IP address:"+IP)
