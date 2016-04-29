import socket
import time
import subprocess
from thread import start_new_thread
from threading import Thread
############ anpassen
UDP_IP = "192.168.1.100"
UDP_PORT = 8989
alarmzeit=1200
## wenn in motion.py 1800 steht
alarmscript='/home/kl/s2.sh'
##################
sock = socket.socket(socket.AF_INET, # Internet
                      socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
########### globale Variablen 
data=""
def sleeper1():
    global Empfang
    global ende1
    global ende2
    ende1=False
    ende2=False
    global start
    global meldung
    meldung=time.time()
    global data
    Empfang=False
    start=time.time()
    while True:	
      if Empfang:
         meldung = data[6:20]
         meldung=float(meldung)
         print start
         start1=str(start)
         start2 = str(time.ctime(start))
         meldung1=str(meldung)
         meldung2=str(time.ctime(meldung))
         print "Local:   "+start1+ "  " + start2
         print "IP102   "+meldung1 + "  "+ meldung2
         zeit = meldung - start
         print "Zeit "+str(zeit)
         Empfang=False
         start=time.time()
      else:
           start=time.time()
	   zeit2 =  start - meldung
           print "Zeit2 "+str(zeit2)
	   if  zeit2 > alarmzeit:
	     print "Alarm"
	     output = subprocess.Popen([alarmscript,''],shell=True)  
             # Hier wird das "Alarm" Shellscript aufgerufen
      time.sleep(10)   
      if ende1:
	ende2 = True
	return

tcheck102 = Thread(target=sleeper1)
tcheck102.start()

while True:
     data, addr = sock.recvfrom(128) # buffer size is 1024 bytes
     print "Empfangen: "+data
     if data[0:5] == "IP102":
       Empfang = True
     if data == "ENDE":
       ende1 = True
     if ende2:
       break