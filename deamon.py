#!/usr/bin/env python
#coding=utf8
 
import os, sys, time

#产生子进程，而后父进程退出
pid = os.fork()
if pid > 0:
    sys.exit(0)

#修改子进程工作目录
os.chdir("/")

#创建新的会话，子进程成为会话的首进程
os.setsid()

#修改工作目录umask
os.umask(0)

#创建孙子进程，而后子进程退出
pid=os.fork()
if pid > 0:
    sys.exit(0)

#重定向标准输出、输入、错误输出
sys.stdout.flush()
sys.stderr.flush()

si = open("/dev/null", 'r')
so = open("/dev/null", 'a+')
#错误输出不开启缓冲
se = open("/dev/null",'a+')

os.dup2(si.fileno(),sys.stdin.fileno())
os.dup2(so.fileno(), sys.stdout.fileno())
os.dup2(se.fileno(), sys.stderr.fileno())

while True:
    time.sleep(10)
    f = open('/home/test.txt','a')
    f.write('hello ')

