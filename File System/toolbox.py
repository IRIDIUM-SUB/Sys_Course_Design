import time
import pickle
def createfile(filename,size:int):
    with open(filename,'wb') as f:
        f.seek(size-1)
        f.write(b'\x00')
    

def gettime():
    return time.strftime('%y-%m-%d %H:%M:%S',time.localtime(time.time()))