"""Regression test for customer_ref vs customer_id schema mismatch.

The store saves the customer reference under 'customer_ref' but the serializer
was reading 'customer_id', causing a KeyError on GET /orders/<id>.
"""

import pytest
from fastapi.testclient import TestClient

from orders import store
from orders.main import app

client = TestClient(app)


@pytest.fixture(autouse=True)
def fresh_store():
    store.reset(seed=0)
    yield


def test_get_order_returns_customer_id_from_customer_ref():
    """GET /orders/<id> should return customer_id using the stored customer_ref."""
    record = store.save_order("cust-123", [{"sku": "A", "qty": 1, "unit_price": 5.0}], None, 5.0)
    r = client.get(f"/orders/{record['id']}")
    assert r.status_code == 200
    assert r.json()["customer_id"] == "cust-123"
