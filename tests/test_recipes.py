from pistitch.recipes import rib_pattern, seed_pattern, moss_pattern, cable_swatch
from pistitch.patterns import Stitch


def test_rib_pattern_counts():
    c = rib_pattern(8, 2)
    assert len(c.rows) == 2
    assert all(len(r.stitches) == 8 for r in c.rows)
    assert "k" in c.as_text()


def test_seed_pattern_alternates():
    c = seed_pattern(4, 2)
    text = c.as_text()
    assert "p" in text and "k" in text


def test_cable_pattern_has_knit_block():
    c = cable_swatch(12, 4, 4)
    assert any(Stitch.K in r.stitches for r in c.rows)
