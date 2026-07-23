from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP

# Packet ko process karne wali function
def packet_callback(packet):
    # Check karein ke packet mein IP layer mojood hai ya nahi
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        print(f"[+] Packet Captured:")
        print(f"    Source IP      : {src_ip}")
        print(f"    Destination IP : {dst_ip}")
        print(f"    Protocol       : {proto}")
        
        # Agar packet mein Payload (data) hai toh usay show karein
        if packet.payload:
            print(f"    Payload        : {bytes(packet.payload)[:50]}") # Pehle 50 bytes dikhaye ga
        print("-" * 50)

def main():
    print("[*] Starting Network Sniffer... Press Ctrl+C to stop.")
    # Sniff function network packets ko capture karegi
    # count=10 ka matlab hai ke sirf 10 packets capture hone ke baad program ruk jayega (aap isay hata bhi sakte hain)
    sniff(prn=packet_callback, count=10, store=False)

if __name__ == "__main__":
    main()