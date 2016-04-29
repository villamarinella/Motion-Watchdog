## aufruf python ende.py
## stoppt das Programm watch.py

import socket
import time
#### anpassen
UDP_IP = "192.168.1.100"
UDP_PORT = 8989
#######
MESSAGE = "ENDE"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
time.sleep(3)
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
