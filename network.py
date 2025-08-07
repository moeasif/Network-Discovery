#!/usr/bin/env python3
"""Simple ARP-based network discovery tool."""
from scapy.all import ARP, Ether, srp
import argparse


def scan(target: str):
    """Scan the target IP or range and return a list of discovered hosts."""
    arp = ARP(pdst=target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = srp(packet, timeout=1, verbose=False)[0]

    clients = []
    for _, received in result:
        clients.append({"ip": received.psrc, "mac": received.hwsrc})
    return clients


def main():
    parser = argparse.ArgumentParser(
        description="Discover devices on the local network using ARP requests.")
    parser.add_argument(
        "target",
        nargs="?",
        default="192.168.1.0/24",
        help="IP address or range to scan (default: 192.168.1.0/24)",
    )
    args = parser.parse_args()

    hosts = scan(args.target)
    print("IP\t\tMAC Address")
    print("-" * 30)
    for host in hosts:
        print(f"{host['ip']:<16}{host['mac']}")


if __name__ == "__main__":
    main()
