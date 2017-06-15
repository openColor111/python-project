import time, socket
#encoding=uft8
def testconn(host,port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    try:
        t1 = time.time()
        sk.connect((host,port))
        t1 = time.time()-t1
        return t1
    except Exception:
        return False

if __name__ == '__main__':
    print(testconn('111.206.186.244',80))
