'''Basic processing API'''
from prettytable import PrettyTable
import logging
from toolbox import *
import random
import pickle
class fileprocessing(object):
    def __init__(self,data:dict,logger):
        self.data=data
        self.path=data
        self.auth=False
        self.logger=logger#logger obj
        return
    def mkfs(self):
        if not self.auth :
            self.logger.error("Operation not permitted")
            return
        else:
            del self.data
            del self.path
            self.data=dict()
            self.path=self.data
            self.logger.info("Format successfully")
            return
    def ls(self):
        table = PrettyTable(['Name','Type','Create Time','Change Time','Owner','Size'])
        for obj in self.path:
            if obj in ['name','type','ctime','mtime','owner','size']:
                continue
            table.add_row([obj,self.path[obj]['type'],self.path[obj]['ctime'],self.path[obj]['mtime'],self.path[obj]['owner'],self.path[obj]['size']])
        print(table)
        return
    def pwd(self):
        print(self.path)
        return
    def cd(self,newpath):
        if  newpath in self.path:
            if self.path[newpath]['type']=="Directory":
                self.path=self.path[newpath]
                self.logger.info("Change Successfully.")
                return
            else:
                self.logger.error("%s is not a directory"%newpath)
                return
        else:
            self.logger.error("File or dorectory not exist")
            return
    def  rm(self,target):
        if target in self.path:
            #if root file
            if  self.auth:
                del self.path[target]
                self.logger.info("%s has been removed"%target)
                return
            elif self.path[target]['owner']== 'user'  and not self.auth:
                del self.path[target]
                self.logger.info("%s has been removed"%target)
                return
            else:
                self.logger.error("Operation is not permitted")
                return
        else:
            self.logger.error("File or dorectory not exist")
            return
    def su(self):
        self.auth= not self.auth
        return
    def mkdir(self,name):
        #Check if the name vaild
        if name in ['type','ctime','mtime','owner','size']:
            self.logger.error("Name is not permitted")
            return 
        if name in self.path:
            self.logger.error("Name already exist")
            return 
        temp=dict()
        temp['type']="Directory"
        temp['ctime']=gettime()
        temp['mtime']=temp['ctime']
        temp['owner']=None
        temp['size']=None
        self.path[name]=temp
        return
    def touch(self,name):
        #Check if the name vaild
        if name in ['type','ctime','mtime','owner','size']:
            self.logger.error("Name is not permitted")
            return 
        if name in self.path:
            self.logger.error("Name already exist")
            return 
        temp=dict()
        temp['type']="File"
        temp['ctime']=gettime()
        temp['mtime']=temp['ctime']
        if self.auth:
            temp['owner']='root'
        else:
            temp['owner']='user'
        temp['size']=random.randint(0,10000000)
        self.path[name]=temp
        return
    def cat(self,name):
        if name not in self.path:
            self.logger.error("File not exist")
            return 
        if self.path[name]['type']=="Directory":
            self.logger.error("It is a directory, not a file")
            return
        if self.auth ==False and self.path[name]['owner']=='root':
            self.logger.error("Operation not permitted")
            return
        self.logger.info("Open file successfully")
        return

    def exit(self):
        with open('simdisk.bin',"wb") as f:
            pickle.dump(self.data,f)
            self.logger.debug("%s"%self.data)
            self.logger.info("Data write successfully")
        return    
            
        