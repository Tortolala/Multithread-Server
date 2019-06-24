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
    global tasks
    while True:
        if not tasks:
            time.sleep(10)
        else:
            task=tasks[0]
            request=str(task[0:2])
            request
            
        #envia el request sin el numero de orden

        #recibe la respuesta
        res=32
        result[task[2][0]][task[2][1]]=res

if __name__ == "__main__":

    # threads initialization
    x = threading.Thread(target=thread_function, args=(1,))
    x.start()
    x.join()
    # taks production


    