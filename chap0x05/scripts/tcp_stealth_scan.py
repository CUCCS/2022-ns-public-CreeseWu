from scapy.all import *
# 从scapy.all中导入所有的函数，这样就可以直接使用函数名而不用加上scapy.all.前缀
def tcpstealthscan(dst_ip, dst_port):
    pkts = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="S"), timeout=10)
    # 发送一个TCP SYN包，等待回应
    if (pkts is None):
        # 如果没有收到回应，说明目标被过滤了
        print("Port %d is filtered" % dst_port)
    elif (pkts.haslayer(TCP)):
        # 如果收到了回应，但是TCP层的flags字段不是SA，说明目标端口是关闭的
        if (pkts.getlayer(TCP).flags == 0x12):
            send_rst = sr(IP(dst=dst_ip) /
                          TCP(dport=dst_port, flags="R"), timeout=10)
            print("Port %d is open" % dst_port)
        elif (pkts.getlayer(TCP).flags == 0x14):
            print("Port %d is closed" % dst_port)
        elif (pkts.haslayer(ICMP)):
            if (int(pkts.getlayer(ICMP).type) == 3 and int(stealth_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10,
                                                                                                      13]):
                print("Port %d is filtered" % dst_port)


print("TCP Stealth Scan")
print("Please input the IP address:")
dst_ip = input()
print("Please input the port number:")
dst_port = int(input())
tcpstealthscan(dst_ip, dst_port)
