from os import name
import threading
import telnetlib
from socket import *
from datetime import datetime
from time import time
import tqdm                                 # 进度条，可自行加上



lock = threading.Lock()                     # 确保 多个线程在共享资源的时候不会出现脏数据
openNum=0                                   # 端口开放数量统计
threads=[]                                  # 线程池
t1=datetime.now()
def portscanner(host,port):
    global openNum
    server = telnetlib.Telnet()
    try:
        s=socket(AF_INET,SOCK_STREAM)
        s.connect((host,port))
        lock.acquire()
        openNum+=1

        server.open(host, port)
        #print('{0} of {1} port is open '.format(ip, port))
        with open("open_port_test.txt", "a", encoding='utf-8') as out_file:
            out_file.write('{0} of {1} port is open \n'.format(host, port)) # write to file open_port_test.txt
        print(f"{port} open")
        lock.release()
        s.close()
    except:
        pass

def main(ip,ports=range(65535)):            # 设置 端口缺省值0-65535

    setdefaulttimeout(1)
    for port in ports:
        t=threading.Thread(target=portscanner,args=(ip,port))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print(f"PortScan is Finish ,OpenNum is {openNum} record time",datetime.now()-t1)

if __name__ == '__main__':
    ip='www.baidu.com'   #输入网址或者IP
    # main(ip,[22,101,8080,8000])          # 输入端口扫描
    main(ip)                               # 全端口扫描
