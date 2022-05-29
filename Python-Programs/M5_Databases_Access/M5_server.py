# -*- coding: utf-8 -*-
import socket

# Create a socket object
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get the IP and port
ip = socket.gethostname()
port = 5490
# Bind the socket to the ip and port
soc.bind((ip, port))
# Make the server listen for incoming connections
print(f"Server listenning on {ip}:{port}")
soc.listen()
# Wait until client connects and
# accept the connection when client tries to connect.
client, client_addr = soc.accept()

print('Got connection from', client_addr)

#print message from client
message = client.recv(1024)
print(message.decode('utf-8')

# send a thank you message to the client.
client.send('Hello, Im your server, Thank you for connecting'.encode('utf-8'))

# Close the connection with the client
client.close()
soc.close()
