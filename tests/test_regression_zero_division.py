import pytest
from orders.stats import average_order_value


def test_average_order_value_empty_list():
    """Test that average_order_value returns 0.0 for empty list instead of ZeroDivisionError."""
    assert average_order_value([]) == 0.0


def test_average_order_value_with_orders():
    """Test that average_order_value calculates correctly for non-empty list."""
    orders = [
        {"total": 100.0},
        {"total": 200.0},
        {"total": 300.0},
    ]
    assert average_order_value(orders) == 200.0
