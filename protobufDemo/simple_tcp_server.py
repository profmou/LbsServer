import socket                 # 导入 socket 模块 

from Person_pb2 import person


def DecodePerson_V1(buff):
    p = person()
    p.ParseFromString(buff)
    return p

def Decode_V2(buff):
    type = buff[0]          #check type ,1 - person 2 - car
    length = buff[1]
    data = buff[2:]
    p2 = person()
    p2.ParseFromString(data)
    return p2

def StartServer(decode_func):
    s = socket.socket()           # 创建 socket 对象 
    host = socket.gethostname()   # 获取本地主机名 
    port = 12345                  # 设置端口 
    s.bind(('127.0.0.1', port))          # 绑定端口 
    s.listen(5)                   # 等待客户端连接 
    while True: 
        c, addr = s.accept()      # 建立客户端连接。 
        print('连接地址：', addr)
        buff = c.recv(256)
        p = decode_func(buff)        
        print('id:',p.id,',name:',p.name)
        c.close()                 # 关闭连接

if __name__ == '__main__':
    #StartServer(DecodePerson_V1)
    StartServer(Decode_V2)