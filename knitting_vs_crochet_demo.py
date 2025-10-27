#!/usr/bin/env python3
"""
Demonstration of distinctions between knitting and crochet in pineedle.
"""

import pineedle


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 60)
    print(f" {title}")
    print("=" * 60)


def demonstrate_stitch_distinctions():
    """Show how knitting and crochet stitches are properly separated."""
    print_section("STITCH DISTINCTIONS")

    print(" KNITTING STITCHES:")
    print("   These are specific to knitting and use knitting abbreviations:")
    knit_stitches = [
        ("k", "knit stitch"),
        ("p", "purl stitch"),
        ("yo", "yarn over (increase)"),
        ("k2tog", "knit two together (decrease)"),
        ("ssk", "slip, slip, knit (decrease)"),
        ("c4f", "cable 4 front"),
        ("c4b", "cable 4 back"),
        ("m1", "make one (increase)"),
    ]

    for abbrev, description in knit_stitches:
        print(f"   • {abbrev:<6} = {description}")

    print("\n CROCHET STITCHES:")
    print("   These are specific to crochet and use crochet abbreviations:")
    crochet_stitches = [
        ("ch", "chain"),
        ("sc", "single crochet"),
        ("dc", "double crochet"),
        ("hdc", "half double crochet"),
        ("tr", "treble crochet"),
        ("sl", "slip stitch"),
        ("inc", "increase"),
        ("dec", "decrease"),
        ("blo", "back loop only"),
        ("flo", "front loop only"),
    ]

    for abbrev, description in crochet_stitches:
        print(f"   • {abbrev:<6} = {description}")

    print(f"\nTotal knitting stitches: {len(list(pineedle.KnitStitch))}")
    print(f"Total crochet stitches: {len(list(pineedle.CrochetStitch))}")
    print("No overlap except for EMPTY marker")


def demonstrate_pattern_types():
    """Show different pattern types for knitting vs crochet."""
    print_section("PATTERN TYPE DISTINCTIONS")

    print(" KNITTING PATTERNS:")

    # Knitting grid pattern with gauge
    knit_pattern = pineedle.KnitPattern(10, 8)
    knit_pattern.set_gauge(1.8, 2.4, 4.5)  # 1.8 sts/cm, 2.4 rows/cm, 4.5mm needles

    print(f"   Grid Pattern: {type(knit_pattern).__name__}")
    print(f"   • Gauge: {knit_pattern.gauge_stitches} stitches per cm")
    print(f"   • Row gauge: {knit_pattern.gauge_rows} rows per cm")
    print(f"   • Needle size: {knit_pattern.needle_size_mm}mm")

    # Knitting chart pattern
    rib_chart = pineedle.rib_pattern(8, 4)
    print(f"   Chart Pattern: {type(rib_chart).__name__}")
    print("   • Uses knitting row terminology (RS/WS)")
    print("   • Contains knitting stitches (k, p)")

    print("\n CROCHET PATTERNS:")

    # Crochet grid pattern with gauge and rounds
    crochet_pattern = pineedle.CrochetPattern(8, 8)
    crochet_pattern.set_gauge(1.4, 1.6, 5.0)  # 1.4 sts/cm, 1.6 rows/cm, 5.0mm hook
    crochet_pattern.set_rounds(True)  # Worked in rounds

    print(f"   Grid Pattern: {type(crochet_pattern).__name__}")
    print(f"   • Gauge: {crochet_pattern.gauge_stitches} stitches per cm")
    print(f"   • Row gauge: {crochet_pattern.gauge_rows} rows per cm")
    print(f"   • Hook size: {crochet_pattern.hook_size_mm}mm")
    print(f"   • Worked in rounds: {crochet_pattern.work_in_rounds}")

    # Crochet chart patterns
    granny_chart = pineedle.granny_square_chart(3)
    rect_chart = pineedle.single_crochet_rectangle(6, 4)

    print(f"   Chart Pattern (rounds): {type(granny_chart).__name__}")
    print(f"   • Worked in rounds: {granny_chart.is_worked_in_rounds()}")
    print("   • Uses crochet round terminology (Rnd)")

    print(f"   Chart Pattern (rows): {type(rect_chart).__name__}")
    print(f"   • Worked in rounds: {rect_chart.is_worked_in_rounds()}")
    print("   • Uses crochet row terminology (Row)")


def demonstrate_knitting_patterns():
    """Show various knitting pattern examples."""
    print_section("KNITTING PATTERN EXAMPLES")

    patterns = [
        ("Garter Stitch", pineedle.garter_pattern(8, 4)),
        ("Stockinette Stitch", pineedle.stockinette_pattern(8, 4)),
        ("2x2 Rib", pineedle.rib_pattern(8, 4, 2)),
        ("Seed Stitch", pineedle.seed_pattern(6, 3)),
        ("Cable Swatch", pineedle.cable_swatch(8, 4, 2)),
    ]

    for name, pattern in patterns:
        print(f"\n {name}:")
        print(f"   Type: {type(pattern).__name__}")
        print("   Pattern:")
        for line in pattern.as_text().split("\n"):
            print(f"   {line}")

        # Show pattern repeat if available
        if hasattr(pattern, "get_pattern_repeat"):
            repeat = pattern.get_pattern_repeat()
            if repeat:
                repeat_str = ", ".join(s.value for s in repeat)
                print(f"   Repeat: [{repeat_str}]")


def demonstrate_crochet_patterns():
    """Show various crochet pattern examples."""
    print_section("CROCHET PATTERN EXAMPLES")

    patterns = [
        ("Granny Square (rounds)", pineedle.granny_square_chart(3)),
        ("Single Crochet Rectangle", pineedle.single_crochet_rectangle(6, 3)),
        ("Shell Stitch", pineedle.shell_stitch_pattern(12, 3)),
    ]

    for name, pattern in patterns:
        print(f"\n {name}:")
        print(f"   Type: {type(pattern).__name__}")
        print(f"   Worked in rounds: {pattern.is_worked_in_rounds()}")
        print("   Pattern:")
        for line in pattern.as_text().split("\n")[:5]:  # Limit output for readability
            print(f"   {line}")
        if len(pattern.as_text().split("\n")) > 5:
            print("   ...")


def demonstrate_cli_distinctions():
    """Show how the CLI properly handles knitting vs crochet."""
    print_section("COMMAND-LINE INTERFACE DISTINCTIONS")

    print(" KNITTING COMMANDS:")
    knit_commands = [
        ("garter", "Generate a garter pattern (knit every row)"),
        ("stockinette", "Generate a stockinette pattern (knit RS, purl WS)"),
        ("rib", "Generate a knitting rib pattern"),
        ("seed", "Generate a knitting seed pattern"),
        ("moss", "Generate a knitting moss pattern"),
        ("cable", "Generate a knitting cable pattern"),
    ]

    for cmd, desc in knit_commands:
        print(f"   pineedle --recipe {cmd} --format text")
        print(f"   → {desc}")

    print("\n CROCHET COMMANDS:")
    crochet_commands = [
        ("granny", "Generate a crochet granny square pattern (grid)"),
        ("granny-chart", "Generate a crochet granny square pattern (chart)"),
        ("single-crochet", "Generate a single crochet rectangle pattern"),
        ("shell", "Generate a crochet shell pattern"),
    ]

    for cmd, desc in crochet_commands:
        print(f"   pineedle --recipe {cmd} --format text")
        print(f"   → {desc}")

    print("\n FORMAT COMPATIBILITY:")
    print("   • Knitting charts: --format text (shows RS/WS rows)")
    print("   • Crochet charts: --format text (shows Row/Rnd)")
    print("   • Grid patterns: --format ascii, svg, png, pdf")
    print("   • Auto-detection: CLI detects knitting vs crochet automatically")


def demonstrate_terminology_differences():
    """Show how terminology differs between knitting and crochet."""
    print_section("TERMINOLOGY DIFFERENCES")

    print("KNITTING TERMINOLOGY:")
    print("   • Rows: Right Side (RS) and Wrong Side (WS)")
    print("   • Stitches: k (knit), p (purl), yo (yarn over)")
    print(
        "   • Basic patterns: Garter pattern (knit every row), Stockinette pattern (knit RS, purl WS)"
    )
    print("   • Tools: Needles (metric mm sizes)")
    print("   • Gauge: Stitches and rows per cm")
    print("   • Techniques: Cables, decreases (k2tog, ssk)")

    print("\n CROCHET TERMINOLOGY:")
    print("   • Work: Rows or Rounds (Rnd)")
    print("   • Stitches: ch (chain), sc (single crochet), dc (double crochet)")
    print("   • Tools: Hooks (metric mm sizes)")
    print("   • Gauge: Stitches and rows per cm")
    print("   • Techniques: Shells, clusters, loops (blo, flo)")


def demonstrate_metric_sizing():
    """Show the metric sizing utilities and European conventions."""
    print_section("METRIC SIZING & EUROPEAN CONVENTIONS")

    print(" METRIC MEASUREMENTS:")
    print("   • All measurements in centimeters (cm)")
    print("   • Gauge measured as stitches per cm and rows per cm")
    print("   • Needle sizes in millimeters (mm)")
    print("   • Hook sizes in millimeters (mm)")

    print("\n KNITTING NEEDLE SIZES (mm):")
    from pineedle import MetricNeedleSizes

    common_sizes = MetricNeedleSizes.SIZES[:10]  # First 10 sizes
    print(f"   Common sizes: {', '.join(f'{s}mm' for s in common_sizes)}...")

    print("\n CROCHET HOOK SIZES (mm):")
    from pineedle import MetricHookSizes

    common_hook_sizes = MetricHookSizes.SIZES[:10]  # First 10 sizes
    print(f"   Common sizes: {', '.join(f'{s}mm' for s in common_hook_sizes)}...")

    print("\n YARN WEIGHT RECOMMENDATIONS:")
    from pineedle import get_gauge_info

    # Show DK weight yarn info for knitting
    dk_knit_info = get_gauge_info("dk", "knit")
    if dk_knit_info:
        print(f"   DK Knitting:")
        print(f"   • Gauge: {dk_knit_info['typical_gauge_sts_per_cm']:.1f} sts/cm")
        print(f"   • Recommended needle: {dk_knit_info['recommended_tool_mm']}mm")

    # Show DK weight yarn info for crochet
    dk_crochet_info = get_gauge_info("dk", "crochet")
    if dk_crochet_info:
        print(f"   DK Crochet:")
        print(f"   • Gauge: {dk_crochet_info['typical_gauge_sts_per_cm']:.1f} sts/cm")
        print(f"   • Recommended hook: {dk_crochet_info['recommended_tool_mm']}mm")

    print("\n PATTERN DIMENSIONS:")
    from pineedle import calculate_pattern_dimensions, suggest_pattern_size

    # Calculate dimensions for a sample pattern
    dimensions = calculate_pattern_dimensions(
        width_stitches=40, height_rows=60, gauge_sts_per_cm=1.8, gauge_rows_per_cm=2.4
    )
    print(f"   40 stitches × 60 rows at 1.8 sts/cm, 2.4 rows/cm:")
    print(
        f"   • Physical size: {dimensions['width_cm']}cm × {dimensions['height_cm']}cm"
    )

    # Suggest pattern size for desired dimensions
    suggested = suggest_pattern_size(
        desired_width_cm=20,
        desired_height_cm=15,
        gauge_sts_per_cm=1.8,
        gauge_rows_per_cm=2.4,
    )
    print(f"   For 20cm × 15cm at same gauge:")
    print(
        f"   • Pattern size: {suggested['width_stitches']} sts × {suggested['height_rows']} rows"
    )


def main():
    """Run the complete demonstration."""
    demonstrate_stitch_distinctions()
    demonstrate_pattern_types()
    demonstrate_knitting_patterns()
    demonstrate_crochet_patterns()
    demonstrate_cli_distinctions()
    demonstrate_terminology_differences()
    demonstrate_metric_sizing()


if __name__ == "__main__":
    main()
