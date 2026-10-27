"""Regression test for KeyError: 'customer_id' in serialize_order().

The store schema uses 'customer_ref' but serialize_order was reading 'customer_id'.
This test exercises the exact failing scenario from the traceback.
"""

import pytest
from orders.serializers import serialize_order
from orders import store


def test_serialize_order_reads_customer_ref():
    """serialize_order should read customer_ref from stored record and output customer_id."""
    # Create a record directly as the store would (using customer_ref)
    record = store.save_order("cust-123", [{"sku": "SKU-1", "qty": 1, "unit_price": 10.0}], None, 10.0)
    
    # This should not raise KeyError
    result = serialize_order(record)
    
    # Output field should be named customer_id with the correct value
    assert result["customer_id"] == "cust-123"
    assert result["id"] == record["id"]
    assert result["items"] == record["items"]
    assert result["total"] == record["total"]


def test_serialize_order_direct_dict():
    """Test serialize_order with a raw dict matching the store schema (customer_ref)."""
    record = {
        "id": 42,
        "customer_ref": "direct-customer",
        "items": [{"sku": "ABC", "qty": 2, "unit_price": 5.0}],
        "discount_code": "SAVE5",
        "total": 9.5,
    }
    
    result = serialize_order(record)
    
    assert result["customer_id"] == "direct-customer"
    assert result["id"] == 42
    assert result["discount_code"] == "SAVE5"
    assert result["total"] == 9.5
