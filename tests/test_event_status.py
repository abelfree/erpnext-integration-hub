def next_status(retries: int) -> str:
    return "failed" if retries >= 3 else "pending"


def test_next_status():
    assert next_status(1) == "pending"
    assert next_status(3) == "failed"
