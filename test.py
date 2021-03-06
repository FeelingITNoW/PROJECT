from enum import unique
import socket
import argparse
import getopt
import sys
import time 

argslist = sys.argv[1:]

def num_format(i, length):
    message = str(i)
    while len(message) < length:
        message = "0" + message

    return message


def send_payload(clientsocket, payload, uniqueID, transaction_id):
    clientsocket.settimeout(1)
    start_time = time.time()
    m = len(payload)
    cwnd = int(m/120)
    index = 0
    seq_num = 0
    messages = []
    last_acked = -1
    last = "0"
    curr_time = time.time() - start_time
    time_frame = m/120
    while curr_time < 120 and index < m:
        if m - index < cwnd:
            last = "1"
        end = min(m, index + cwnd)
        data = payload[index: end]
        #print(data)
        Message = "ID" + uniqueID + "SN" + num_format(seq_num, 7) + transaction_id + "LAST" + last + data
        messages.append(Message)
        clientsocket.sendto(str(Message).encode(), (UDP_IP_ADDRESS, R_PORT_NO))
        print(Message)
        try:
            message, address = clientsocket.recvfrom(1024)
            index += cwnd
            curr_time = time.time() - start_time
            seq_num += 1
            cwnd +=1
        except:
            cwnd /= 2
            curr_time = time.time() - start_time
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
clientsocket.bind(('',UDP_PORT_NO)) #my port sa email
clientsocket.sendto('ID29c4ebac'.encode(), (UDP_IP_ADDRESS, R_PORT_NO))

transaction_id, addr = clientsocket.recvfrom(1024)

print(transaction_id)
transaction_id = transaction_id.decode('utf-8')
send_payload(clientsocket, payload = payload, uniqueID= uniqueID, transaction_id= transaction_id)
#Message = "ID" + uniqueID + "SN" + seqnum + transaction_id + "LAST" + last + data



