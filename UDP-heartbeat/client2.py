from socket import *
import time
from datetime import datetime, date


now = datetime.now()
today = date.today()
d = today.strftime("%B %d %Y")
current_time = now.strftime("%H:%M:%S")
num_pings = 50  
timeout = 1.0  


# create a UDP socket
sock = socket(AF_INET, SOCK_DGRAM)
i = 0
# for i in range(num_pings):
while True:
    # send a message to the server
    message = f"Packet from client2 {i+1} {d} {current_time}".encode()
    start_time = time.time() 
    sock.sendto(message, ('localhost', 12000))
    sock.settimeout(timeout)

    try:
        data, address = sock.recvfrom(1024)
        end_time = time.time()  

        rtt_ms = (end_time - start_time) * 1000
        print(f"Vu {i+1}: Server reply: {data.decode()}, RTT = {rtt_ms:.2f} ms")
        i += 1
        time.sleep(2)

    except:
        print(f"Request timed out, Packet {i+1} loss")

# close the socket
sock.close()