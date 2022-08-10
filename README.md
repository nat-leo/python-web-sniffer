# Scapy Web Sniffer

On Server:
```
natleo@Nats-MacBook-Air web-sniffer % python3 src/web.py 
WARNING: No IPv4 address found on anpi1 !
WARNING: No IPv4 address found on anpi0 !
WARNING: more No IPv4 address found on en3 !
```

Interactive Client:
```
natleo@Nats-MacBook-Air web-sniffer % python3 -m websockets ws://localhost:5000
Connected to ws://localhost:5000.
< Enter a valid URL (ex. www.google.com):
> cloudnoodlebar.com
< Sniffing 199.36.158.100... (Listening for 15 seconds (time checked after every rquest))
< <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
< <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
< <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
< <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
< <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
< <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
< <Sniffed: TCP:1 UDP:0 ICMP:0 Other:0>
< All Done! Enter another URL
> 
```

## Installation

Clone the repo:
```
git clone https://github.com/nat-leo/python-web-sniffer.git
```

## Getting Started 

So far this has been testes with Python 3.8.9 on MacOS with Apple Silicon. Running on windows
requires admin privledges and Winpcap, and MacOS might require libpcap to run with sudo privledges.

Run the server 
```
python3 -m pip install -r requirements.txt
python3 src/web.py
```
or
```
python src/web.py
```
In another terminal, run the client to interact with the websocket:
```
python3 -m websockets ws://localhost:5000
```
or
```
python -m websockets ws://localhost:5000
```