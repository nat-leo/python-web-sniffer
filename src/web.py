import time
import asyncio
from scapy.all import DNS, DNSQR, IP, sr1, UDP, conf, sniff
import websockets

list_of_traffic = []
new_data = True

def sniff_traffic_to(ip_address: str) -> str:
    # Usage:
    # >>>sniff_traffic_to(find_ip_address("www.cloudnoodlebar.com"))
    # <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
    
    conf.use_pcap = True
    packet = sniff(count=1,filter="host "+ ip_address, prn=lambda x: x.summary())
    return packet

def find_ip_address(url: str) -> str:
    dns_req = IP(dst='8.8.8.8')/UDP(dport=53)/DNS(rd=1, qd=DNSQR(qname=url))
    answer = sr1(dns_req, verbose=0)
    return parse_ip_address(answer[DNS].summary())

def parse_ip_address(s: str) -> str: 
    word_list = s.split()
    return word_list[-1][1:-1]

async def send_data(websocket):
    await websocket.send("Enter a valid URL (ex. www.google.com):")
    async for message in websocket:
        ip_address = find_ip_address(message)
        await websocket.send("Sniffing "+ip_address+"... (Listening for 15 seconds (time checked after every rquest))")
        end = time.time() + 15
        while True:
            packet = sniff_traffic_to(ip_address)
            await websocket.send(str(packet))
            if time.time() > end:
                await websocket.send("All Done! Enter another URL")
                break   

async def main():
    async with websockets.serve(send_data, "localhost", 5000):
        await asyncio.Future() # means run forever

asyncio.run(main())

#def main():
#    # keeps sniffing until 100 packets are found and summarized.
#    #sniff_traffic_to("tcp")
#    find_ip_address("www.cloudnoodlebar.com")
#    find_ip_address("www.google.com")
#    find_ip_address("www.geeksforgeeks.com")
#    sniff_traffic_to(find_ip_address("www.cloudnoodlebar.com"))
#
#if __name__ == "__main__":
#    main()