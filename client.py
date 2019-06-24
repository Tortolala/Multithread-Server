import pandas as pd
import threading
import argparse
import socket
import time

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

# dataframes initialization
df1=pd.read_csv(m1+'.csv',header=None)
df2=pd.read_csv(m2+'.csv',header=None)
result=pd.read_csv(out+'.csv',header=None)
tasks = []

# create tasks
for i in range(len(df1)):
    for j in range(len(df2)):
        tasks.append([list(df1.iloc[i]),list(df2[j]),[i,j]])

# runner function for threads
def thread_function(name):
    global tasks, result
    while True:
        if not tasks:
            print("pos me duermo")
            time.sleep(10)
        else:
            task=tasks[0]
            tasks.pop(0)
            req=str(task[0:2])
        #envia el request sin el numero de orden
            print("enviando: ",req)
            host = '192.168.2.15'
            port = 80
            BUFFER_SIZE = 2000 
            MESSAGE =req
            res=32
            result[task[2][0]][task[2][1]]=res
        '''
        # connecting with server 
            tcpClientA = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            tcpClientA.connect((host, port))
        # sending request to server
            tcpClientA.send(b'[[1,2,3],[4,5,6]]')     
        # waiting for response
            response = tcpClientA.recv(BUFFER_SIZE)
            print(response.decode("utf-8"))
        # inserting response in result df
            response=int(response)
            result[task[2][0]][task[2][1]]=res
        '''
            

if __name__ == "__main__":

    # threads initialization
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    x.join()
    # taks production


    