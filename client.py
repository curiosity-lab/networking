import socket               # Import socket module

s = socket.socket()         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = socket.gethostbyaddr('192.168.43.94')
print(host)
port = 12345                # Reserve a port for your service.
s.connect((host[0], port))
print(s.recv(1024))
s.close