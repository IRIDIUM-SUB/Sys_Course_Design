from os import *
from re import *
from pprint import *# Unit test
def analyze(raw:list,itemlist:list):
    '''
    Sort and find key words and return a aorted list
    '''
    itemlen=len(itemlist)
    res=["" for _ in range(itemlen)]
    final=dict()
    for item in raw:
        if itemlist==["" for _ in range(itemlen)]:
            break#Finish
        else:
            for opt in itemlist:
                if opt=="":
                    continue
                if item.find(opt)!=-1:#Match
                    res[itemlist.index(opt)]=item
                    itemlist[itemlist.index(opt)]=""
                    break
    
    for i in range(len(res)):
        res[i]=sub('\s','',res[i]) #Sort
    for item in res:#TODO: Revise to reduce circulations
        temp=item.split(":")
        final[temp[0]]=[temp[1]]
    return final
def getpid():
    '''
    Return pidinfo
    '''
    exec=popen("ls /proc -F|grep [0-9]*")
    raw=exec.readlines()
    res=findall("[0-9]+",str(raw))

    pid=list()
    for item in res:
        pid.append(int(item))
    return set(pid)#Deduplication
def getpidinfo(pid:int):
    command="cat /proc/"+str(pid)+"/status"
    exec=popen(command)
    raw=exec.readlines()
    
    if raw ==[]:#Exception
    	return False
    itemlist=["Name","PPid","State","Threads"]
    return analyze(raw,itemlist)
    
def getcpuinfo():
    command="cat /proc/cpuinfo"
    exec=popen(command)
    raw=exec.readlines()

    itemlist=["vendo","family","model","MHz","cpu cores"]
    return analyze(raw,itemlist)

def getmeminfo():
    command="cat /proc/meminfo"
    exec=popen(command)
    raw=exec.readlines()

    itemlist=["MemTotal","MemFree"]
    return analyze(raw,itemlist)

def getsysinfo():
    command="cat /proc/version"
    exec=popen(command)
    raw=exec.read()
    return raw

def getinfo():
    '''
    Use proc to get information and return dict like:
    {
        pidinfo:{PID:[Name,Parent PID,State,Threads]}
        cpuinfo:{vendor,family,model,frequency,cores},
        meminfo:[total,free],
        sysinfo:str
    }
    '''
    '''
    PID info
    '''
    info=dict()
    pidlist=set(getpid())
    result=dict()
    for pid in pidlist:
        temp=getpidinfo(pid)
        if temp==False:#Exception
            continue
        else:
            result[str(pid)]=temp
    info['pidinfo']=result
    del(result)# Release
    '''
    CPU info
    '''
    info['cpuinfo']=getcpuinfo()
    '''
    Memory info
    '''
    info['meminfo']=getmeminfo()
    '''
    System info
    '''
    info['sysinfo']=getsysinfo()
    
    return info


if __name__=="__main__":#Unit test only
    pprint(getinfo())
