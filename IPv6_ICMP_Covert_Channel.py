#!/usr/bin/env python3

from scapy.all import *
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest

number_packets = 1000


def icmp_covert_cnannel():
    print("ICMP Covert Channel")
    destination = "fe80::a00:27ff:fe4c:1052"
    source = "fe80::a00:27ff:fe3b:c7d"
    l3 = IPv6(dst=destination, src=source)
    h = ICMPv6EchoRequest(data="lol")
    l4 = UDP()
    payload = Raw(load="DC7495 N3m351d4 Inside")
    packets = l3 / h / l4 / payload
    packets.show()
    send(packets, count=int(number_packets))


icmp_covert_cnannel()


