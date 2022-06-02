from enum import unique
import socket
import argparse
import getopt
import sys
import time 


def num_format(i, length):
    message = str(i)
    while len(message) < length:
        message = "0" + message

    return message


def send_payload(clientsocket, payload, uniqueID, transaction_id):
    
    start_time = time.time()
    m = len(payload)
    cwnd = int(m/20)
    index = 0
    seq_num = 0
    messages = []
    upper_len = m
    last = "0"
    curr_time = time.time() - start_time
    #time_frame = m/120
    lower_len = cwnd
    while curr_time < 120 and index < m:
        if m - index < cwnd:
            last = "1"
        end = min(m, index + cwnd)
        data = payload[index: end]
        #print(data)
        Message = "ID" + uniqueID + "SN" + num_format(seq_num, 7) + "TXN" + transaction_id + "LAST" + last + data
        Message = Message.encode('utf-8')
        clientsocket.sendto(Message, (UDP_IP_ADDRESS, R_PORT_NO))
        print(Message)
        print("CWND: ", cwnd, "longest known:", lower_len, "max_len:", upper_len, "index: ", index)
        try:
            servermessage, address = clientsocket.recvfrom(1024)
            servermessage = servermessage.decode('utf-8')
            print(servermessage)
            if servermessage[0:3] == "ACK":
                print("Happens")
                lower_len = cwnd
                index += cwnd
                curr_time = time.time() - start_time
                seq_num += 1
                cwnd = min(int(cwnd*1.5), upper_len)
            else:
                print(servermessage)
                upper_len = cwnd
                #cwnd = int(cwnd*.75)
                cwnd =  max(lower_len,int(cwnd*.75))

        except socket.timeout:
            print("timeout")
            upper_len = cwnd
            cwnd =  max(lower_len,int(cwnd*.75))
            #cwnd = max(lower_len, int(cwnd*.75))
            curr_time = time.time() - curr_time
            clientsocket.settimeout(curr_time)

argslist = sys.argv[1:]
opts,args = getopt.getopt(argslist, 'f:a:s:c:i:')
filename = ""
UDP_IP_ADDRESS = ""
UDP_PORT_NO = ""
R_PORT_NO = ""
uniqueID = ""

for i in opts:
    if i[0] == "-f":
        filename = i[1]
    if i[0] == "-a":
        UDP_IP_ADDRESS = (i[1])
    if i[0] == "-s":
        R_PORT_NO = int(i[1])
    if i[0] == "-c":
        UDP_PORT_NO = int(i[1])
    if i[0] == "-i":
        uniqueID = i[1]

#TCP_IP_ADDRESS = "10.0.7.141"
#TCP_PORT_NO = 6693

"""
parameters:

-f filename of payload
-a IP address of the receiver 
-s port used by the receiver 9000
-c port used by the sender 6693
-i unique ID
"""
payload = open(file = filename).read()
print(payload)

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsocket.settimeout(10)
argslist = sys.argv[1:]
clientsocket.bind(('',UDP_PORT_NO)) #my port sa email
clientsocket.sendto('ID29c4ebac'.encode('utf-8'), (UDP_IP_ADDRESS, R_PORT_NO))

transaction_id, addr = clientsocket.recvfrom(1024)
print(transaction_id)
transaction_id = transaction_id.decode('utf-8')
clientsocket.settimeout(10)
if transaction_id != "Existing alive transaction":
    
    send_payload(clientsocket, payload = payload, uniqueID= uniqueID, transaction_id= transaction_id)
#Message = "ID" + uniqueID + "SN" + seqnum + transaction_id + "LAST" + last + data



