from scapy.all import *

def handle_packet(packet):
   
    if IP in packet and ICMP in packet and packet[ICMP].type == 8:  

        packet.show()  

def receive_icmp_request():
    
    # waits for incoming packet
    sniff(filter="icmp", prn=handle_packet)

if __name__ == "__main__":

    receive_icmp_request()
