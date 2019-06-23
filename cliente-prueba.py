
import socket 

host = '192.168.2.15'
port = 80
BUFFER_SIZE = 2000 
MESSAGE ='[[1,2,3],[4,5,6]]'
 
tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
tcpClientA.connect((host, port))

tcpClientA.send(b'[[1,2,3],[4,5,6]]')     
response = tcpClientA.recv(BUFFER_SIZE)
print(response.decode("utf-8"))
