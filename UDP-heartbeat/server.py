from socket import *
import time
import random

# Create a UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))



last_heartbeat_times = {}

while True:
# Receive the client packet along with the address it is coming from
    serverSocket.settimeout(20)
    try:
        message, address = serverSocket.recvfrom(1024)

        if random.random() < 0.1:
            print('Simulating packet loss')
            continue
        
        decode = message.decode()
        client_name = decode.split()[0]
        last_heartbeat_times[client_name] = time.time()


        delay = random.randint(10, 20) / 1000
        time.sleep(delay)

        print(f"Server received: {message.decode()} at {time.ctime()}")
        for client, last_time in last_heartbeat_times.items():
            time_diff = int(time.time() - last_time)
            print(f"Server received: {message.decode()} Last heartbeat received {time_diff} seconds ago")

        serverSocket.sendto(message, address)

    except:
        # Loop through the clients and check if any have exceeded the timeout
        for client, last_time in list(last_heartbeat_times.items()):
            if time.time() - last_time > 20:
                print(f"No heartbeat received from {client} in 20 seconds.")

