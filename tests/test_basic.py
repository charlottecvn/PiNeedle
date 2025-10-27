from pistitch import KnitPattern
from pistitch.exporters import to_ascii


def test_checkerboard_ascii_contains_hashes_and_dots():
    p = KnitPattern(width=4, height=3)
    p.fill_checkerboard()
    s = to_ascii(p)
    assert "#" in s
    assert "." in s
    rows = s.splitlines()
    assert len(rows) == 3
    assert all(len(r) == 4 for r in rows)
