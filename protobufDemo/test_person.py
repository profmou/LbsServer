import socket
from Person_pb2 import person



def CreatePerson():
    p1 = person()
    p1.id = 5
    p1.age = 30
    p1.name = 'zhangsan'
    return p1

def SerializeAndParse():
    p1 = CreatePerson()
    p1_data = p1.SerializeToString()    
    p1_copy = person()
    p1_copy.ParseFromString(p1_data)
    print(p1_copy.id)

def EncodePerson_V1(buff, type):
    return buff

def Encode_V2(buff, type):
    br = bytearray()
    br.append(type)             #T
    br.append(len(buff))        #L
    br += buff
    return br

def SendBuffToServer(encode_func):
    p1 = CreatePerson()
    p1_data = p1.SerializeToString()

    s = socket.socket()            # 创建 socket 对象 
    host = '127.0.0.1'    # 获取本地主机名 
    port = 12345                   # 设置端口号 
    s.connect((host, port)) 
    s.send(encode_func(p1_data, 1))
    s.close()        


if __name__ == "__main__":
 #   SerializeAndParse()
 #   SendBuffToServer(EncodePerson_V1)
    SendBuffToServer(Encode_V2)

    # p1 = CreatePerson()
    # p1_data = p1.SerializeToString()
    # p1_d = Encode_V2(p1_data, 1)
    # t = p1_d[0]
    # t1 = p1_d[1]
    # p11 = p1_d[2:]
    # p2 = person()
    # p2.ParseFromString(p11)
    # print(p2.name)
  #  print(p1_d[2])