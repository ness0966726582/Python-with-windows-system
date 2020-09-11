#取得本機資訊

import socket
import getpass
import platform
import uuid#通用唯一识别码

myname1=socket.getfqdn(socket.gethostname())
#socket.getfqdn(name)将使用点号分隔的 IP 地址字符串转换成一个完整的域名
#或者这样
myname2=platform.uname()[1]
myaddr=socket.gethostbyname(myname1)
#socket.gethostbyname(hostname)将主机名解析为一个使用点号分隔的 IP 地址字符串
user=getpass.getuser()
#获得机器名
myarchitecture=platform.architecture()
#返回系统架构信息,好像不怎么准确
myplatform=platform.platform()
mac=uuid.UUID(int=uuid.getnode())
MAC=mac.hex[-12:]
 
print ("User   : " + user) 
print ("Domain : " + myname1)
print ("Name   : " + myname2)
print ("IP     : " + myaddr)
print ("MAC    : " + MAC)
print ("")
print ("OS platform : " + str(myplatform)+"---"+str(myarchitecture))
input()
