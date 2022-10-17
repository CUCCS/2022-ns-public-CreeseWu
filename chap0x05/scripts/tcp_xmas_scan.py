# encoding:utf-8
from scapy.all import *


# 从scapy.all中导入所有的函数，这样就可以直接使用函数名而不用加上scapy.all.前缀


def tcp_Xmas_scan(dst_ip, dst_port, timeout=10):
    pkts = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="FPU"), timeout=10)
    # 发送一个TCP SYN包，等待回应
    if (pkts is None):
        print("Port %d is filtered or open" % dst_port)
    elif (pkts.haslayer(TCP)):
        if (pkts.getlayer(TCP).flags == 0x14):
            print("Port %d is closed" % dst_port)
    elif (pkts.haslayer(ICMP)):
        if (int(pkts.getlayer(ICMP).type) == 3 and int(pkts.getlayer(ICMP).code) in [1, 2, 3, 9, 10, 13]):
            print("Port %d is filtered" % dst_port)


tcp_Xmas_scan('192.168.130.130', 9090)
