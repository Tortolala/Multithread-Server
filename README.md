# Python Multithreading

Python server and client arquitecture using multithreading to handle matrix multiplications.

### Tests

**a)** 1 thread on server - 3 threads on client 
##### Server
`python3 server.py -t 1`

##### Client
`python3 client.py -t 3 -m1 matriza -m2 matrizb -server [server ip] -port 1234 -out resultado`

**b)** 3 threads on server - 3 threads on client 
##### Server
`python3 server.py -t 3`

##### Client
`python3 client.py -t 3 -m1 matriza -m2 matrizb -server [server ip] -port 1234 -out resultado`

**c)** 3 threads on server - 1 thread on client 
##### Server
`python3 server.py -t 3`

##### Client
`python3 client.py -t 1 -m1 matriza -m2 matrizb -server [server ip] -port 1234 -out resultado`