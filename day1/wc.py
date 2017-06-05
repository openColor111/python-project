#!/usr/bin/env python
def wc(fi):
    f = open(fi)
    # 统计单词全局变量
    count = 0
    # 统计读取几次
    k = 0
    while True:
    # 一次访问的吞吐量决定了速度
        str1= f.read(1048576)
        k +=1
        # 判断是否读到数据
        if str1 == "":
            break
        else:
        #如果读到数据，就要找末尾最近的空格
            x = -1
            while str1[x] != ' ':
        #判断如果这是最后一段读取，那么就不需要寻找空格
                if len(str1) != 1048576:
                    break
                else:
                    x -= 1
            str1 = str1[:x]
            f.seek(f.tell()+x+1)
        #通过数组统计个数
            count += len(str1.split())
    return (count,k)
if __name__ == '__main__':
    wc('/var/log/messages-20170517')


