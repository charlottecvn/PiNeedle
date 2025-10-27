# PiStitch

A Python package for generating knitting and crochet patterns.


## Features

- Knitting stitches (k, p, yo, k2tog, cables) with RS/WS row terminology
- Crochet stitches (ch, sc, dc, hdc, tr) with Row/Round terminology
- Both grid-based patterns and semantic stitch charts
- Track stitches/rows per inch with needle/hook sizes
- Multiple Exports: SVG, PNG, PDF, ASCII, and text formats
- Command-line with knitting/crochet-specific recipes

## Installation

```bash
# Install the package
pip install -e .

# Install with all export dependencies
pip install -e .[all]

# Or install dependencies separately
pip install svgwrite pillow reportlab
```

## Quick Examples

### Knitting Patterns

```python
import pistitch

# Create a knitting rib pattern
rib_chart = pistitch.rib_pattern(width=8, height=4)
print(rib_chart.as_text())
# Output:
# Row 1 (RS): k, k, p, p, k, k, p, p
# Row 2 (WS): k, k, p, p, k, k, p, p
# ...

# Create a knitting pattern with gauge
knit_pattern = pistitch.KnitPattern(10, 8)
knit_pattern.set_gauge(4.5, 6.0, "US 7")
pistitch.to_svg(knit_pattern, "knit_pattern.svg")
```

### Crochet Patterns

```python
import pistitch

# Create a crochet granny square chart
granny_chart = pistitch.granny_square_chart(rounds=3)
print(granny_chart.as_text())
# Output:
# Rnd 1: ch, ch, ch, dc, dc, dc, ch, ch
# Rnd 2: ch, ch, dc, dc, dc, ch, ch, dc, dc
# ...

# Create a single crochet rectangle
sc_rect = pistitch.single_crochet_rectangle(width=6, height=4)
print(f"Worked in rounds: {sc_rect.is_worked_in_rounds()}")  # False

# Create a crochet pattern with gauge
crochet_pattern = pistitch.CrochetPattern(8, 8)
crochet_pattern.set_gauge(1.4, 1.6, 5.0)  # 1.4 sts/cm, 1.6 rows/cm, 5.0mm hook
crochet_pattern.set_rounds(True)  # Worked in rounds
```

## Craft Distinctions

### Knitting Features

- **Stitches**: `k`, `p`, `yo`, `k2tog`, `ssk`, `c4f`, `c4b`, `m1`
- **Terminology**: Right Side (RS) and Wrong Side (WS) rows
- **Pattern Types**: `KnitPattern`, `KnitChart`, `KnitChartRow`
- **Tools**: Needle sizes (metric mm)
- **Techniques**: Cables, texture patterns, shaping

### Crochet Features

- **Stitches**: `ch`, `sc`, `dc`, `hdc`, `tr`, `sl`, `inc`, `dec`, `blo`, `flo`
- **Terminology**: Rows and Rounds (Rnd)
- **Pattern Types**: `CrochetPattern`, `CrochetChart`, `CrochetChartRow`
- **Tools**: Hook sizes (metric mm)
- **Techniques**: Shells, clusters, working in rounds

## Available Patterns

### Knitting Recipes
- `rib_pattern(width, height, rib=2)` - Ribbing patterns (1x1, 2x2, etc.)
- `seed_pattern(width, height)` - Seed stitch texture
- `moss_pattern(width, height)` - Moss stitch (2x2 alternating)
- `cable_swatch(width, height, cable_width=6)` - Cable patterns

### Crochet Recipes
- `granny_square(size, rounds=4)` - Traditional granny square (grid)
- `granny_square_chart(rounds=4)` - Granny square with stitch details
- `single_crochet_rectangle(width, height)` - Basic SC rectangle
- `shell_stitch_pattern(width, height)` - Shell stitch pattern

## Command Line Interface

The CLI automatically detects whether you're creating a knitting or crochet pattern:

```bash
# Knitting patterns
pistitch --recipe rib --width 8 --height 4 --format text
pistitch --recipe cable --width 12 --height 8 --format svg --out cable.svg

# Crochet patterns
pistitch --recipe granny-chart --rounds 4 --format text
pistitch --recipe single-crochet --width 10 --height 6 --format text
pistitch --recipe shell --width 12 --height 6 --format text

# Export options
pistitch --recipe granny --width 8 --format ascii    # Grid patterns
pistitch --recipe rib --format text                  # Chart patterns
```

### CLI Options

- `--recipe`: Pattern type (rib, seed, moss, cable, granny, granny-chart, single-crochet, shell)
- `--width`: Pattern width (default: 24)
- `--height`: Pattern height (default: 16)
- `--rounds`: Number of rounds for crochet (default: 4)
- `--format`: Output format (ascii, svg, png, pdf, text)
- `--out`: Output file (default: stdout)
- `--craft`: Force craft type (knit/crochet) if needed

## Export Formats

- **ASCII**: Grid patterns only (`#` for filled, `.` for empty)
- **SVG**: Grid patterns, scalable vector graphics
- **PNG**: Grid patterns, raster images
- **PDF**: Grid patterns, print-ready
- **Text**: Chart patterns, human-readable stitch instructions

## Examples

For a demonstration of the knitting vs crochet distinctions, run:

```bash
python knitting_vs_crochet_demo.py
```
