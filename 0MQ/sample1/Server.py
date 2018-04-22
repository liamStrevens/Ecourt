import zmq
from random import randrange
import json
import time

port = "5560"
port_pub = "5561"
context1 = zmq.Context()
socket1 = context1.socket(zmq.PAIR)
socket1.bind("tcp://*:5560")


context2 = zmq.Context()
socket2 = context2.socket(zmq.PUB)
socket2.bind("tcp://*:5561")
current_document = None
current_page = None
print('some good info')
time.sleep(1)
while True:
    #waits for a message to com into the presenter
    msg = socket1.recv_json()

    if current_document != msg['doc'] or current_page != msg['page']:
        #sends messages to all subscribers
        socket2.send(json.dumps(msg))
        current_document = msg['doc']
        current_page = msg['page']