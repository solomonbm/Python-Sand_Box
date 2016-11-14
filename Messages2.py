import configparser
import os
import sys
from datetime import datetime
from ftplib import FTP


def notify(msg):
    echo = True
    log = True
    if echo:
        print(msg)
    if log:
        f = open('log.txt','a')
        msg = datetime.now().strftime("%y-%m-%d-%H:%M:%S")+': ' + msg
        f.write(msg)
        f.write('\n')
        f.close()

class zoneFTP():
    def __init__(self):
        self.conn = FTP()
        self.dir = './'
        notify('The dir is :' + self.dir)

def main():
    notify('starting')
    ftp = zoneFTP()

if __name__ == "__main__":
    main()
