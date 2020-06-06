import tkinter
''' 
win=tkinter.Tk() #构造窗体
my_frame = tkinter.Frame(win,   relief="sunken")
my_frame.pack()
mylist=tkinter.Listbox(my_frame,width=100) #列表框
mylist.pack()
 
for  item  in ["1","asdsa","asdsadsa","asdsadsad",1,2,3,4,5,6,7,8,9,11,22,33,44,55,66,77]: #插入内容
    mylist.insert(tkinter.END,item) #从尾部插入

tkinter.Label(win, text="This", borderwidth=2, relief="groove").pack()
win.mainloop() #进入消息循环
 '''
d=list()
p={'ss':"ojd",'sad':'daw'}
for item in p:
    d.append((item,p[item]))
print(set(d))