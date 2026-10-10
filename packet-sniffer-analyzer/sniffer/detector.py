"""Anomaly detection placeholders for port-scan and ARP spoof checks."""

from typing import Any, Dict, Iterable


def detect_port_scan(packets: Iterable[Any]) -> Dict[str, Any]:
    """Detect potential port-scan behavior from captured packets."""
    raise NotImplementedError


def detect_arp_spoof(packets: Iterable[Any]) -> Dict[str, Any]:
    """Detect potential ARP spoofing behavior from captured packets."""
    raise NotImplementedError
