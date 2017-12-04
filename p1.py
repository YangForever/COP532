import icns
import os
from threading import Thread
 
n = icns.Network(111)
nh = n.add_neighbour('131.231.115.80', 112)
ui = icns.UI('title text')
fd = ui.getfd()

def recv():
    print 'thread 1'
    while 1:
        str = n.receive()
        ui.addline(str)
        ui.addline('receive')

def send(): 
    print 'thread 2'
    while 1:
        mesg = os.read(fd, 100)
        if mesg:
            ui.addline('send')
            n.send(nh, mesg)

thread1 = Thread(target=recv)
thread2 = Thread(target=send)
thread1.start()
thread2.start()

    
    
