import os
import time
from xml.etree.ElementTree import tostring
import socket.timeout as TimeoutException

def seq_num_format(i):
    message = str(i)
    while len(message) < 7:
        message = "0" + message

    return message


def send_payload(payload, uniqueID, transaction_id):
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
    while curr_time < 120:
        if m - index < cwnd:
            last = "1"
        end = min(m, index + cwnd)
        data = payload[index: end]
        Message = "ID" + uniqueID + "SN" + seq_num_format(seq_num) + transaction_id + "LAST" + last + data
        messages.append(Message)
        clientsocket.sendto()
def main():
    
    payload = open(file = filename).read()
main()