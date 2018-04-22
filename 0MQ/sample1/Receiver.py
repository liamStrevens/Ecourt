import sys
import zmq
port = "5561"
#  Socket to talk to server
context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:%s" % port)

print("Collecting to ecort server")
# zip_filter = sys.argv[1] if len(sys.argv) > 1 else "10001"
#
# # Python 2 - ascii bytes to unicode str
# if isinstance(zip_filter, bytes):
#     zip_filter = zip_filter.decode('ascii')
# socket.setsockopt_string(zmq.SUBSCRIBE, zip_filter)
total_temp = 0
socket.setsockopt_string(zmq.SUBSCRIBE,u'')
while True:
    msg = socket.recv_json()

    print('Document Id :  '+ str(msg['doc']))
    print('Page No :  '+ str(msg['page']))

print('\nstuff')
