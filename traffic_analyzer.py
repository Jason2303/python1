from scapy.all import sniff
import pandas as pd

all_packets = []

def process_packet(packet):
    if packet.haslayer('IP'):
        all_packets.append({
            'src': packet['IP'].src,
            'dst': packet['IP'].dst,
            'proto': packet['IP'].proto
        })

sniff(prn=process_packet, count=100)

df = pd.DataFrame(all_packets)
df.to_csv("traffic_log.csv", index=False)
print("Captured 100 packets. Open traffic_analyzer.py")