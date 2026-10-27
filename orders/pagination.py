"""Page-number pagination helpers."""

import math


def paginate(items: list[dict], page: int | str, size: int) -> dict:
    """Return one page of ``items``. Pages are 1-based; ``page="last"`` means the final page."""
    pages = max(1, math.ceil(len(items) / size))
    if page == "last":
        page = pages
    page = int(page)
    # Clamp page to valid range
    page = max(1, min(page, pages))
    start = (page - 1) * size
    chunk = items[start:start + size]
    first_id = chunk[0]["id"] if chunk else None
    return {
        "page": page,
        "pages": pages,
        "first_id": first_id,
        "items": chunk,
    }
