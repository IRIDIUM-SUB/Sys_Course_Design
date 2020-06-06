# `\proc` monitor dev log

## Environments requirement

- Linux Ubuntu 20.04LTS
- Python 3.8.3 32 bits
  - `Tkinter`

## Project Design

1. process info `/pid`
2. memory info `/meminfo`
3. CPU info `/cpuinfo`
4. System info `/version`

## Technical Design

- `main.py`: Main entrance and main loop
- `tk.py`: Basic `Tkinter` component
- `info.py`: Get and process information via `\proc`

The information need to gather and sort:

1. PID information
   1. PID `/$pid`
   2. Name `/status/Name`
   3. Parent PID `/status/PPid`
   4. State `/status/State`
   5. Threads `/status/Threads`
2. CPU information
   1. 生产商`vendor_id`
   2. 系列代号`cpu family`
   3. 名称`model name`
   4. 频率`cpu MHz`
   5. 核数`cpu cores`
3. Memory information
   1. 总内存`Memtotal`
   2. 空闲内存`Memfree`
4. System information

### Get PID info

#### Get PID

1. Use `ls /proc -F|grep [0-9]*` to get raw test. Use absolute path to secure it runs in any place
2. Use regex to match:`findall("[0-9]+",str(raw))`
3. Get the list of all PIDs.

#### Get Info

Visit `/status` to get information.

==Note==: Use improved solution to boost: Scanning the whole raw text even less than one time and get all information

```python
res=["" for _ in range(4)]

itemlist=["Name","PPid","State","Threads"]

for item in raw:
	if itemlist==["" for _ in range(4)]:
		break#Finish
	else:
		for opt in itemlist:
			if opt=="":
				continue
			if item.find(opt)!=-1:#Match
				res[itemlist.index(opt)]=item
				itemlist[itemlist.index(opt)]=""#Remove opt
				break
print(res)# Revised: Use dict{name:value} instead.
```

==Note==: Some processes are killed when the program is executing. Remember to get rid of them from the list.

### Get CPU info 

Simply use `cat /proc/cpuinfo` to get information and revise.

### Get memory info

\*\*Omitted\*\*

### Get kernel info

\*\*Omitted\*\*

## Unit Test

Now test the non-GUI version in the environment.

`pprint` is needed in the unit test.

It goes like that:

```json
{'cpuinfo': {'cpuMHz': ['2808.004'],
             'cpucores': ['1'],
             'cpufamily': ['6'],
             'model': ['158'],
             'vendor_id': ['GenuineIntel']},
 'meminfo': {'MemFree': ['172772kB'], 'MemTotal': ['2006888kB']},
 'pidinfo': {'1': {'Name': ['systemd'],
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
            },
'sysinfo': 'Linux version 5.4.0-26-generic (buildd@lcy01-amd64-029) (gcc '
            'version 9.3.0 (Ubuntu 9.3.0-10ubuntu2)) #30-Ubuntu SMP Mon Apr 20 '
            '16:58:30 UTC 2020\n'
}             
```

It runs smoothly.

## Display Design

Use Multi-Columns list to contain information.

Display format is `((Names),(Value1),(vaule2),...)`

1. Sort the raw data `self.procinfo` like above to the target format
2. When packing, using `info[0]` as the column and the followings are data.

```python
            self.cpubox=MultiListbox(self.ltf,self.cpuinfo[0])
            for item in self.cpuinfo[1:]:
                self.cpubox.insert(END,item)
            self.cpubox.pack(expand=YES, fill=BOTH)

            self.pidbox=MultiListbox(self.rtf,self.pidinfo[0])
            for item in self.pidinfo[1:]:
                self.pidbox.insert(END,item)
            self.pidbox.pack(expand=YES, fill=BOTH)

            self.membox=MultiListbox(self.lbf,self.meminfo[0])
            for item in self.meminfo[1:]:
                self.membox.insert(END,item)
            self.membox.pack(expand=YES, fill=BOTH)
```

## Assemble Test

![image-20200605223702059](proc%20monitor%20dev%20log.assets/image-20200605223702059.png)

还行,需要进一步调整框架.

- 调整框架大小
- 调整栏目宽度
- 调整框架结构

![image-20200605230239828](proc%20monitor%20dev%20log.assets/image-20200605230239828.png)

成品.