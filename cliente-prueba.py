
import socket 

host = '192.168.2.15'
port = 2004
BUFFER_SIZE = 2000 
MESSAGE ='[[1,2,3],[4,5,6]]'
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

tcpClientA.send(MESSAGE)     
response = tcpClientA.recv(BUFFER_SIZE)
print (" Client received data:", response)
