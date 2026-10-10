"""CLI entry point for the packet sniffer analyzer project."""

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Build and return the CLI argument parser."""
    parser = argparse.ArgumentParser(description="Packet sniffer and protocol analyzer")
    parser.add_argument("--list-interfaces", action="store_true", help="List available capture interfaces")
    parser.add_argument("-i", "--interface", type=str, help="Network interface for live capture")
    parser.add_argument("-c", "--count", type=int, default=0, help="Number of packets to capture")
    parser.add_argument("--timeout", type=int, help="Capture timeout in seconds")
    parser.add_argument("--protocol", type=str, help="Protocol filter (e.g., TCP, UDP, ICMP)")
    parser.add_argument("--ip", type=str, help="IP address filter")
    parser.add_argument("--port", type=int, help="Port filter")
    parser.add_argument("--save", type=str, help="Path to save captured packets as PCAP")
    parser.add_argument("--read", type=str, help="Path to a PCAP file to analyze")
    parser.add_argument("--stats", action="store_true", help="Show computed traffic statistics")
    return parser


def main() -> None:
    """Parse command-line arguments (logic not implemented yet)."""
    parser = build_parser()
    parser.parse_args()


if __name__ == "__main__":
    main()
