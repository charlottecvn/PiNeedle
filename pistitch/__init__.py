"""PiStitch package — knitting & crochet pattern generation."""

from .patterns import (
    Pattern,
    KnitPattern,
    CrochetPattern,
    Chart,
    KnitChart,
    CrochetChart,
    Stitch,
    KnitStitch,
    CrochetStitch,
    ChartRow,
    KnitChartRow,
    CrochetChartRow,
)
from .exporters import to_svg, to_ascii, to_png, to_pdf, to_text
from .recipes import (
    rib_pattern,
    seed_pattern,
    moss_pattern,
    granny_square,
    granny_square_chart,
    cable_swatch,
    single_crochet_rectangle,
    shell_stitch_pattern,
)
from .sizing import (
    MetricNeedleSizes,
    MetricHookSizes,
    GaugeConverter,
    get_gauge_info,
    calculate_pattern_dimensions,
    suggest_pattern_size,
)

__all__ = [
    # Pattern classes
    "Pattern",
    "KnitPattern",
    "CrochetPattern",
    # Chart classes
    "Chart",
    "KnitChart",
    "CrochetChart",
    # Stitch classes
    "Stitch",
    "KnitStitch",
    "CrochetStitch",
    # Row classes
    "ChartRow",
    "KnitChartRow",
    "CrochetChartRow",
    # Export functions
    "to_svg",
    "to_ascii",
    "to_png",
    "to_pdf",
    "to_text",
    # Knitting recipes
    "rib_pattern",
    "seed_pattern",
    "moss_pattern",
    "cable_swatch",
    # Crochet recipes
    "granny_square",
    "granny_square_chart",
    "single_crochet_rectangle",
    "shell_stitch_pattern",
    # Sizing utilities
    "MetricNeedleSizes",
    "MetricHookSizes",
    "GaugeConverter",
    "get_gauge_info",
    "calculate_pattern_dimensions",
    "suggest_pattern_size",
]
