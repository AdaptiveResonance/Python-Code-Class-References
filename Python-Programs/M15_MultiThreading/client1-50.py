# -*- coding: utf-8 -*-
#receives numbers 1-50 from server (Multiplex_Server.py)
import socket

# Create a socket connection for client
soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Get the server IP and port
IP = '127.0.0.1' #socket.gethostname()
PORT = 5490

# Try connecting to the server
soc.connect((IP,PORT))

# See what server sent
soc.send('Hello I am your client'.encode('utf-8'))
for i in range(50):
#while True:
    message = soc.recv(28)#Receive 28 bytes, so the server's lines don't overlap
    print(message.decode('utf-8'))

# Close the connection
soc.close()
