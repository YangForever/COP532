
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
        self.packetIDlist = range(128)
        self.existList = []

    def Encapsulate(self, data):
        packetID = random.choice(list(set(self.mesgIDlist)-set(existList)))
        self.existList.append(packetID)
        header = self.ack + bin(mesgID)[2:].zfill(7)
        # binary: '01010....'
        newData = header + data
        return newData

    def Decapsulate(self, data, nb, n):
        if data[0] == '0':            
            decapData = data[8:]
            ackMesg = Gen_ACK(nb, data, n)
            return decapData, ackMesg
        elif data[0] == '1':
            finMesg = int(data[1:8])
            self.existList.remove(finMesg)
            return finMesg, None


    def Gen_ACK(self, nb, data, n):
        self.ack = '1'
        ackMesg = self.ack + data[1:]
        return ackMesg
        

def StringToBianry():

def BinaryToString():

def recv(n, nh, ReLayer):
    # print 'thread 1'
    while 1:
        str = n.receive()
        data, ack = ReLayer.Decapsulate(str[0])
        if ack:
            ui.addline(data)
            n.send(nh, ack)
        else:
            ui.addline('ACK from: ' + str(data))

def send(fd, n, nb, ReLayer): 
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

    ReLayer = Reliability()
    ui = icns.UI('Chat Room')
    fd = ui.getfd()
    
    thread1 = Thread(target=recv(n, nh, ReLayer))
    thread1.start()
    
    send(fd, n, nh, ReLayer)

