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
#prueba
tasks = []

def thread_function(name):
    logging.info("Thread %s: starting", name)
    # time.sleep(2)

    global tasks

    while True:
        if not tasks:
            time.sleep(10)
        else:
            lock.acquire()
            task = tasks[0] # chequear para compartir recurso
            tasks.pop(0)
            lock.release()
            # print("Task en thread: ", task)
            # tasks = []
            col = task[0]
            row = task[1]
            con = task[2]
            result = numpy.matmul(col, row)
            # Send result through connection
            print(result)
            con.send(bytes(str(result), "utf-8"))
            # Close connection
            con.close()

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # CREATE THREAD POOL 
    # with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
    #     executor.map(thread_function, range(number_of_threads))

    x = threading.Thread(target=thread_function, args=(1,))
    x.start()

    # CREATE SOCKETS
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("10.174.238.224", 1234))
    s.listen(5)
    print("Socket created")

    while True:
        # now our endpoint knows about the OTHER endpoint.
        
        (clientsocket, (address,port)) = s.accept()
        print(f"Connection from {address} with {port}")
        data=clientsocket.recv(1024).decode("utf-8")
        print("El cliente dice: ",data)
        # clientsocket.send(bytes("Hey there!!!","utf-8"))
        # clientsocket.close()
        data = ast.literal_eval(data)
        # print("Data 1: ", data)
        data.append(clientsocket)
        # print("Data 2: ", data)
        lock.acquire()
        tasks.append(data)
        lock.release()
        # print("Data 3: ", tasks)

    