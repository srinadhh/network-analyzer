"""Packet parsing utilities that convert packets into dictionaries."""

from typing import Any, Dict


def parse_packet(packet: Any) -> Dict[str, Any]:
    """Parse one packet into a serializable dictionary."""
    raise NotImplementedError
