"""Shared utilities for logging, privilege checks, and helper functions."""

import logging


def setup_logging(level: int = logging.INFO) -> logging.Logger:
    """Configure and return the project logger."""
    raise NotImplementedError


def is_admin() -> bool:
    """Return whether the current process has elevated privileges."""
    raise NotImplementedError
