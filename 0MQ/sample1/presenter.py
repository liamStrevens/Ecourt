import zmq
import json
import time
port = "5560"
context = zmq.Context()

print "Connecting to server..."
socket = context.socket(zmq.PAIR)
socket.connect ("tcp://localhost:%s" % port)

document_id = 1
page_no = 201

data_dict = {
    'doc':document_id,
    'page': page_no
}
while True:
    time.sleep(1)
    socket.send(json.dumps(data_dict))
    data_dict['doc'] = data_dict['doc'] +1

