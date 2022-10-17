#encoding:utf-8

from scapy.all import *
# 从scapy.all中导入所有的函数，这样就可以直接使用函数名而不用加上scapy.all.前缀
print("TCP FIN Scan")
print("Please input the IP address:")
dst_ip = input()
print("Please input the port number:")
dst_port = int(input())
src_ip = "192.168.130.128"
src_port = RandShort()

fin_scan_pkt = sr1(IP(dst=dst_ip) / TCP(dport=dst_port, flags="F"), timeout=10)
# 发送一个TCP FIN包，等待回应
if (str(type(fin_scan_pkt)) == "<class 'NoneType'>"):
    print("Port %d is filtered or open" % dst_port)
elif (fin_scan_pkt.haslayer(TCP)):
    if (fin_scan_pkt.getlayer(TCP).flags == 0x14):
        # 接收 RST 包，说明端口是关闭的
        print("Port %d is closed" % dst_port)
    elif (fin_scan_pkt.haslayer(ICMP)):
        # 接收 ICMP 包，说明端口被过滤了
        if (int(fin_scan_pkt.getlayer(ICMP).type) == 3 and int(fin_scan_resp.getlayer(ICMP).code) in [1, 2, 3, 9, 10,
                                                                                                      13]):
            print("Port %d is filtered" % dst_port)
