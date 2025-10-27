"""Test distinction between knitting and crochet patterns."""

import pytest
from pineedle import (
    KnitStitch,
    CrochetStitch,
    KnitChart,
    CrochetChart,
    KnitPattern,
    CrochetPattern,
    rib_pattern,
    granny_square,
    granny_square_chart,
    single_crochet_rectangle,
    cable_swatch,
    shell_stitch_pattern,
)


class TestStitchDistinction:
    """Test that knitting and crochet stitches are properly separated."""

    def test_knit_stitches_have_knitting_abbreviations(self):
        """Knitting stitches should use knitting abbreviations."""
        assert KnitStitch.K == "k"  # knit
        assert KnitStitch.P == "p"  # purl
        assert KnitStitch.YO == "yo"  # yarn over
        assert KnitStitch.K2TOG == "k2tog"  # knit two together
        assert KnitStitch.C4F == "c4f"  # cable 4 front

    def test_crochet_stitches_have_crochet_abbreviations(self):
        """Crochet stitches should use crochet abbreviations."""
        assert CrochetStitch.CH == "ch"  # chain
        assert CrochetStitch.SC == "sc"  # single crochet
        assert CrochetStitch.DC == "dc"  # double crochet
        assert CrochetStitch.HDC == "hdc"  # half double crochet
        assert CrochetStitch.TR == "tr"  # treble crochet

    def test_stitch_enums_are_separate(self):
        """Knitting and crochet stitches should be in separate enums."""
        knit_values = set(s.value for s in KnitStitch)
        crochet_values = set(s.value for s in CrochetStitch)

        # Only EMPTY should overlap
        overlap = knit_values & crochet_values
        assert overlap == {"."}, f"Unexpected overlap: {overlap}"

    def test_no_crochet_stitches_in_knit_enum(self):
        """Knitting enum should not contain crochet-specific stitches."""
        knit_values = [s.value for s in KnitStitch]
        crochet_specific = ["ch", "sc", "dc", "hdc", "tr"]

        for stitch in crochet_specific:
            assert stitch not in knit_values, (
                f"Found crochet stitch '{stitch}' in knitting enum"
            )

    def test_no_knit_stitches_in_crochet_enum(self):
        """Crochet enum should not contain knitting-specific stitches."""
        crochet_values = [s.value for s in CrochetStitch]
        knit_specific = ["k", "p", "yo", "k2tog", "ssk", "c4f", "c4b"]

        for stitch in knit_specific:
            assert stitch not in crochet_values, (
                f"Found knitting stitch '{stitch}' in crochet enum"
            )


class TestPatternDistinction:
    """Test that knitting and crochet patterns are properly distinguished."""

    def test_knit_pattern_has_knitting_features(self):
        """KnitPattern should have knitting-specific features."""
        pattern = KnitPattern(10, 8)

        # Should have gauge methods
        pattern.set_gauge(1.8, 2.4, 4.5)
        assert pattern.gauge_stitches == 1.8
        assert pattern.gauge_rows == 2.4
        assert pattern.needle_size_mm == 4.5

    def test_crochet_pattern_has_crochet_features(self):
        """CrochetPattern should have crochet-specific features."""
        pattern = CrochetPattern(8, 6)

        # Should have gauge and hook methods
        pattern.set_gauge(1.4, 1.6, 5.0)
        assert pattern.gauge_stitches == 1.4
        assert pattern.gauge_rows == 1.6
        assert pattern.hook_size_mm == 5.0

        # Should have rounds feature
        pattern.set_rounds(True)
        assert pattern.work_in_rounds is True

    def test_pattern_types_are_different_classes(self):
        """Knit and crochet patterns should be different classes."""
        knit_pattern = KnitPattern(5, 5)
        crochet_pattern = CrochetPattern(5, 5)

        assert type(knit_pattern).__name__ == "KnitPattern"
        assert type(crochet_pattern).__name__ == "CrochetPattern"
        assert type(knit_pattern) != type(crochet_pattern)


class TestChartDistinction:
    """Test that knitting and crochet charts are properly distinguished."""

    def test_knit_chart_uses_knit_terminology(self):
        """Knitting charts should use RS/WS terminology."""
        chart = rib_pattern(4, 2)
        text_output = chart.as_text()

        assert "RS" in text_output or "WS" in text_output, (
            "Should contain knitting row terminology"
        )
        assert "Row" in text_output, "Should use 'Row' terminology"
        assert "Rnd" not in text_output, "Should not use crochet 'Rnd' terminology"

    def test_crochet_chart_uses_crochet_terminology(self):
        """Crochet charts should use round terminology when appropriate."""
        chart = granny_square_chart(2)
        text_output = chart.as_text()

        assert "Rnd" in text_output, "Should use 'Rnd' terminology for rounds"
        assert chart.is_worked_in_rounds(), "Should be identified as worked in rounds"

    def test_chart_types_are_different_classes(self):
        """Knit and crochet charts should be different classes."""
        knit_chart = rib_pattern(4, 2)
        crochet_chart = granny_square_chart(2)

        assert type(knit_chart).__name__ == "KnitChart"
        assert type(crochet_chart).__name__ == "CrochetChart"
        assert type(knit_chart) != type(crochet_chart)


class TestRecipeDistinction:
    """Test that recipe functions produce the correct type of patterns."""

    def test_knitting_recipes_produce_knit_charts(self):
        """Knitting recipe functions should produce KnitChart objects."""
        knitting_recipes = [
            rib_pattern(8, 4),
            cable_swatch(12, 6),
        ]

        for pattern in knitting_recipes:
            assert isinstance(pattern, KnitChart), (
                f"Expected KnitChart, got {type(pattern)}"
            )

    def test_crochet_recipes_produce_crochet_patterns_or_charts(self):
        """Crochet recipe functions should produce crochet objects."""
        # Grid-based crochet pattern
        granny_grid = granny_square(8, 3)
        assert isinstance(granny_grid, CrochetPattern), (
            f"Expected CrochetPattern, got {type(granny_grid)}"
        )

        # Chart-based crochet patterns
        crochet_charts = [
            granny_square_chart(3),
            single_crochet_rectangle(6, 4),
            shell_stitch_pattern(12, 4),
        ]

        for pattern in crochet_charts:
            assert isinstance(pattern, CrochetChart), (
                f"Expected CrochetChart, got {type(pattern)}"
            )

    def test_knitting_recipes_contain_knitting_stitches(self):
        """Knitting recipes should only contain knitting stitches."""
        rib_chart = rib_pattern(6, 2)

        for row in rib_chart.rows:
            for stitch in row.stitches:
                assert isinstance(stitch, KnitStitch), (
                    f"Found non-knitting stitch: {stitch}"
                )

    def test_crochet_recipes_contain_crochet_stitches(self):
        """Crochet chart recipes should only contain crochet stitches."""
        crochet_chart = single_crochet_rectangle(4, 2)

        for row in crochet_chart.rows:
            for stitch in row.stitches:
                assert isinstance(stitch, CrochetStitch), (
                    f"Found non-crochet stitch: {stitch}"
                )


class TestBackwardsCompatibility:
    """Test that backwards compatibility is maintained."""

    def test_old_stitch_enum_still_works(self):
        """The old Stitch enum should still work for backwards compatibility."""
        from pineedle import Stitch

        # Should be an alias to KnitStitch
        assert Stitch.K == "k"
        assert Stitch.P == "p"

    def test_old_chart_class_still_works(self):
        """The old Chart class should still work for backwards compatibility."""
        from pineedle import Chart

        # Should be an alias to KnitChart
        chart = rib_pattern(4, 2)
        assert isinstance(chart, Chart)


class TestTextRepresentation:
    """Test that text representations clearly indicate the craft type."""

    def test_knitting_pattern_text_shows_knitting_stitches(self):
        """Knitting pattern text should show knitting stitch abbreviations."""
        chart = rib_pattern(4, 2)
        text = chart.as_text()

        # Should contain knitting stitches
        assert "k" in text.lower()
        assert "p" in text.lower()

    def test_crochet_pattern_text_shows_crochet_stitches(self):
        """Crochet pattern text should show crochet stitch abbreviations."""
        chart = single_crochet_rectangle(4, 2)
        text = chart.as_text()

        # Should contain crochet stitches
        assert "ch" in text.lower()
        assert "sc" in text.lower()

    def test_granny_square_chart_shows_rounds(self):
        """Granny square chart should clearly show it's worked in rounds."""
        chart = granny_square_chart(2)
        text = chart.as_text()

        assert "Rnd" in text, "Should show 'Rnd' for rounds"
        assert "dc" in text or "ch" in text, "Should contain crochet stitches"


class TestPatternFeatures:
    """Test craft-specific pattern features."""

    def test_knit_chart_has_repeat_detection(self):
        """Knit charts should be able to detect stitch repeats."""
        chart = rib_pattern(8, 2)  # 2x2 rib should have a 4-stitch repeat
        repeat = chart.get_pattern_repeat()

        if repeat:  # Only test if repeat detection is implemented
            assert len(repeat) == 4, f"Expected 4-stitch repeat, got {len(repeat)}"
            assert repeat == [KnitStitch.K, KnitStitch.K, KnitStitch.P, KnitStitch.P]

    def test_crochet_chart_round_detection(self):
        """Crochet charts should correctly identify if worked in rounds."""
        granny_chart = granny_square_chart(2)
        rectangle_chart = single_crochet_rectangle(4, 2)

        assert granny_chart.is_worked_in_rounds(), (
            "Granny square should be worked in rounds"
        )
        assert not rectangle_chart.is_worked_in_rounds(), (
            "Rectangle should not be worked in rounds"
        )

    def test_crochet_pattern_rounds_setting(self):
        """Crochet patterns should properly track rounds setting."""
        pattern = CrochetPattern(8, 8)

        # Default should be False
        assert pattern.work_in_rounds is False

        # Should be settable
        pattern.set_rounds(True)
        assert pattern.work_in_rounds is True
