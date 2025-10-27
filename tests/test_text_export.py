"""Test text export functionality for grid patterns."""

import pytest
from pistitch import (
    Pattern,
    KnitPattern,
    CrochetPattern,
    to_text,
)


class TestBasicPatternTextExport:
    """Test text export for basic Pattern class."""

    def test_pattern_has_as_text_method(self):
        """Test that Pattern class has as_text method."""
        pattern = Pattern(4, 3)
        assert hasattr(pattern, "as_text")
        text = pattern.as_text()
        assert isinstance(text, str)
        assert len(text) > 0

    def test_empty_pattern_text(self):
        """Test text export of empty pattern."""
        pattern = Pattern(4, 3)
        text = pattern.as_text()

        # Should describe all rows as background
        assert "All background" in text
        assert "Row 1:" in text
        assert "Row 3:" in text

    def test_filled_pattern_text(self):
        """Test text export of completely filled pattern."""
        pattern = Pattern(4, 3)
        # Fill all cells
        for y in range(3):
            for x in range(4):
                pattern.set_cell(x, y, True)

        text = pattern.as_text()
        assert "All stitches" in text

    def test_checkerboard_pattern_text(self):
        """Test text export of checkerboard pattern."""
        pattern = Pattern(4, 4)
        pattern.fill_checkerboard()

        text = pattern.as_text()
        # Should describe alternating pattern
        assert "stitches" in text
        assert "background" in text


class TestKnitPatternTextExport:
    """Test text export for KnitPattern class."""

    def test_knit_pattern_has_as_text_method(self):
        """Test that KnitPattern class has as_text method."""
        pattern = KnitPattern(4, 3)
        assert hasattr(pattern, "as_text")
        text = pattern.as_text()
        assert isinstance(text, str)

    def test_knit_pattern_uses_knitting_terminology(self):
        """Test that KnitPattern uses proper knitting terminology."""
        pattern = KnitPattern(4, 3)
        pattern.fill_checkerboard()

        text = pattern.as_text()
        # Should use knitting terms
        assert "RS" in text or "WS" in text  # Right/Wrong side
        assert "Row" in text

        # Should use knitting stitch abbreviations
        lines = text.split("\n")
        stitch_lines = [line for line in lines if "Row" in line and ":" in line]
        if stitch_lines:
            # Should contain k or p for knit/purl
            stitch_content = " ".join(stitch_lines)
            assert "k" in stitch_content or "p" in stitch_content

    def test_knit_pattern_with_gauge_info(self):
        """Test that KnitPattern includes gauge information in text."""
        pattern = KnitPattern(20, 15)
        pattern.set_gauge(1.8, 2.4, 4.5)
        pattern.fill_checkerboard()

        text = pattern.as_text()

        # Should include gauge information
        assert "Gauge:" in text
        assert "1.8" in text  # stitches per cm
        assert "2.4" in text  # rows per cm
        assert "4.5mm" in text  # needle size

        # Should include finished size
        assert "Finished size:" in text
        assert "cm" in text

    def test_knit_pattern_rs_ws_alternation(self):
        """Test that KnitPattern alternates RS/WS correctly."""
        pattern = KnitPattern(4, 4)
        text = pattern.as_text()

        lines = text.split("\n")
        row_lines = [line for line in lines if line.startswith("Row")]

        # Check that RS/WS alternate properly
        for i, line in enumerate(row_lines):
            if i % 2 == 0:  # Odd rows (1, 3, 5...) should be RS
                assert "(RS)" in line
            else:  # Even rows (2, 4, 6...) should be WS
                assert "(WS)" in line

    def test_knit_pattern_all_knit_row(self):
        """Test description of all-knit row."""
        pattern = KnitPattern(4, 2)
        # Fill all rows to create garter stitch (avoid stockinette detection)
        for y in range(2):
            for x in range(4):
                pattern.set_cell(x, y, True)

        text = pattern.as_text()
        assert "Garter Pattern" in text or "All knit" in text

    def test_knit_pattern_all_purl_row(self):
        """Test description of all-purl row."""
        pattern = KnitPattern(4, 2)
        # Leave first row empty (all purl)

        text = pattern.as_text()
        assert "All purl" in text


class TestCrochetPatternTextExport:
    """Test text export for CrochetPattern class."""

    def test_crochet_pattern_has_as_text_method(self):
        """Test that CrochetPattern class has as_text method."""
        pattern = CrochetPattern(4, 3)
        assert hasattr(pattern, "as_text")
        text = pattern.as_text()
        assert isinstance(text, str)

    def test_crochet_pattern_uses_crochet_terminology(self):
        """Test that CrochetPattern uses proper crochet terminology."""
        pattern = CrochetPattern(4, 3)
        pattern.fill_checkerboard()

        text = pattern.as_text()
        # Should use Row by default
        assert "Row" in text

        # Should use crochet stitch abbreviations
        lines = text.split("\n")
        stitch_lines = [line for line in lines if "Row" in line and ":" in line]
        if stitch_lines:
            stitch_content = " ".join(stitch_lines)
            assert "sc" in stitch_content or "ch" in stitch_content

    def test_crochet_pattern_with_rounds(self):
        """Test that CrochetPattern uses Rnd when worked in rounds."""
        pattern = CrochetPattern(4, 3)
        pattern.set_rounds(True)
        pattern.fill_checkerboard()

        text = pattern.as_text()
        # Should use Rnd instead of Row
        assert "Rnd" in text
        assert "Row" not in text or text.count("Rnd") > text.count("Row")

    def test_crochet_pattern_with_gauge_info(self):
        """Test that CrochetPattern includes gauge information in text."""
        pattern = CrochetPattern(16, 12)
        pattern.set_gauge(1.4, 1.6, 5.0)
        pattern.fill_checkerboard()

        text = pattern.as_text()

        # Should include gauge information
        assert "Gauge:" in text
        assert "1.4" in text  # stitches per cm
        assert "1.6" in text  # rows per cm
        assert "5.0mm" in text  # hook size

        # Should include finished size
        assert "Finished size:" in text
        assert "cm" in text

    def test_crochet_pattern_all_single_crochet(self):
        """Test description of all-single-crochet row."""
        pattern = CrochetPattern(4, 2)
        # Fill entire first row
        for x in range(4):
            pattern.set_cell(x, 0, True)

        text = pattern.as_text()
        assert "All single crochet" in text

    def test_crochet_pattern_all_chains(self):
        """Test description of all-chain row."""
        pattern = CrochetPattern(4, 2)
        # Leave first row empty (all chains)

        text = pattern.as_text()
        assert "All chains" in text


class TestTextExportFunction:
    """Test the to_text() export function."""

    def test_to_text_works_with_grid_patterns(self):
        """Test that to_text() works with grid patterns."""
        knit_pattern = KnitPattern(4, 3)
        knit_pattern.set_gauge(1.8, 2.4, 4.5)

        text = to_text(knit_pattern)
        assert isinstance(text, str)
        assert "Gauge:" in text
        assert "Row" in text

    def test_to_text_works_with_charts(self):
        """Test that to_text() works with chart patterns."""
        from pistitch import rib_pattern

        chart = rib_pattern(8, 4)
        text = to_text(chart)
        assert isinstance(text, str)
        assert "Row" in text
        assert "RS" in text or "WS" in text

    def test_to_text_fallback_for_unknown_patterns(self):
        """Test that to_text() has fallback for patterns without as_text."""

        class MockPattern:
            def __init__(self):
                self.width = 10
                self.height = 8

        mock_pattern = MockPattern()
        text = to_text(mock_pattern)
        assert "10 × 8" in text


class TestPatternComplexity:
    """Test text export with various pattern complexities."""

    def test_simple_stripe_pattern(self):
        """Test text export of simple stripe pattern."""
        pattern = KnitPattern(6, 4)
        pattern.set_gauge(1.8, 2.4, 4.5)

        # Create stripes: alternating filled/empty rows
        for x in range(6):
            pattern.set_cell(x, 0, True)  # Row 1: all knit
            # Row 2: all purl (empty)
            pattern.set_cell(x, 2, True)  # Row 3: all knit
            # Row 4: all purl (empty)

        text = pattern.as_text()
        # This pattern will be detected as stockinette stitch
        assert "Stockinette Pattern" in text or (
            "All knit" in text and "All purl" in text
        )

    def test_rib_pattern_simulation(self):
        """Test text export of rib-like pattern."""
        pattern = KnitPattern(8, 2)

        # Create 2x2 rib pattern
        for y in range(2):
            for x in range(8):
                if (x // 2) % 2 == 0:
                    pattern.set_cell(x, y, True)  # knit columns
                # else: purl columns (leave False)

        text = pattern.as_text()
        # Should describe the pattern alternation
        assert "k" in text.lower()
        assert "p" in text.lower()

    def test_checkerboard_detailed_description(self):
        """Test detailed description of checkerboard pattern."""
        pattern = KnitPattern(4, 4)
        pattern.fill_checkerboard()

        text = pattern.as_text()
        lines = text.split("\n")

        # Should have description for each row
        row_lines = [line for line in lines if line.startswith("Row")]
        assert len(row_lines) == 4

        # Each row should describe the alternating pattern
        for line in row_lines:
            assert "k" in line.lower() or "p" in line.lower()

    def test_pattern_with_different_stitch_counts(self):
        """Test pattern with varying stitch counts per row."""
        pattern = KnitPattern(6, 3)

        # Row 1: k2, p2, k2
        pattern.set_cell(0, 0, True)
        pattern.set_cell(1, 0, True)
        # 2, 3 are False (purl)
        pattern.set_cell(4, 0, True)
        pattern.set_cell(5, 0, True)

        text = pattern.as_text()

        # Should group consecutive stitches
        row1_line = [line for line in text.split("\n") if "Row 1" in line][0]
        # Should mention counts for multiple stitches
        assert "2" in row1_line  # k2 or p2


class TestMetricIntegration:
    """Test integration with metric sizing features."""

    def test_finished_size_calculation_accuracy(self):
        """Test that finished size calculations are accurate."""
        pattern = KnitPattern(36, 48)  # 36 stitches, 48 rows
        pattern.set_gauge(1.8, 2.4, 4.5)  # 1.8 sts/cm, 2.4 rows/cm

        text = pattern.as_text()

        # Should calculate: 36/1.8 = 20cm width, 48/2.4 = 20cm height
        assert "20.0 × 20.0 cm" in text

    def test_gauge_display_format(self):
        """Test that gauge is displayed in proper metric format."""
        pattern = KnitPattern(20, 15)
        pattern.set_gauge(1.8, 2.4, 4.5)

        text = pattern.as_text()

        # Should show metric units clearly
        assert "sts/cm" in text
        assert "rows/cm" in text
        assert "mm" in text

    def test_pattern_without_gauge_no_size_info(self):
        """Test that patterns without gauge don't show size info."""
        pattern = KnitPattern(20, 15)
        # Don't set gauge

        text = pattern.as_text()

        # Should not include gauge or size information
        assert "Gauge:" not in text
        assert "Finished size:" not in text
        assert "cm" not in text
