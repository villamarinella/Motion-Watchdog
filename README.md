This programm written in Python controls the Software Motion is still working.
It uses the snapshot function of Motion.
Place something like this into the motion.conf file:

target_dir /root/bilder
snapshot_interval 300
snapshot_filename /log/cam%t%H%M%S-snapshot

The program has two components:
The program motion.py which runs on the Motion computer
The program watch.py which runs on the controlling computer.

The communication between the computers is over LAN, UDP ports.

As well the motion.log file for the Motion computer, an alarm sample script for the controlling computer
and a small programm ende.py to finish the watch.py because CTRL-C not work.
You have to config the software on top of each program.

All this is very easy to handle and I wrote it that everybody, a newcomer as well, can understand it.

Have fun

Klaus Werner


