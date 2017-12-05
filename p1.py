import icns
import os
import signal
import sys
import random
from threading import Thread

FLAG = 1 


class Reliability:
    def __init__(self):
        self.ack = '0'
        self.mesgIDlist = range(128)
        self.existList = []
        # 
        self.seqNum = 0
    def Encapsulate(self, data):
        mesgID = random.choice(list(set(self.mesgIDlist)-set(existList)))
        self.existList.append(meshID)
        header = self.ack + bin(mesgID).zfill(7) + bin(self.seqNum).zfill(16)
        #
        self.seqNum += 1
        RnewData = header + data
        return RnewDAta
    def Decapsulate(self, data, nb, n):
        decapData = data[24:]
        
        return decapData
    def Send_ACK(self, nb, data, n):
        self.ack = '1'
        ackMesg = self.ack + data[1:]
        n.send
        

def recv():
    # print 'thread 1'
    while 1:
        str = n.receive()
        ui.addline(str)
        ui.addline('receive')

def send(): 
    # print 'thread 2'
    while FLAG:
        signal.signal(signal.SIGINT, handler)
        mesg = os.read(fd, 100)
        # signal.signal(signal.SIGINT, handler)
        if mesg:
            ui.addline('send')
            n.send(nh, mesg)

def handler(signum, frame):
    FLAG = 0
    ui.stop()
    thread1._Thread__stop()
    # thread2.terminate()

if __name__=='__main__':
    
    network = int(sys.argv[1])
    neighbour = sys.argv[2].split(":") 
    n = icns.Network(network)
    nh = n.add_neighbour(neighbour[0], int(neighbour[1]))
    ui = icns.UI('Chat Room')
    fd = ui.getfd()
    thread1 = Thread(target=recv)
    thread1.start()
    send()    
