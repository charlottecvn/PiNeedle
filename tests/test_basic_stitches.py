"""Test basic knitting stitch patterns (garter, stockinette)."""

import pytest
from pineedle import (
    garter_pattern,
    stockinette_pattern,
    garter_stitch,  # backwards compatibility
    stockinette_stitch,  # backwards compatibility
    KnitPattern,
    KnitStitch,
    KnitChart,
)


class TestGarterStitch:
    """Test garter stitch pattern functionality."""

    def test_garter_stitch_creates_knit_chart(self):
        """Test that garter_pattern returns a KnitChart."""
        pattern = garter_pattern(8, 4)
        assert isinstance(pattern, KnitChart)
        assert len(pattern.rows) == 4
        assert all(len(row.stitches) == 8 for row in pattern.rows)

    def test_garter_stitch_all_knit_stitches(self):
        """Test that garter stitch contains only knit stitches."""
        pattern = garter_pattern(6, 3)

        for row in pattern.rows:
            for stitch in row.stitches:
                assert stitch == KnitStitch.K, (
                    "Garter stitch should only contain knit stitches"
                )

    def test_garter_stitch_alternates_rs_ws(self):
        """Test that garter stitch properly alternates RS/WS rows."""
        pattern = garter_pattern(4, 4)

        for i, row in enumerate(pattern.rows):
            if i % 2 == 0:  # Odd row numbers (1, 3, 5...) should be RS
                assert row.rs is True, f"Row {i + 1} should be RS"
            else:  # Even row numbers (2, 4, 6...) should be WS
                assert row.rs is False, f"Row {i + 1} should be WS"

    def test_garter_stitch_row_numbers(self):
        """Test that garter stitch has correct row numbering."""
        pattern = garter_pattern(4, 3)

        for i, row in enumerate(pattern.rows):
            assert row.row_number == i + 1, f"Row should be numbered {i + 1}"

    def test_garter_stitch_text_output(self):
        """Test that garter stitch produces appropriate text output."""
        pattern = garter_pattern(4, 2)
        text = pattern.as_text()

        assert "Row 1 (RS): k, k, k, k" in text
        assert "Row 2 (WS): k, k, k, k" in text

    def test_garter_stitch_default_dimensions(self):
        """Test garter stitch with default dimensions."""
        pattern = garter_pattern()
        assert len(pattern.rows) == 16  # default height
        assert all(len(row.stitches) == 24 for row in pattern.rows)  # default width

    def test_garter_stitch_custom_dimensions(self):
        """Test garter stitch with custom dimensions."""
        pattern = garter_pattern(width=10, height=5)
        assert len(pattern.rows) == 5
        assert all(len(row.stitches) == 10 for row in pattern.rows)


class TestStockinetteStitch:
    """Test stockinette stitch pattern functionality."""

    def test_stockinette_stitch_creates_knit_chart(self):
        """Test that stockinette_pattern returns a KnitChart."""
        pattern = stockinette_pattern(8, 4)
        assert isinstance(pattern, KnitChart)
        assert len(pattern.rows) == 4
        assert all(len(row.stitches) == 8 for row in pattern.rows)

    def test_stockinette_stitch_alternates_knit_purl(self):
        """Test that stockinette alternates knit and purl rows."""
        pattern = stockinette_pattern(6, 4)

        for i, row in enumerate(pattern.rows):
            if i % 2 == 0:  # RS rows should be all knit
                for stitch in row.stitches:
                    assert stitch == KnitStitch.K, f"RS row {i + 1} should be all knit"
            else:  # WS rows should be all purl
                for stitch in row.stitches:
                    assert stitch == KnitStitch.P, f"WS row {i + 1} should be all purl"

    def test_stockinette_stitch_rs_ws_designation(self):
        """Test that stockinette properly designates RS/WS rows."""
        pattern = stockinette_pattern(4, 4)

        for i, row in enumerate(pattern.rows):
            if i % 2 == 0:  # Odd row numbers should be RS
                assert row.rs is True, f"Row {i + 1} should be RS"
            else:  # Even row numbers should be WS
                assert row.rs is False, f"Row {i + 1} should be WS"

    def test_stockinette_stitch_text_output(self):
        """Test that stockinette produces appropriate text output."""
        pattern = stockinette_pattern(4, 2)
        text = pattern.as_text()

        assert "Row 1 (RS): k, k, k, k" in text
        assert "Row 2 (WS): p, p, p, p" in text

    def test_stockinette_stitch_default_dimensions(self):
        """Test stockinette with default dimensions."""
        pattern = stockinette_pattern()
        assert len(pattern.rows) == 16  # default height
        assert all(len(row.stitches) == 24 for row in pattern.rows)  # default width

    def test_stockinette_stitch_custom_dimensions(self):
        """Test stockinette with custom dimensions."""
        pattern = stockinette_pattern(width=12, height=6)
        assert len(pattern.rows) == 6
        assert all(len(row.stitches) == 12 for row in pattern.rows)


class TestKnitPatternStitchMethods:
    """Test KnitPattern fill methods for basic stitches."""

    def test_knit_pattern_fill_garter(self):
        """Test KnitPattern.fill_garter() method."""
        pattern = KnitPattern(6, 4)
        pattern.fill_garter()

        # All cells should be True (knit stitches)
        for row in pattern.grid:
            for cell in row:
                assert cell is True, "Garter stitch should fill all cells with True"

    def test_knit_pattern_fill_stockinette(self):
        """Test KnitPattern.fill_stockinette() method."""
        pattern = KnitPattern(6, 4)
        pattern.fill_stockinette()

        # RS rows (even indices) should be True, WS rows (odd indices) should be False
        for row_idx, row in enumerate(pattern.grid):
            for cell in row:
                if row_idx % 2 == 0:  # RS rows
                    assert cell is True, (
                        f"RS row {row_idx + 1} should have knit stitches (True)"
                    )
                else:  # WS rows
                    assert cell is False, (
                        f"WS row {row_idx + 1} should have purl stitches (False)"
                    )

    def test_knit_pattern_garter_text_detection(self):
        """Test that KnitPattern detects garter stitch in text output."""
        pattern = KnitPattern(4, 3)
        pattern.fill_garter()

        text = pattern.as_text()
        assert "Garter Pattern" in text
        assert "Knit every row" in text

    def test_knit_pattern_stockinette_text_detection(self):
        """Test that KnitPattern detects stockinette stitch in text output."""
        pattern = KnitPattern(4, 4)
        pattern.fill_stockinette()

        text = pattern.as_text()
        assert "Stockinette Pattern" in text
        assert "RS rows: Knit all stitches" in text
        assert "WS rows: Purl all stitches" in text


class TestBackwardsCompatibility:
    """Test backwards compatibility for deprecated function names."""

    def test_garter_stitch_backwards_compatibility(self):
        """Test that garter_stitch still works (backwards compatibility)."""
        pattern_old = garter_stitch(6, 3)
        pattern_new = garter_pattern(6, 3)

        # Both should return KnitChart
        assert isinstance(pattern_old, KnitChart)
        assert isinstance(pattern_new, KnitChart)

        # Both should have same dimensions
        assert len(pattern_old.rows) == len(pattern_new.rows)
        assert len(pattern_old.rows[0].stitches) == len(pattern_new.rows[0].stitches)

        # Both should produce same pattern
        for i, (old_row, new_row) in enumerate(zip(pattern_old.rows, pattern_new.rows)):
            assert old_row.stitches == new_row.stitches, f"Row {i} should match"
            assert old_row.rs == new_row.rs, f"Row {i} RS/WS should match"
            assert old_row.row_number == new_row.row_number, (
                f"Row {i} number should match"
            )

    def test_stockinette_stitch_backwards_compatibility(self):
        """Test that stockinette_stitch still works (backwards compatibility)."""
        pattern_old = stockinette_stitch(8, 4)
        pattern_new = stockinette_pattern(8, 4)

        # Both should return KnitChart
        assert isinstance(pattern_old, KnitChart)
        assert isinstance(pattern_new, KnitChart)

        # Both should have same dimensions
        assert len(pattern_old.rows) == len(pattern_new.rows)
        assert len(pattern_old.rows[0].stitches) == len(pattern_new.rows[0].stitches)

        # Both should produce same pattern
        for i, (old_row, new_row) in enumerate(zip(pattern_old.rows, pattern_new.rows)):
            assert old_row.stitches == new_row.stitches, f"Row {i} should match"
            assert old_row.rs == new_row.rs, f"Row {i} RS/WS should match"
            assert old_row.row_number == new_row.row_number, (
                f"Row {i} number should match"
            )

    def test_knit_pattern_with_gauge_shows_pattern_name(self):
        """Test that pattern name is shown even with gauge information."""
        pattern = KnitPattern(8, 4)
        pattern.set_gauge(1.8, 2.4, 4.5)
        pattern.fill_garter()

        text = pattern.as_text()
        assert "Pattern: Garter Pattern" in text
        assert "Gauge:" in text
        assert "Finished size:" in text


class TestStitchPatternComparisons:
    """Test comparisons between different stitch patterns."""

    def test_garter_vs_stockinette_structure(self):
        """Test structural differences between garter and stockinette."""
        garter = garter_stitch(6, 4)
        stockinette = stockinette_stitch(6, 4)

        # Both should have same dimensions
        assert len(garter.rows) == len(stockinette.rows)
        assert len(garter.rows[0].stitches) == len(stockinette.rows[0].stitches)

        # But different stitch patterns
        garter_text = garter.as_text()
        stockinette_text = stockinette.as_text()

        assert garter_text != stockinette_text
        assert "k, k, k, k, k, k" in garter_text  # All knit on all rows
        assert "p, p, p, p, p, p" in stockinette_text  # Purl on WS rows

    def test_pattern_recognition_accuracy(self):
        """Test that pattern recognition correctly identifies different patterns."""
        # Create patterns using KnitPattern fill methods
        garter_pattern = KnitPattern(4, 4)
        garter_pattern.fill_garter()

        stockinette_pattern = KnitPattern(4, 4)
        stockinette_pattern.fill_stockinette()

        checkerboard_pattern = KnitPattern(4, 4)
        checkerboard_pattern.fill_checkerboard()

        # Test pattern detection
        assert "Garter Pattern" in garter_pattern.as_text()
        assert "Stockinette Pattern" in stockinette_pattern.as_text()
        assert "Garter Pattern" not in checkerboard_pattern.as_text()
        assert "Stockinette Pattern" not in checkerboard_pattern.as_text()

    def test_single_row_patterns(self):
        """Test that single-row patterns are handled correctly."""
        single_garter = garter_stitch(6, 1)
        single_stockinette = stockinette_stitch(6, 1)

        assert len(single_garter.rows) == 1
        assert len(single_stockinette.rows) == 1

        # Single row should still be recognized
        assert all(stitch == KnitStitch.K for stitch in single_garter.rows[0].stitches)
        assert all(
            stitch == KnitStitch.K for stitch in single_stockinette.rows[0].stitches
        )


class TestStitchPatternIntegration:
    """Test integration of stitch patterns with other features."""

    def test_garter_with_gauge_calculations(self):
        """Test garter stitch pattern with gauge information."""
        pattern = KnitPattern(20, 10)
        pattern.set_gauge(1.8, 2.4, 4.5)
        pattern.fill_garter()

        text = pattern.as_text()

        # Should show pattern name, gauge, and size
        assert "Garter Pattern" in text
        assert "1.8 sts/cm" in text
        assert "2.4 rows/cm" in text
        assert "4.5mm" in text
        assert "Finished size:" in text

    def test_stockinette_with_metric_sizing(self):
        """Test stockinette with metric sizing calculations."""
        pattern = KnitPattern(36, 48)
        pattern.set_gauge(1.8, 2.4, 4.5)
        pattern.fill_stockinette()

        text = pattern.as_text()

        # Should calculate correct dimensions: 36/1.8 = 20cm, 48/2.4 = 20cm
        assert "20.0 × 20.0 cm" in text
        assert "Stockinette Pattern" in text

    def test_empty_pattern_handling(self):
        """Test handling of empty or invalid patterns."""
        empty_pattern = KnitPattern(0, 0)

        # Should not crash and should not detect a standard pattern
        text = empty_pattern.as_text()
        assert "Garter Stitch" not in text
        assert "Stockinette Stitch" not in text
