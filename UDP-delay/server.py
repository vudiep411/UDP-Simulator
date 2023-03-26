from socket import *
import time
import random


# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))


while True:
# Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    print(f"Received {len(message)} bytes from {address}: {message.decode()}")
	
    if random.random() < 0.1:
        print('Simulating packet loss')
        continue
	
    # Simulating the delay
    delay = random.randint(10, 20) / 1000
    time.sleep(delay)
# The server responds
    serverSocket.sendto(message, address)