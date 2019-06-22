import logging
import threading
import time
import concurrent.futures
import argparse
import numpy

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--threads", required=True)
args = vars(ap.parse_args())

number_of_threads = int(args["threads"])

tasks = []

def thread_function(name):
    logging.info("Thread %s: starting", name)
    # time.sleep(2)

    global tasks

    while True:

        if not tasks:
            time.sleep(10)
        else:

            task = tasks[0] # chequear
            col = task[0]
            row = task[1]
            con = task[2]
            result = numpy.matmul(col, row)
        
            # Send result through connection
            # Close connection

    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    # CREATE THREAD POOL 
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        executor.map(thread_function, range(number_of_threads))

    # CREATE SOCKETS

    