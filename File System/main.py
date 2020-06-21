import os
from toolbox import *
import pickle
import logging
import commandresolve
def console(data:dict,logger):
    '''
    Main console program
    '''
    consoleobj=commandresolve.commandresolve(data,logger)
    flag=True# to mark if it is time to exit
    while (flag):
        rawcommand=input(">")
        flag=consoleobj.resolvecommand(rawcommand)
    #Exit now
    logger.info("Exit Successfully")
    return #NOTE data should be saved in exit
        

if __name__=="__main__":
    #Mainloop
    #Search for file
    filename="simdisk.bin"
    '''
    Setup logger
    '''
    logger = logging.getLogger()#创建对象
    logger.setLevel(logging.INFO)#设定起始显示级别

    # 创建Handler
    # 终端Handler
    consoleHandler = logging.StreamHandler()
    consoleHandler.setLevel(logging.INFO)
    # Formatter
    formatter = logging.Formatter('%(asctime)s [%(levelname)s] \t %(message)s')
    consoleHandler.setFormatter(formatter)
 

    # 添加到Logger中
    logger.addHandler(consoleHandler)


    if not os.path.isfile(filename):
        logger.warning("File not exist. Trying to create...")
        createfile(filename,20000000)
        with open(filename,'wb') as p:
            pickle.dump({},p)
    #Build simlink
    data=dict()
    with open(filename,"rb") as f:
        data=pickle.load(f)
    
    if data !={}:
        logger.info("Get existed file data, trying to resolve...")
        if  type(data)!=dict:
            print(data)
            logger.error("File structure is unable to resolve")
            
            
        else:
            logger.info("File structure is resolved successfully")
            logger.info("Jumping to command line...")
            console(data,logger)
    else:
        logger.info("File structure is resolved successfully")
        logger.info("Jumping to command line...")
        console(data,logger)

