#!/usr/bin/env python
def wc(fi):
    f = open(fi)
    count = 0
    while True:
        str1= f.read(1024)
        if str1 == "":
            break
        else:
            x = -1
            while str1[x] != ' ':
                if -x == len(str1):
                    break
                x -= 1
            str1 = str1[:x]
            f.seek(f.tell()+x+1)
            count += len(str1.split())
    return count
