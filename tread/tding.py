#!/bin/env python3
#encoding:utf8
import threading,time
class Th(threading.Thread):
    def __init__(self,name):
        threading.Thread.__init__(self)
        self.t_name = name
        # 调用父类构造函数
    def run(self):
        #重写run()函数，线程默认从此函数开始执行
        print(self.getName())
        for i in range(5):
            time.sleep(1)
            print(str(i))
        print(self.getName() + " is over")



if __name__ == '__main__':
    t1 = Th("Thread_1")
    t1.setDaemon(True)
    t1.start()
    print("main thread is over")
    #t1.join()

