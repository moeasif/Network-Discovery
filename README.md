# Network-Discovery

A simple Python script that uses Scapy to discover devices connected to your network.

## Requirements

- Python 3
- Scapy

Install dependencies with:

```
pip install -r requirements.txt
```

## Usage

Run the script with the IP range you want to scan (root privileges may be required):

```
python network.py 192.168.1.0/24
```

The script sends ARP requests and prints the IP and MAC addresses of each responding host.
