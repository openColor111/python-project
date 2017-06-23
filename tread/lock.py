#!/bin/env python3
#encoding:utf8
import threading,time
class Th(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.t_name = name
        # 调用父类构造函数
    def run(self):
        #获得锁然后运行
        #重写run()函数，线程默认从此函数开始执行

        threadLock.acquire()
        print(self.getName())
        for i in range(5):
            print(self.getName()+" "+str(i))
        print(self.getName() + " is over")
        threadLock.release()
        #释放锁



if __name__ == '__main__':
    #创建一个锁
    threadLock = threading.Lock()
    t1 = Th("Thread_1")
    t2 = Th("Thread_2")
    t1.start()
    t2.start()

