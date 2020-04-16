#!/usr/bin/env python3

import binascii
from scapy.all import *
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6

number_packets = 1000


def flow_label():
    print("CC Flow Label attack")
    destination = "fe80::a00:27ff:fe4c:1052"
    source = "fe80::a00:27ff:fe3b:c7d"
    payload_fl = int(binascii.hexlify(b"DC"), 16)
    l3 = IPv6(dst=destination, src=source, fl=payload_fl)
    l4 = UDP()
    payload = Raw(load=RandString(10))
    packets = l3 / l4 / payload
    packets.show()
    send(packets, count=int(number_packets))


flow_label()




