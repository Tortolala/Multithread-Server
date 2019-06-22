import socket
from threading import Thread 
import time

class TThread(Thread):
    


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    (clientsocket, (address,port)) = s.accept()
    print(f"Connection from {address} with {port}")
    data=clientsocket.recv(1024).decode("utf-8")
    print("El cliente dice: ",data)
    clientsocket.send(bytes("Hey there!!!","utf-8"))
    clientsocket.close()
