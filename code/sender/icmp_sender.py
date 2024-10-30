from scapy.all import *

def send_icmp_request():

    ip_layer = IP(dst="receiver", ttl=1)
    icmp_layer = ICMP()
    packet = ip_layer / icmp_layer
    
    send(packet)


if __name__ == "__main__":
    send_icmp_request()
