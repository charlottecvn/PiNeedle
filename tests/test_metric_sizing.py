"""Test metric sizing utilities and European conventions."""

import pytest
from pistitch import (
    MetricNeedleSizes,
    MetricHookSizes,
    GaugeConverter,
    get_gauge_info,
    calculate_pattern_dimensions,
    suggest_pattern_size,
    KnitPattern,
    CrochetPattern,
)


class TestMetricNeedleSizes:
    """Test metric knitting needle size utilities."""

    def test_common_needle_sizes_available(self):
        """Test that common metric needle sizes are available."""
        expected_sizes = [2.0, 2.25, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 6.0, 8.0]

        for size in expected_sizes:
            assert size in MetricNeedleSizes.SIZES

    def test_is_valid_size(self):
        """Test needle size validation."""
        assert MetricNeedleSizes.is_valid_size(4.5) is True
        assert MetricNeedleSizes.is_valid_size(4.6) is False  # Not standard
        assert MetricNeedleSizes.is_valid_size(2.0) is True
        assert MetricNeedleSizes.is_valid_size(25.0) is True

    def test_get_closest_size(self):
        """Test finding closest standard needle size."""
        assert MetricNeedleSizes.get_closest_size(4.6) == 4.5
        assert MetricNeedleSizes.get_closest_size(4.4) == 4.5
        assert MetricNeedleSizes.get_closest_size(2.1) == 2.0
        assert MetricNeedleSizes.get_closest_size(7.8) == 8.0

    def test_yarn_weight_recommendations(self):
        """Test that yarn weight recommendations exist."""
        dk_needles = MetricNeedleSizes.get_range_for_yarn("dk")
        assert dk_needles is not None
        assert len(dk_needles) > 0
        assert all(isinstance(size, (int, float)) for size in dk_needles)

        # Test case insensitive
        worsted_needles = MetricNeedleSizes.get_range_for_yarn("WORSTED")
        assert worsted_needles is not None

        # Test invalid yarn weight
        invalid = MetricNeedleSizes.get_range_for_yarn("invalid_weight")
        assert invalid is None


class TestMetricHookSizes:
    """Test metric crochet hook size utilities."""

    def test_common_hook_sizes_available(self):
        """Test that common metric hook sizes are available."""
        expected_sizes = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 8.0]

        for size in expected_sizes:
            assert size in MetricHookSizes.SIZES

    def test_is_valid_size(self):
        """Test hook size validation."""
        assert MetricHookSizes.is_valid_size(5.0) is True
        assert MetricHookSizes.is_valid_size(5.1) is False  # Not standard
        assert MetricHookSizes.is_valid_size(2.0) is True
        assert MetricHookSizes.is_valid_size(25.0) is True

    def test_get_closest_size(self):
        """Test finding closest standard hook size."""
        assert MetricHookSizes.get_closest_size(5.1) == 5.0
        assert MetricHookSizes.get_closest_size(4.9) == 5.0
        assert MetricHookSizes.get_closest_size(2.1) == 2.0
        assert MetricHookSizes.get_closest_size(7.8) == 8.0

    def test_yarn_weight_recommendations(self):
        """Test that yarn weight recommendations exist."""
        dk_hooks = MetricHookSizes.get_range_for_yarn("dk")
        assert dk_hooks is not None
        assert len(dk_hooks) > 0
        assert all(isinstance(size, (int, float)) for size in dk_hooks)


class TestGaugeConverter:
    """Test gauge conversion utilities."""

    def test_stitches_per_inch_to_cm(self):
        """Test conversion from stitches per inch to cm."""
        # 4.5 stitches per inch ≈ 1.77 stitches per cm
        result = GaugeConverter.stitches_per_inch_to_cm(4.5)
        assert abs(result - 1.77) < 0.01

        # Test with different values
        result = GaugeConverter.stitches_per_inch_to_cm(6.0)
        assert abs(result - 2.36) < 0.01

    def test_stitches_per_cm_to_inch(self):
        """Test conversion from stitches per cm to inch."""
        # 1.8 stitches per cm ≈ 4.57 stitches per inch
        result = GaugeConverter.stitches_per_cm_to_inch(1.8)
        assert abs(result - 4.57) < 0.01

    def test_rows_per_inch_to_cm(self):
        """Test conversion from rows per inch to cm."""
        result = GaugeConverter.rows_per_inch_to_cm(6.0)
        assert abs(result - 2.36) < 0.01

    def test_rows_per_cm_to_inch(self):
        """Test conversion from rows per cm to inch."""
        result = GaugeConverter.rows_per_cm_to_inch(2.4)
        assert abs(result - 6.10) < 0.01

    def test_conversion_roundtrip(self):
        """Test that converting back and forth gives original value."""
        original = 4.5
        converted = GaugeConverter.stitches_per_inch_to_cm(original)
        back = GaugeConverter.stitches_per_cm_to_inch(converted)
        assert abs(back - original) < 0.001


class TestGaugeInfo:
    """Test gauge information utilities."""

    def test_get_gauge_info_knitting(self):
        """Test getting gauge info for knitting."""
        info = get_gauge_info("dk", "knit")

        assert info["yarn_weight"] == "dk"
        assert info["craft"] == "knit"
        assert "gauge_range_sts_per_cm" in info
        assert "typical_gauge_sts_per_cm" in info
        assert "tool_sizes_mm" in info
        assert "recommended_tool_mm" in info

        # Check that gauge is reasonable for DK weight
        gauge = info["typical_gauge_sts_per_cm"]
        assert 1.5 <= gauge <= 2.5  # Reasonable range for DK knitting

    def test_get_gauge_info_crochet(self):
        """Test getting gauge info for crochet."""
        info = get_gauge_info("dk", "crochet")

        assert info["yarn_weight"] == "dk"
        assert info["craft"] == "crochet"
        assert "gauge_range_sts_per_cm" in info

        # Crochet gauge should be different from knitting
        knit_info = get_gauge_info("dk", "knit")
        assert info["typical_gauge_sts_per_cm"] != knit_info["typical_gauge_sts_per_cm"]

    def test_get_gauge_info_invalid_yarn(self):
        """Test with invalid yarn weight."""
        info = get_gauge_info("invalid_yarn", "knit")
        assert info == {}

    def test_different_yarn_weights_have_different_gauges(self):
        """Test that different yarn weights have different typical gauges."""
        lace_info = get_gauge_info("lace", "knit")
        chunky_info = get_gauge_info("chunky", "knit")

        # Lace should have much finer gauge than chunky
        assert (
            lace_info["typical_gauge_sts_per_cm"]
            > chunky_info["typical_gauge_sts_per_cm"]
        )


class TestPatternDimensions:
    """Test pattern dimension calculations."""

    def test_calculate_pattern_dimensions(self):
        """Test calculating physical dimensions from pattern specs."""
        dimensions = calculate_pattern_dimensions(
            width_stitches=36,
            height_rows=48,
            gauge_sts_per_cm=1.8,
            gauge_rows_per_cm=2.4,
        )

        assert dimensions["width_cm"] == 20.0  # 36 / 1.8
        assert dimensions["height_cm"] == 20.0  # 48 / 2.4
        assert dimensions["width_stitches"] == 36
        assert dimensions["height_rows"] == 48
        assert dimensions["gauge_sts_per_cm"] == 1.8
        assert dimensions["gauge_rows_per_cm"] == 2.4

    def test_suggest_pattern_size(self):
        """Test suggesting pattern size for desired dimensions."""
        suggested = suggest_pattern_size(
            desired_width_cm=20.0,
            desired_height_cm=15.0,
            gauge_sts_per_cm=1.8,
            gauge_rows_per_cm=2.4,
        )

        assert suggested["width_stitches"] == 36  # 20.0 * 1.8
        assert suggested["height_rows"] == 36  # 15.0 * 2.4
        assert suggested["actual_width_cm"] == 20.0
        assert suggested["actual_height_cm"] == 15.0

    def test_dimension_rounding(self):
        """Test that dimensions are properly rounded."""
        # Test with values that need rounding
        dimensions = calculate_pattern_dimensions(
            width_stitches=37,  # 37 / 1.8 = 20.555...
            height_rows=47,  # 47 / 2.4 = 19.583...
            gauge_sts_per_cm=1.8,
            gauge_rows_per_cm=2.4,
        )

        assert dimensions["width_cm"] == 20.6  # Rounded to 1 decimal
        assert dimensions["height_cm"] == 19.6  # Rounded to 1 decimal


class TestMetricPatternIntegration:
    """Test integration of metric features with pattern classes."""

    def test_knit_pattern_metric_gauge(self):
        """Test that KnitPattern properly stores metric gauge."""
        pattern = KnitPattern(20, 15)
        pattern.set_gauge(1.8, 2.4, 4.5)

        assert pattern.gauge_stitches == 1.8
        assert pattern.gauge_rows == 2.4
        assert pattern.needle_size_mm == 4.5

    def test_crochet_pattern_metric_gauge(self):
        """Test that CrochetPattern properly stores metric gauge."""
        pattern = CrochetPattern(20, 15)
        pattern.set_gauge(1.4, 1.6, 5.0)

        assert pattern.gauge_stitches == 1.4
        assert pattern.gauge_rows == 1.6
        assert pattern.hook_size_mm == 5.0

    def test_pattern_physical_dimensions(self):
        """Test calculating physical dimensions from pattern with gauge."""
        pattern = KnitPattern(36, 48)
        pattern.set_gauge(1.8, 2.4, 4.5)

        # Calculate what the physical dimensions would be
        width_cm = pattern.width / pattern.gauge_stitches
        height_cm = pattern.height / pattern.gauge_rows

        assert abs(width_cm - 20.0) < 0.1
        assert abs(height_cm - 20.0) < 0.1

    def test_metric_gauge_is_different_from_imperial(self):
        """Test that metric gauge values are clearly different from imperial."""
        # Typical DK knitting gauge
        metric_gauge = 1.8  # sts per cm

        # This should be clearly different from imperial (typically 4-5 sts per inch)
        assert metric_gauge < 3.0, "Metric gauge should be much smaller than imperial"

        # Convert to imperial for comparison
        imperial_gauge = GaugeConverter.stitches_per_cm_to_inch(metric_gauge)
        assert 4.0 <= imperial_gauge <= 5.0, (
            "Should convert to reasonable imperial gauge"
        )


class TestMetricConventions:
    """Test that the package follows metric conventions properly."""

    def test_all_sizes_use_millimeters(self):
        """Test that all tool sizes are in millimeters."""
        # All needle sizes should be reasonable mm values
        for size in MetricNeedleSizes.SIZES:
            assert 1.0 <= size <= 30.0, f"Needle size {size}mm seems unreasonable"

        # All hook sizes should be reasonable mm values
        for size in MetricHookSizes.SIZES:
            assert 1.0 <= size <= 30.0, f"Hook size {size}mm seems unreasonable"

    def test_gauge_units_are_per_cm(self):
        """Test that gauge is consistently measured per cm."""
        info = get_gauge_info("dk", "knit")
        gauge = info.get("typical_gauge_sts_per_cm", 0)

        # Gauge per cm should be reasonable (not per inch values)
        assert 0.5 <= gauge <= 5.0, "Gauge per cm should be in reasonable range"

        # Should be much smaller than typical per-inch values
        assert gauge < 10.0, "Gauge per cm should be much less than per-inch"

    def test_european_sizing_philosophy(self):
        """Test that the package follows European/metric philosophy."""
        # Needle sizes should include European standard sizes
        european_sizes = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 7.0, 8.0]

        for eu_size in european_sizes:
            assert eu_size in MetricNeedleSizes.SIZES, (
                f"Missing European size {eu_size}mm"
            )
