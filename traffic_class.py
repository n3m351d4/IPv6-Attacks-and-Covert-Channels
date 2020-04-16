#!/usr/bin/env python3

import binascii
from scapy.all import *
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6

number_packets = 1000


def traffic_class():
    print(" CC Traffic Class attack")
    destination = "fe80::a00:27ff:fe4c:1052"
    source = "fe80::a00:27ff:fe3b:c7d"
    payload_tc = int(binascii.hexlify(b"f"), 16)
    l3 = IPv6(dst=destination, src=source, tc=payload_tc)
    l4 = UDP()
    payload = Raw(load=RandString(10))
    packets = l3 / l4 / payload
    packets.show()
    send(packets, count=int(number_packets))


traffic_class()
