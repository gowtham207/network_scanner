#!/usr/bin/python2
import scapy.all as scapy
import optparse

def user_input():
    parse_object=optparse.OptionParser()
    parse_object.add_option("-i","--ip",dest="ip",help="ip to search")
    return parse_object.parse_args()

def scanner(ip):
    arp_packet=scapy.ARP(pdst=ip)
    #print(arp_packet.show())
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #print(broadcast.show()
    combine=broadcast/arp_packet
    answer=scapy.srp(combine,timeout = 0,verbose=False)[0]
    return answer
    
def print_result(c):
    print("ip\t\t\t\tmac")
    print("-----------------------------------------------------")
    for element in c:
        client={"ip":element[1].psrc,"mac":element[1].hwsrc}
        print(client["ip"]+'\t\t\t'+client["mac"])


(user_input,s)=user_input()
a=scanner(user_input.ip)
print_result(a)
