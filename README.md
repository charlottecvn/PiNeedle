# PiNeedle

A Python package for generating knitting and crochet patterns. The CLI automatically detects whether you're creating a knitting or crochet pattern.

## Quick Start

```bash
# Install the package
pip install -e .

# Try basic patterns
pineedle --recipe garter --width 8 --height 4 --format text
pineedle --recipe granny --width 6 --format ascii

# Run demo
python knitting_vs_crochet_demo.py
```

## Help & Documentation
For more examples, see the [examples.md](examples.md) and [cli.md](cli.md).

### Get CLI Help
```bash
pineedle --help                    # Show all available options
```

### Available Patterns
- **Knitting**: `garter`, `stockinette`, `rib`, `seed`, `moss`, `cable`
- **Crochet**: `granny`, `granny-chart`, `single-crochet`, `shell`

### Quick Pattern Examples
```bash
# Beginner-friendly garter pattern
pineedle --recipe garter --width 10 --height 5 --format text

# Classic stockinette pattern
pineedle --recipe stockinette --width 10 --height 5 --format text

# Traditional granny square
pineedle --recipe granny --width 8 --format ascii
```

## Testing

### Run All Tests
```bash
# Quick test run
python -m pytest tests/ -q

# Quick functionality test
python -c "import pineedle; print(pineedle.garter_pattern(6,3).as_text())"
```

## Features

- **Knitting Support**: Knitting stitches (k, p, yo, k2tog, cables) with RS/WS row terminology
- **Crochet Support**: Crochet stitches (ch, sc, dc, hdc, tr) with Row/Round terminology
- **Pattern Types**: Both grid-based patterns and semantic stitch charts
- **Gauge Support**: Track stitches/rows per cm with needle/hook sizes (metric)
- **Multiple Exports**: SVG, PNG, PDF, ASCII, and text formats
- **CLI Interface**: Command-line tool
- **Metric System**: European measurements (cm, mm) as standard

## Installation

```bash
# Install the package
pip install -e .

# Install with all export dependencies
pip install -e .[all]

# Or install dependencies separately
pip install svgwrite pillow reportlab
```

## Differences

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
- `garter_pattern(width, height)` - Garter pattern (knit every row)
- `stockinette_pattern(width, height)` - Stockinette pattern (knit RS, purl WS)
- `rib_pattern(width, height, rib=2)` - Ribbing patterns (1x1, 2x2, etc.)
- `seed_pattern(width, height)` - Seed stitch texture
- `moss_pattern(width, height)` - Moss stitch (2x2 alternating)
- `cable_swatch(width, height, cable_width=6)` - Cable patterns

### Crochet Recipes
- `granny_square(size, rounds=4)` - Traditional granny square (grid)
- `granny_square_chart(rounds=4)` - Granny square with stitch details
- `single_crochet_rectangle(width, height)` - Basic SC rectangle
- `shell_stitch_pattern(width, height)` - Shell stitch pattern

## Export Formats

- **ASCII**: Grid patterns only (`#` for filled, `.` for empty)
- **SVG**: Grid patterns, scalable vector graphics (metric units)
- **PNG**: Grid patterns, raster images
- **PDF**: Grid patterns
- **Text**: All patterns, stitch instructions with gauge info and sizing
