# encoding:utf-8
from scapy.all import *


# 从scapy.all中导入所有的函数，这样就可以直接使用函数名而不用加上scapy.all.前缀
def udp_scan(dst_ip, dst_port, dst_timeout=10):
    resp = sr1(IP(dst=dst_ip) / UDP(dport=dst_port), timeout=dst_timeout)
    # 发送一个UDP包，等待回应
    if (resp is None):
        print("Port %d is open or filtered" % dst_port)
    elif (resp.haslayer(UDP)):
        # 接收到UDP包，说明端口是开放的
        print("Port %d is open" % dst_port)
    elif (resp.haslayer(ICMP)):
        if (int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) == 3):
            print("Port %d is closed" % dst_port)
        elif (int(resp.getlayer(ICMP).type) == 3 and int(resp.getlayer(ICMP).code) in [1, 2, 9, 10, 13]):
            print("Port %d is filtered" % dst_port)
        elif (resp.haslayer(IP) and resp.getlayer(IP).proto == IP_PROTOS.udp):
            print("Port %d is open" % dst_port)


udp_scan('192.168.130.130', 5000)
# 为了方便测试，这里直接写了IP地址和端口号，实际使用时可以从命令行获取
