"""Traffic statistics helpers for protocol distribution and traffic trends."""

from typing import Any, Dict, Iterable, List, Tuple


def protocol_distribution(packets: Iterable[Any]) -> Dict[str, int]:
    """Compute packet counts grouped by protocol."""
    raise NotImplementedError


def top_talkers(packets: Iterable[Any], limit: int = 10) -> List[Tuple[str, int]]:
    """Return top source/destination talkers by packet count."""
    raise NotImplementedError


def packets_per_second(packets: Iterable[Any]) -> Dict[int, int]:
    """Compute packet rate over time in packets per second."""
    raise NotImplementedError
