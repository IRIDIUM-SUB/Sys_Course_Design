from fileprocessing import *
from prettytable import PrettyTable
import logging
from toolbox import *
import random
import pickle
class commandresolve(fileprocessing):
    def __init__(self,data:dict,logger,):
        self.data=data
        self.path=data
        self.auth=False
        self.logger=logger
        self.cmd=['mkfs','ls','pwd','cd','rm','su','mkdir','touch','cat','exit']
    def resolvecommand(self,rawcommand):
        self.raw=rawcommand
        cmdlist=self.raw.split()
        if cmdlist[0] not in self.cmd:
            self.logger.error("Command not found")
            return True
        name=cmdlist[0]
        if name=='mkfs':
            self.mkfs()
            return True
        elif name=='ls':
            self.ls()
            return True
        elif name=="pwd":
            self.pwd()
            return True
        elif name=="cd":
            if len(cmdlist)<2:
                self.logger.error("Invalid command")
                return True
            else:
                self.cd(cmdlist[1])
                return True
        elif name=="rm":
            if len(cmdlist)<2:
                self.logger.error("Invalid command")
                return True
            else:
                self.rm(cmdlist[1])
                return True
        elif name=='su':
            self.su()
            return True
        elif name=="mkdir":
            if len(cmdlist)<2:
                self.logger.error("Invalid command")
                return True
            else:
                self.mkdir(cmdlist[1])
                return True
        elif name=='touch':
            if len(cmdlist)<2:
                self.logger.error("Invalid command")
                return True
            else:
                self.touch(cmdlist[1])
                return True
        elif name=='cat':
            if len(cmdlist)<2:
                self.logger.error("Invalid command")
                return True
            else:
                self.cat(cmdlist[1])
                return True
        elif name=='exit':
            self.exit()
            return False