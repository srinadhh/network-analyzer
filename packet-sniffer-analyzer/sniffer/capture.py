"""Packet capture helpers for live sniffing and PCAP file I/O."""

from typing import Any, List, Optional


def start_capture(interface: Optional[str] = None, count: int = 0, timeout: Optional[int] = None) -> List[Any]:
    """Start live packet capture and return captured packets."""
    raise NotImplementedError


def read_pcap(path: str) -> List[Any]:
    """Read packets from a PCAP file."""
    raise NotImplementedError


def save_pcap(packets: List[Any], path: str) -> None:
    """Save packets to a PCAP file."""
    raise NotImplementedError
