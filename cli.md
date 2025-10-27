## Command Line Interface

The CLI automatically detects whether you're creating a knitting or crochet pattern:

```bash
# Knitting patterns
pineedle --recipe garter --width 8 --height 4 --format text
pineedle --recipe stockinette --width 8 --height 4 --format text
pineedle --recipe rib --width 8 --height 4 --format text
pineedle --recipe cable --width 12 --height 8 --format svg --out cable.svg

# Crochet patterns
pineedle --recipe granny-chart --rounds 4 --format text
pineedle --recipe single-crochet --width 10 --height 6 --format text
pineedle --recipe shell --width 12 --height 6 --format text

# Export options
pineedle --recipe granny --width 8 --format ascii    # Grid patterns
pineedle --recipe granny --width 8 --format text     # Grid pattern instructions
pineedle --recipe rib --format text                  # Chart pattern instructions
```

### CLI Options

- `--recipe`: Pattern type (garter, stockinette, rib, seed, moss, cable, granny, granny-chart, single-crochet, shell)
- `--width`: Pattern width (default: 24)
- `--height`: Pattern height (default: 16)
- `--rounds`: Number of rounds for crochet (default: 4)
- `--format`: Output format (ascii, svg, png, pdf, text)
- `--out`: Output file (default: stdout)
- `--craft`: Force craft type (knit/crochet) if needed
