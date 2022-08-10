# Scapy Web Sniffer
```
Connected to ws://localhost:5000.
< Enter a valid URL (ex. www.google.com):
> cloudnoodlebar.com
< Sniffing 199.36.158.100... (stopping after 5 packets)
Connection closed: 1006 (connection closed abnormally [internal]).
natleo@Nats-MacBook-Air web-sniffer % python3 -m websockets ws://localhost:5000
Connected to ws://localhost:5000.
< Enter a valid URL (ex. www.google.com):
> cloudnoodlebar.com
< Sniffing 199.36.158.100... (stopping after 5 packets)
< All Done! Enter another URL
Connection closed: 1006 (connection closed abnormally [internal]).
```
## Installation

Clone the repo:
```
git clone https://github.com/nat-leo/python-web-sniffer.git
```

## Getting Started 

Run the server (last run using Python 3.8.9 on Mac with Apple Silicon):
```
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