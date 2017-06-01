#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from multiprocessing import Process
import os
import socket
import fileinput

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('10.3.45.144',2333))
s.listen(1)


def write(sock,addr):
    filename=sock.recv(1024).decode('utf-8')
    textfile=open('./%s'%filename,'w')
    while True:
        data=sock.recv(1024).decode('utf-8')
        if data=='over':break
        textfile.write('%s'%data)
    textfile.close()
    print('successful receive from %s'%addr[0])
    sock.close()
    quit()



while True:
    sock,addr=s.accept()
    p=Process(target=write,args=(sock,addr))
    p.start()
