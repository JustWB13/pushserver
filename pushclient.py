#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import time
import fileinput

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input('please enter the ip of server:')
s.connect((ip,2333))


filename=input('please enter the name of file:')
s.send(filename.encode())
textfile=open('./%s'%filename,'r')
for line in open('./%s'%filename):
    line =textfile.readline()
    s.send(line.encode())
o='over'
s.send(o.encode())
s.close()
quit()
