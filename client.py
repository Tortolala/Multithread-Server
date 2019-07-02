import pandas as pd
import threading
import argparse
import socket
import time
import numpy as np
from threading import Lock

lock=Lock()

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--threads", required=True)
ap.add_argument("-m1", "--matrix1", required=True)
ap.add_argument("-m2", "--matrix2", required=True)
ap.add_argument("-server", "--server", required=True)
ap.add_argument("-port", "--port", required=True)
ap.add_argument("-out", "--output", required=True)
args = vars(ap.parse_args())

# CATCHING ARGUMENTS
number_of_threads = int(args["threads"])
m1=str(args["matrix1"])
m2=str(args["matrix2"])
server=str(args["server"])
port2=str(args["port"])
out=str(args["output"])

# RUNNER FUNCTION 
def thread_function(name):
    global tasks, result
    while True:
        lock.acquire()
        try:
            task=tasks[0]
            tasks.pop(0)
        except:
            task=""
        lock.release()
        if task=="":
            break
        else:
            # REQUEST WITH THE INDEX
            req=task
            print("T",name," sending: ",req)
            host = server
            port = int(port2)
            BUFFER_SIZE = 2000 
            # CONNECTING TO SERVER
            tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            tcpClientA.connect((host, port))
            # SENDING REQUEST TO SERVER
            tcpClientA.send(bytes(str(req), "utf-8"))     
            # WAITING FOR RESPONSE
            response=""
            while response=="":
                response = tcpClientA.recv(BUFFER_SIZE).decode('utf-8')
            # INSERTING RESPONSE IN DF
            print(response)
            result.iloc[task[2][0]][task[2][1]]=response

        
if __name__ == "__main__":
    # dataframes initialization
    df1=pd.read_csv(m1+'.csv',header=None)
    df2=pd.read_csv(m2+'.csv',header=None)
    result=df=pd.DataFrame(np.zeros(shape=(df1.shape[0],df1.shape[0])))
    tasks = []

    # TASK CREATION
    for i in range(len(df1)):
        for j in range(len(df2)):
            tasks.append([list(df1.iloc[i]),list(df2[j]),[i,j]])
    # THREADS INITIALIZATION
    threads=[]
    for i in range(number_of_threads):
        x = threading.Thread(target=thread_function, args=(i,))
        threads.append(x)
        x.start()
    for i in threads:
        i.join()
    result.to_csv(out+".csv")
    
    


    