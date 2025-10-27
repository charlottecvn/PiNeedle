"""Command-line interface for PiStitch."""

import argparse
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
from .exporters import to_svg, to_ascii, to_png, to_pdf, to_text


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="pistitch",
        description="Generate knitting and crochet patterns (uses metric measurements: cm, mm)",
        epilog="Examples: pistitch --recipe rib --width 20 --height 15 (creates ~11×6cm at DK gauge)\n"
        "For a comprehensive demo of knitting vs crochet distinctions, run: python knitting_vs_crochet_demo.py",
    )
    parser.add_argument(
        "--recipe",
        choices=[
            # Knitting patterns
            "rib",
            "seed",
            "moss",
            "cable",
            # Crochet patterns
            "granny",
            "granny-chart",
            "single-crochet",
            "shell",
        ],
        required=True,
        help="Pattern type to generate",
    )
    parser.add_argument(
        "--width", type=int, default=24, help="Pattern width (stitches)"
    )
    parser.add_argument("--height", type=int, default=16, help="Pattern height (rows)")
    parser.add_argument(
        "--rounds", type=int, default=4, help="Number of rounds (for crochet)"
    )
    parser.add_argument("--out", type=str, default="-", help="Output file")
    parser.add_argument(
        "--format",
        choices=["ascii", "svg", "png", "pdf", "text"],
        default="ascii",
        help="Output format",
    )
    parser.add_argument(
        "--craft",
        choices=["knit", "crochet"],
        help="Specify craft type (auto-detected from recipe)",
    )
    args = parser.parse_args(argv)

    # Create pattern based on recipe
    if args.recipe == "rib":
        pattern = rib_pattern(args.width, args.height)
        craft_type = "knit"
    elif args.recipe == "seed":
        pattern = seed_pattern(args.width, args.height)
        craft_type = "knit"
    elif args.recipe == "moss":
        pattern = moss_pattern(args.width, args.height)
        craft_type = "knit"
    elif args.recipe == "cable":
        pattern = cable_swatch(args.width, args.height)
        craft_type = "knit"
    elif args.recipe == "granny":
        pattern = granny_square(args.width, args.rounds)
        craft_type = "crochet"
    elif args.recipe == "granny-chart":
        pattern = granny_square_chart(args.rounds)
        craft_type = "crochet"
    elif args.recipe == "single-crochet":
        pattern = single_crochet_rectangle(args.width, args.height)
        craft_type = "crochet"
    elif args.recipe == "shell":
        pattern = shell_stitch_pattern(args.width, args.height)
        craft_type = "crochet"

    # Use specified craft type if provided
    if args.craft:
        craft_type = args.craft

    # Handle output based on pattern type
    try:
        if args.format == "text":
            # Chart patterns have as_text() method
            if hasattr(pattern, "as_text"):
                print(f"# {craft_type.title()} Pattern")
                print(pattern.as_text())
                # Show approximate dimensions for metric context
                if craft_type == "knit":
                    approx_width = args.width / 1.8  # ~1.8 sts/cm for DK
                    approx_height = args.height / 2.4  # ~2.4 rows/cm for DK
                else:
                    approx_width = args.width / 1.4  # ~1.4 sts/cm for DK crochet
                    approx_height = args.height / 1.6  # ~1.6 rows/cm for DK crochet
                print(
                    f"# Approximate size at DK gauge: {approx_width:.1f}×{approx_height:.1f}cm"
                )
            else:
                print("Text format not available for this pattern type")
        elif args.format == "ascii":
            # Grid patterns have as_rows() method for ASCII export
            if hasattr(pattern, "as_rows"):
                print(f"# {craft_type.title()} Pattern (ASCII)")
                print(to_ascii(pattern))
                # Show approximate dimensions for metric context
                if craft_type == "knit":
                    approx_width = args.width / 1.8  # ~1.8 sts/cm for DK
                    approx_height = args.height / 2.4  # ~2.4 rows/cm for DK
                else:
                    approx_width = args.width / 1.4  # ~1.4 sts/cm for DK crochet
                    approx_height = args.height / 1.6  # ~1.6 rows/cm for DK crochet
                print(
                    f"# Approximate size at DK gauge: {approx_width:.1f}×{approx_height:.1f}cm"
                )
            else:
                print(
                    "ASCII format not available for chart patterns. Try --format text"
                )
        elif args.format == "svg":
            if hasattr(pattern, "as_rows"):
                to_svg(pattern, args.out)
                print(f"SVG saved to {args.out}")
            else:
                print("SVG export not available for chart patterns")
        elif args.format == "png":
            if hasattr(pattern, "as_rows"):
                to_png(pattern, args.out)
                print(f"PNG saved to {args.out}")
            else:
                print("PNG export not available for chart patterns")
        elif args.format == "pdf":
            if hasattr(pattern, "as_rows"):
                to_pdf(pattern, args.out)
                print(f"PDF saved to {args.out}")
            else:
                print("PDF export not available for chart patterns")
    except Exception as e:
        print(f"Error generating pattern: {e}")
