
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
knit_pattern.set_gauge(1.8, 2.4, 4.5)  # 1.8 sts/cm, 2.4 rows/cm, 4.5mm needles
knit_pattern.fill_garter()  # Default pattern for knitting
print(knit_pattern.as_text())
# Output:
# Pattern: Garter Stitch
# Gauge: 1.8 sts/cm, 2.4 rows/cm using 4.5mm needles
# Instructions: Knit every row
# Repeat for 8 rows
# Finished size: 5.6 × 3.3 cm

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

# Create a crochet pattern with gauge and text export
crochet_pattern = pistitch.CrochetPattern(8, 8)
crochet_pattern.set_gauge(1.4, 1.6, 5.0)  # 1.4 sts/cm, 1.6 rows/cm, 5.0mm hook
crochet_pattern.set_rounds(True)  # Worked in rounds
crochet_pattern.fill_single_crochet()
print(crochet_pattern.as_text())
# Output:
# Gauge: 1.4 sts/cm, 1.6 rows/cm using 5.0mm hook
# Rnd 1: sc, ch, sc, ch, sc, ch, sc, ch
# Rnd 2: ch, sc, ch, sc, ch, sc, ch, sc
# ...
# Finished size: 5.7 × 5.0 cm
```

## Examples

### Text Export Examples

```python
import pistitch

# Grid pattern with text export (garter stitch)
knit_pattern = pistitch.KnitPattern(8, 4)
knit_pattern.set_gauge(1.8, 2.4, 4.5)
knit_pattern.fill_garter()  # Default pattern for knitting
print(knit_pattern.as_text())
# Output:
# Pattern: Garter Stitch
# Gauge: 1.8 sts/cm, 2.4 rows/cm using 4.5mm needles
# Instructions: Knit every row
# Repeat for 4 rows
# Finished size: 4.4 × 1.7 cm

# Or use stockinette stitch
knit_pattern.fill_stockinette()
print(knit_pattern.as_text())
# Output:
# Pattern: Stockinette Stitch
# Gauge: 1.8 sts/cm, 2.4 rows/cm using 4.5mm needles
# Instructions:
# RS rows: Knit all stitches
# WS rows: Purl all stitches
# Repeat for 4 rows
# Finished size: 4.4 × 1.7 cm

# Chart pattern with text export
garter_chart = pistitch.garter_stitch(8, 4)
print(garter_chart.as_text())
# Output:
# Row 1 (RS): k, k, k, k, k, k, k, k
# Row 2 (WS): k, k, k, k, k, k, k, k
# ...

# More complex chart pattern
rib_chart = pistitch.rib_pattern(8, 4)
print(rib_chart.as_text())
# Output:
# Row 1 (RS): k, k, p, p, k, k, p, p
# Row 2 (WS): k, k, p, p, k, k, p, p
# ...

# Use to_text() function for any pattern
print(pistitch.to_text(knit_pattern))
print(pistitch.to_text(rib_chart))
```
