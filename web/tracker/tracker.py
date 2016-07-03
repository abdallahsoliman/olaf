from scapy.all import srp, Ether, ARP, conf
import socket

class ARPScanner:
    
    def __init__(self, interface, ips):
        self.interface = interface
        self.ips = ips
    
    def scan(self):
        conf.verb = 0
        ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst = ips), timeout = 2, iface=interface, inter=0.1)
        arp_data = {}
        for snd, rcv in ans:
            mac = rcv.sprintf(r"%Ether.src%")
            ip = rcv.sprintf(r"%ARP.psrc%")
            hostname = socket.gethostbyaddr(ip)[0]
            arp_data[mac] = [ip, hostname]
        return arp_data

    
if __name__ == "__main__":
    target_mac = "c4:9a:02:75:5c:a4"
    interface = "wlp3s0"
    ips = "192.168.1.0/24"

    arp_scanner = ARPScanner(interface, ips)
    results = arp_scanner.scan()
    print(results)
