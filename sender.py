from enum import unique
import socket
import argparse
import getopt
import sys


argslist = sys.argv[1:]

def num_format(i, len):
    message = str(i)
    while len(message) < len:
        message = "0" + message

    return message


def send_payload():
    return

opts,args = getopt.getopt(argslist, 'f:a:s:c:i:')
filename = ""
TCP_IP_ADDRESS = ""
TCP_PORT_NO = ""
R_PORT_NO = ""
uniqueID = ""

for i in opts:
    if i[0] == "-f":
        filename = i[1]
    if i[0] == "-a":
        TCP_IP_ADDRESS = (i[1])
    if i[0] == "-s":
        R_PORT_NO = int(i[1])
    if i[0] == "-c":
        TCP_PORT_NO = int(i[1])
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

print(len(payload))
"""with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as clientsocket:
    clientsocket.connect((TCP_IP_ADDRESS,TCP_PORT_NO))
    clientsocket.send('ID29c4ebac'.encode())
    transaction_id = clientsocket.recv(8)"""

    Message = "ID" + uniqueID + "SN" + seqnum + transaction_id + "LAST" + last + data
