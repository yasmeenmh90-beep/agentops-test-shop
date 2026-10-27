"""Order statistics."""


def average_order_value(orders: list[dict]) -> float:
    """Average total across orders; 0.0 when there are no orders."""
    if not orders:
        return 0.0
    return round(sum(o["total"] for o in orders) / len(orders), 2)
