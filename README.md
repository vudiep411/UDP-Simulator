# Socket programming UDP protocol with python
Simulating the UDP protocol with python socket client and server architecture. Use UDP heartbeat to monitor the availability of a remote device or application that is communicating over the User Datagram Protocol (UDP). It involves sending periodic, small UDP packets called "heartbeats" from one device to another to confirm that the remote device is still available and responsive.

# How to run
* Have python installed to
Run UDP simulator

```
cd UDP-delay

```
or

```
cd UDP-heartbeat
```

then run the server

```
python server.py
```

open 2 more terminals and run each client

```
python client1.py
python client2.py
```

# Overview
<p align="center"> 
    <img src="https://firebasestorage.googleapis.com/v0/b/chatapp-be9bd.appspot.com/o/server.png?alt=media&token=ac0a8544-54d6-45d3-8180-da53701145bf"/>
</p>
<p align="center"> 
    <img src="https://firebasestorage.googleapis.com/v0/b/chatapp-be9bd.appspot.com/o/c1.png?alt=media&token=d043a85b-4eff-4599-90da-0a877aaad833"/>
</p>
<p align="center"> 
    <img src="https://firebasestorage.googleapis.com/v0/b/chatapp-be9bd.appspot.com/o/c2.png?alt=media&token=0c550a81-8aae-40fb-84a6-5dd5c18d6039"/>
</p>
