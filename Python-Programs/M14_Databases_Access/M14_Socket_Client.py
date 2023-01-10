# -*- coding: utf-8 -*-
import socket

# Create a socket connection for client
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Get the server IP and port
ip = socket.gethostname()
port = 5490

# Try connecting to the server
soc.connect((ip,port))
soc.send('Hello I am your client'.encode('utf-8'))

# See what server sent
message = soc.recv(1024)
print(message.decode('utf-8'))

# Close the connection
soc.close()
