# coding: utf-8
#TCP socket server with multithreading for 10 client (client1-50.py)
#to receive numbers through 1-50
# helpful resource: https://realpython.com/python-sockets/#tcp-sockets
import socket
import threading
import time

def counter(client_connect):
    """counts 1-50 returning value to client"""
    count = 0
    while count<50:
        count = count+1
        #send a thank you message to the client.
        #zfill pads number to maintain 2byte num + 26byte string.
        client_connect.send('Thank you for connecting: '.encode('utf-8') +
            (bytes(str(count), encoding='utf-8').zfill(2)))#convert to bytes and utf-8 formatting
        # Close the connection with the client
        time.sleep(1)#only needed to slow down display, can be removed.
    client_connect.close()
    return 0

# Create a socket object
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get the IP and port
IP = '127.0.0.1' #socket.gethostname()
PORT = 5490
# Bind the socket to the ip and port
soc.bind((IP, PORT))
# Make the server listen for incoming connections
soc.listen(10)
print(f"Server now listening on {IP}:{PORT}")

# Wait until client connects and
# accept the connection when client tries to connect.
try:
    while True:
        client, client_addr = soc.accept()

        print('Got connection from', client_addr)
        # receiving client text
        message = client.recv(1024)
        print(message.decode('utf-8'))

        #function to return 1-50 to client
        #create threads
        thread = threading.Thread(target=counter, args=[client])
        thread.start()
        #counter(client)
    soc.close()
except KeyboardInterrupt:
    soc.close()
    print("server closed")
