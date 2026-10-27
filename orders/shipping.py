"""Shipping fees."""

RATES = {"standard": 5.0, "express": 12.0}


def shipping_fee(method: str) -> float:
    """Fee for a shipping method; unknown methods fall back to standard."""
    return RATES[method.lower()]
