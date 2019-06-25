import pandas as pd
import threading
import argparse
import socket
import time
from threading import Lock
lock=Lock()

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--threads", required=True)
ap.add_argument("-m1", "--matrix1", required=True)
ap.add_argument("-m2", "--matrix2", required=True)
ap.add_argument("-out", "--output", required=True)
args = vars(ap.parse_args())

#arguments 
number_of_threads = int(args["threads"])
m1=str(args["matrix1"])
m2=str(args["matrix2"])
out=str(args["output"])


# runner function for threads
def thread_function(name):
    global tasks, result
    while tasks:
        lock.acquire()
        task=tasks[0]
        tasks.pop(0)
        lock.release()
        req=task[0:2]
        #envia el request sin el numero de orden
        print("T",name," enviando: ",req)
        host = '172.20.10.2'
        port = 1234
        BUFFER_SIZE = 2000 
        # connecting with server 
        tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        tcpClientA.connect((host, port))
        # sending request to server
        tcpClientA.send(bytes(str(req), "utf-8"))     
        # waiting for response
        response=""
        while response=="":
            response = tcpClientA.recv(BUFFER_SIZE).decode('utf-8')
        # inserting response in result df
        print(response)
        result[task[2][0]][task[2][1]]=response

        
            

if __name__ == "__main__":
    # dataframes initialization
    df1=pd.read_csv(m1+'.csv',header=None)
    df2=pd.read_csv(m2+'.csv',header=None)
    result=pd.read_csv(out+'.csv',header=None)
    tasks = []

    # create tasks
    for i in range(len(df1)):
        for j in range(len(df2)):
            tasks.append([list(df1.iloc[i]),list(df2[j]),[i,j]])
    # threads initialization
    threads=[]
    for i in range(number_of_threads):
        x = threading.Thread(target=thread_function, args=(i,))
        threads.append(x)
        x.start()
    for i in threads:
        i.join()
    result.to_csv("result.csv")
    
    
    # taks production


    