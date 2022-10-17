from scapy.all import *
# 从scapy.all中导入所有的函数，这样就可以直接使用函数名而不用加上scapy.all.前缀
def tcp_connect(dst_ip, dst_port, timeout=10):
    # 定义一个函数，用于TCP连接扫描
    pkts = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="S"), timeout=timeout)
    # 发送一个TCP SYN包，等待回应
    if pkts is None:
        # 如果没有收到回应，说明目标被过滤了
        print("Port %d is filtered" % dst_port)
    elif (pkts.haslayer(TCP)):
        # 如果收到了回应，但是TCP层的flags字段不是SA，说明目标端口是关闭的
        if (pkts.getlayer(TCP).flags == 0x12):
            # 发送一个TCP RST包，用于释放连接
            send_rst = sr(IP(dst=dst_ip) / TCP(dport=dst_port, flags="AR"), timeout=timeout)
            print("Port %d is open" % dst_port)
            # 如果收到了回应，且TCP层的flags字段是RA，说明目标端口是打开的
        elif (pkts.getlayer(TCP).flags == 0x14):
            print("Port %d is closed" % dst_port)
print("TCP Connect Scan")
print("Please input the IP address:")
dst_ip = input()
print("Please input the port number:")
dst_port = int(input())
tcp_connect(dst_ip, dst_port)
