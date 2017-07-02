#!/bin/env python
#encoding=utf8

from daemon import Daemon
import socket,time

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""
#设定图片服务器的家目录
home_dir="/usr/git/python-project/nbnet/picture"

class agentD(Daemon):
    def run(self):
        #                       监听ipv4, 使用流的方式
        listen_fd = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
        # TCP time_wait关闭不了，就会等待2分钟，如果端口time_wait 还是可以启动监听SO_REUSEADDR
        listen_fd.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        listen_fd.bind(("0.0.0.0",9000))
        # 设置TCP队列长度，如果超过队列数，直接关闭
        listen_fd.listen(10)

        while True:
        # socket默认阻塞，一旦网络被请求，才会被唤醒
            conn,addr = listen_fd.accept()
            print("Coming"+str(conn),str(addr)+"\n")
        # 一般请求100bit的请求http头部,如果读到没有数据，超时返回  
        # 如果浏览器客户端请求没有读完，就会被阻塞掉，4K请求头部为限制
            read_data =  buff = conn.recv(1000)
            while True:
            #获取后四位字符，如果是\r\n\r\n就是请求头部结束
                if buff[-4:] == bytes("\r\n\r\n","utf8"):
                    read_data += buff
                    break
                #read_data +=buff
                buff = conn.recv(1000)

        # 取出请求路径
            pic_name = str(read_data).split(" ")[1]
            print(pic_name)
            try:
                with open(home_dir+pic_name,"rb") as f:
                    pic_content = f.read()
                    #获取文件大小
                    length = len(pic_content)
                    html_resp = html
                    html_resp += "%d\r\n\r\n"%(length)
                    html_resp = bytes(html_resp,"utf-8")
                    html_resp += pic_content
                    conn.send(html_resp)
            except:
                html_resp = html404
                conn.send(bytes(html_resp,"utf-8"))
            conn.close()

if __name__ == "__main__":
    agentd = agentD(pidfile="agent.pid", stdout="agentd.log", stderr="agentd.log")
    agentd.run()

