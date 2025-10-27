"""Metric sizing utilities for knitting needles and crochet hooks."""

from typing import Dict, List, Optional


class MetricNeedleSizes:
    """Standard metric knitting needle sizes in millimeters."""

    # Common metric needle sizes (mm)
    SIZES = [
        2.0,
        2.25,
        2.5,
        2.75,
        3.0,
        3.25,
        3.5,
        3.75,
        4.0,
        4.5,
        5.0,
        5.5,
        6.0,
        6.5,
        7.0,
        8.0,
        9.0,
        10.0,
        12.0,
        15.0,
        20.0,
        25.0,
    ]

    # Typical yarn weights and recommended needle sizes
    YARN_WEIGHT_RECOMMENDATIONS = {
        "lace": [2.0, 2.25, 2.5, 2.75, 3.25],
        "sport": [3.25, 3.5, 3.75, 4.0],
        "dk": [4.0, 4.5, 5.0],
        "worsted": [4.5, 5.0, 5.5],
        "aran": [5.0, 5.5, 6.0, 6.5],
        "chunky": [6.5, 8.0, 9.0, 10.0],
        "super_chunky": [10.0, 12.0, 15.0, 20.0, 25.0],
    }

    @classmethod
    def is_valid_size(cls, size_mm: float) -> bool:
        """Check if a needle size is valid."""
        return size_mm in cls.SIZES

    @classmethod
    def get_closest_size(cls, size_mm: float) -> float:
        """Get the closest standard needle size."""
        return min(cls.SIZES, key=lambda x: abs(x - size_mm))

    @classmethod
    def get_range_for_yarn(cls, yarn_weight: str) -> Optional[List[float]]:
        """Get recommended needle sizes for a yarn weight."""
        return cls.YARN_WEIGHT_RECOMMENDATIONS.get(yarn_weight.lower())


class MetricHookSizes:
    """Standard metric crochet hook sizes in millimeters."""

    # Common metric hook sizes (mm)
    SIZES = [
        2.0,
        2.25,
        2.5,
        2.75,
        3.0,
        3.25,
        3.5,
        3.75,
        4.0,
        4.5,
        5.0,
        5.5,
        6.0,
        6.5,
        7.0,
        8.0,
        9.0,
        10.0,
        12.0,
        15.0,
        19.0,
        25.0,
    ]

    # Typical yarn weights and recommended hook sizes
    YARN_WEIGHT_RECOMMENDATIONS = {
        "thread": [0.6, 0.75, 1.0, 1.25, 1.5, 1.75],
        "lace": [2.0, 2.25, 2.5, 2.75, 3.25],
        "sport": [3.5, 4.0, 4.5],
        "dk": [4.5, 5.0, 5.5],
        "worsted": [5.5, 6.0, 6.5],
        "aran": [6.5, 8.0, 9.0],
        "chunky": [9.0, 10.0, 12.0],
        "super_chunky": [12.0, 15.0, 19.0, 25.0],
    }

    @classmethod
    def is_valid_size(cls, size_mm: float) -> bool:
        """Check if a hook size is valid."""
        return size_mm in cls.SIZES

    @classmethod
    def get_closest_size(cls, size_mm: float) -> float:
        """Get the closest standard hook size."""
        return min(cls.SIZES, key=lambda x: abs(x - size_mm))

    @classmethod
    def get_range_for_yarn(cls, yarn_weight: str) -> Optional[List[float]]:
        """Get recommended hook sizes for a yarn weight."""
        return cls.YARN_WEIGHT_RECOMMENDATIONS.get(yarn_weight.lower())


class GaugeConverter:
    """Convert between different gauge measurements."""

    CM_TO_INCH = 2.54
    INCH_TO_CM = 1 / CM_TO_INCH

    @classmethod
    def stitches_per_inch_to_cm(cls, sts_per_inch: float) -> float:
        """Convert stitches per inch to stitches per cm."""
        return sts_per_inch * cls.INCH_TO_CM

    @classmethod
    def stitches_per_cm_to_inch(cls, sts_per_cm: float) -> float:
        """Convert stitches per cm to stitches per inch."""
        return sts_per_cm * cls.CM_TO_INCH

    @classmethod
    def rows_per_inch_to_cm(cls, rows_per_inch: float) -> float:
        """Convert rows per inch to rows per cm."""
        return rows_per_inch * cls.INCH_TO_CM

    @classmethod
    def rows_per_cm_to_inch(cls, rows_per_cm: float) -> float:
        """Convert rows per cm to rows per inch."""
        return rows_per_cm * cls.CM_TO_INCH


def get_gauge_info(yarn_weight: str, craft: str = "knit") -> Dict:
    """Get typical gauge information for a yarn weight and craft."""

    # Typical gauge ranges in stitches per cm
    knit_gauges = {
        "lace": (2.8, 4.0),  # 7-10 sts per inch
        "sport": (2.2, 2.8),  # 5.5-7 sts per inch
        "dk": (1.8, 2.2),  # 4.5-5.5 sts per inch
        "worsted": (1.6, 2.0),  # 4-5 sts per inch
        "aran": (1.4, 1.8),  # 3.5-4.5 sts per inch
        "chunky": (1.0, 1.4),  # 2.5-3.5 sts per inch
        "super_chunky": (0.4, 1.0),  # 1-2.5 sts per inch
    }

    crochet_gauges = {
        "thread": (3.2, 4.8),  # 8-12 sts per inch
        "lace": (2.4, 3.2),  # 6-8 sts per inch
        "sport": (2.0, 2.4),  # 5-6 sts per inch
        "dk": (1.6, 2.0),  # 4-5 sts per inch
        "worsted": (1.2, 1.6),  # 3-4 sts per inch
        "aran": (1.0, 1.4),  # 2.5-3.5 sts per inch
        "chunky": (0.8, 1.2),  # 2-3 sts per inch
        "super_chunky": (0.4, 0.8),  # 1-2 sts per inch
    }

    gauges = knit_gauges if craft.lower() == "knit" else crochet_gauges
    sizes_class = MetricNeedleSizes if craft.lower() == "knit" else MetricHookSizes

    if yarn_weight.lower() not in gauges:
        return {}

    gauge_range = gauges[yarn_weight.lower()]
    tool_sizes = sizes_class.get_range_for_yarn(yarn_weight)

    return {
        "yarn_weight": yarn_weight,
        "craft": craft,
        "gauge_range_sts_per_cm": gauge_range,
        "typical_gauge_sts_per_cm": sum(gauge_range) / 2,
        "tool_sizes_mm": tool_sizes or [],
        "recommended_tool_mm": tool_sizes[len(tool_sizes) // 2] if tool_sizes else None,
    }


def calculate_pattern_dimensions(
    width_stitches: int,
    height_rows: int,
    gauge_sts_per_cm: float,
    gauge_rows_per_cm: float,
) -> Dict[str, float]:
    """Calculate the physical dimensions of a pattern in centimeters."""

    width_cm = width_stitches / gauge_sts_per_cm
    height_cm = height_rows / gauge_rows_per_cm

    return {
        "width_cm": round(width_cm, 1),
        "height_cm": round(height_cm, 1),
        "width_stitches": width_stitches,
        "height_rows": height_rows,
        "gauge_sts_per_cm": gauge_sts_per_cm,
        "gauge_rows_per_cm": gauge_rows_per_cm,
    }


def suggest_pattern_size(
    desired_width_cm: float,
    desired_height_cm: float,
    gauge_sts_per_cm: float,
    gauge_rows_per_cm: float,
) -> Dict[str, int]:
    """Suggest pattern dimensions in stitches/rows for desired physical size."""

    width_stitches = round(desired_width_cm * gauge_sts_per_cm)
    height_rows = round(desired_height_cm * gauge_rows_per_cm)

    return {
        "width_stitches": width_stitches,
        "height_rows": height_rows,
        "actual_width_cm": round(width_stitches / gauge_sts_per_cm, 1),
        "actual_height_cm": round(height_rows / gauge_rows_per_cm, 1),
    }
