from tkinter import *
from info import *
from multibox import *
class tk(object):
    def __init__(self):
        '''
        Main loop of windows
        '''
        self.root= Tk()
        self.buildframe()
        self.loadtext()
        self.root.title("System monitor")
        self.root.geometry("1000x600+10+10")
        self.procinfo=""
        
    def buildframe(self):

        '''
        Root frame
        '''
        self.frame = Frame(self.root)
        '''
        Second Layer
        '''
        self.leftframe=Frame(self.frame,relief="sunken",width=200, height=600)
        self.rightframe=Frame(self.frame,relief="sunken",width=600, height=600)
        self.botframe=Frame(self.frame,relief="sunken")
        
        '''
        Third Layer
        '''
        self.ltf=Frame(self.leftframe,width=200, height=400)
        self.lbf=Frame(self.leftframe,width=200, height=200)      
        
        
        '''
        Packing
        '''


        self.ltf.pack(side=TOP,expand=True,fill=BOTH)
        self.lbf.pack(side=BOTTOM,expand=True,fill=BOTH)

        self.botframe.pack(side=BOTTOM,expand=True,fill=BOTH)
        self.leftframe.pack(side=LEFT,expand=True,fill=BOTH)
        self.rightframe.pack(side=RIGHT,expand=True,fill=BOTH)
        

        self.frame.pack(expand=True,fill=BOTH)



    def loadtext(self):
        '''
        Padding
        '''
        self.resolvedata()
        print("Load Text")
        if self.procinfo=="":#Failed, display default text
            Label(self.ltf,text='CPUinfo',font=("Arial", 12), borderwidth=2).pack()
            Label(self.lbf,text="Meminfo",font=("Arial", 12), borderwidth=2).pack()
            Label(self.rightframe,text="PIDinfo",font=("Arial", 12), borderwidth=2).pack()
            Label(self.botframe,text="Sysinfo",font=("Arial", 12), borderwidth=2).pack()

        else:
            self.cpubox=MultiListbox(self.ltf,self.cpuinfo[0])
            for item in self.cpuinfo[1:]:
                self.cpubox.insert(END,item)
            self.cpubox.pack(expand=YES, fill=BOTH)

            self.pidbox=MultiListbox(self.rightframe,self.pidinfo[0])
            for item in self.pidinfo[1:]:
                self.pidbox.insert(END,item)
            self.pidbox.pack(expand=YES, fill=BOTH)

            self.membox=MultiListbox(self.lbf,self.meminfo[0])
            for item in self.meminfo[1:]:
                self.membox.insert(END,item)
            self.membox.pack(expand=YES, fill=BOTH)
            
            Label(self.botframe,text=self.sysinfo,font=("Arial", 12), borderwidth=2).pack()

            
    def resolvedata(self):
        '''
        Get info via proc
        '''
        self.procinfo=getinfo()
        if type(self.procinfo) is not  dict:
            return None
        '''
        Sorting CPU
        The data should like this:
        'cpuinfo': {'cpuMHz': ['2808.004'],
             'cpucores': ['1'],
             'cpufamily': ['6'],
             'model': ['158'],
             'vendor_id': ['GenuineIntel']}

        The target foramt is like this:
        ((cpuMHz', 'cpucores'),  ('2808.004',1) ...)  
        '''
        temp1=list()
        temp2=list()
        for item in self.procinfo['cpuinfo']:
            temp1.append((item,'10'))
            temp2.append(self.procinfo['cpuinfo'][item][0])
        self.cpuinfo=(temp1,temp2)
        del temp1
        del temp2
        
        self.meminfo=((("MemFree",'5'),("MemTotal",'5')),(self.procinfo['meminfo']["MemFree"][0],self.procinfo['meminfo']["MemTotal"][0]))

        '''
        pidinfo:
        {'1': {'Name': ['systemd'],
                   'PPid': ['0'],
                   'State': ['S(sleeping)'],
                   'Threads': ['1']},
             '10': {'Name': ['ksoftirqd/0'],
                    'PPid': ['2'],
                    'State': ['S(sleeping)'],
                    'Threads': ['1']},
             '1026': {'Name': ['upowerd'],
                      'PPid': ['1'],
                      'State': ['S(sleeping)'],
                      'Threads': ['3']},
				... ...
            }
        '''
        temp=list()
        name=(("PID",'5'),('Name','10'),('PPid','5'),("State",'5'),('Threads','5'))
        temp=[name]
        for  item in self.procinfo['pidinfo']:# For each process
            ca=[item]
            for info in name[1:]:
                ca.append(self.procinfo['pidinfo'][item][info[0]][0])
            temp.append(ca)
        self.pidinfo=temp

        self.sysinfo=self.procinfo['sysinfo']
