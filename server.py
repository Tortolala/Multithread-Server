import logging
import threading
import time
import concurrent.futures
import argparse
import numpy
import ast
import socket
from threading import Lock

lock = Lock()
ap = argparse.ArgumentParser()
ap.add_argument("-t", "--threads", required=True)
args = vars(ap.parse_args())

number_of_threads = int(args["threads"])
# TASKS ARRAY
tasks = []

def thread_function(name):
    logging.info("Thread %s: starting", name)
    global tasks
    while True:
        lock.acquire()
        try:
            task=tasks[0]
            tasks.pop(0)
        except:
            task=""
        lock.release()
        if task=="":
            time.sleep(10)
        else:
            col = task[0]
            row = task[1]
            con = task[2]
            result = numpy.matmul(col, row)
            # SEND RESULT THROUGH CONNECTION
            print(result)
            con.send(bytes(str(result), "utf-8"))
            # CLOSE CONNECTION
            con.close()

    # logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
    # CREATE THREAD POOL 
    threads=[]
    for i in range(number_of_threads):
        x = threading.Thread(target=thread_function, args=(i,))
        threads.append(x)
        x.start()

    # CREATE SOCKET
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("192.168.0.20", 1234))
    s.listen(5)
    print("Socket created")

    while True:
        #LISTENING         
        (clientsocket, (address,port)) = s.accept()
        print(f"Connection from {address} with {port}")
        data=clientsocket.recv(1024).decode("utf-8")
        print("El cliente dice: ",data)
        # clientsocket.close()
        data = ast.literal_eval(data)
        data.append(clientsocket)
        #INSERTING TASKS
        lock.acquire()
        tasks.append(data)
        lock.release()

    