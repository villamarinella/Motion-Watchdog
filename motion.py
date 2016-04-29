import socket
import os
import os.path
import time
import subprocess
from glob import glob
schlafen=600
## ten minutes
raspinr="IP102 "
## Wer sendet 
pfad="/root/bilder/"
## target_dir von motion
UDP_IP = "192.168.1.100"
## hier die IP des Hauptrechners an den die Message geschickt wird
UDP_PORT = 8989
############################################
while True:
    snappfad=os.readlink(pfad+"lastsnap.jpg")
    datei=pfad+snappfad  
    print datei
    if not os.path.isfile(datei):
        time.sleep(120)
        continue
    info = os.stat(datei)
    zeit = os.path.getmtime(datei)
    zeit1 = time.ctime(zeit)
    zeit1 = str(zeit1)
    MESSAGE=raspinr+str(zeit)
    print MESSAGE
    file = open('motion.log', "a+")
    file.write(zeit1 + '\n')
    file.close()
    snaps = glob(pfad+'log/*.jpg')
    anz=len(snaps)
    for note in snaps[0:anz-1]:
        os.remove(note)
    sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT)) 
    time.sleep(schlafen)

