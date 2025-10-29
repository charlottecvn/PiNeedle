# Mathematical Foundations of PiNeedle

Mathematical concepts, algorithms, and equations used in the PiNeedle.

## Table of Contents

1. [Gauge Calculations](#gauge-calculations)
2. [Pattern Dimension Calculations](#pattern-dimension-calculations)
3. [Unit Conversions](#unit-conversions)
4. [Pattern Generation Algorithms](#pattern-generation-algorithms)
5. [Geometric Transformations](#geometric-transformations)
6. [Stitch Pattern Mathematics](#stitch-pattern-mathematics)
7. [Coordinate Systems](#coordinate-systems)

## Gauge Calculations

### Basic Gauge Formula

Gauge defines the relationship between stitches/rows and physical dimensions.

**Stitch Gauge (Horizontal):**
```
gauge_stitches = stitches_count / width_cm
```

**Row Gauge (Vertical):**
```
gauge_rows = rows_count / height_cm
```

## Pattern Dimension Calculations

### Physical Dimensions from Stitch Counts

Given a pattern with known stitch counts and gauge measurements:

**Width Calculation:**
```
width_cm = width_stitches / gauge_stitches_per_cm
```

**Height Calculation:**
```
height_cm = height_rows / gauge_rows_per_cm
```

### Stitch Counts from Desired Dimensions

To determine the required number of stitches for a desired physical size:

**Width in Stitches:**
```
width_stitches = round(desired_width_cm × gauge_stitches_per_cm)
```

**Height in Rows:**
```
height_rows = round(desired_height_cm × gauge_rows_per_cm)
```

### Accuracy and Rounding

Dimensions are rounded to one decimal place for practical use:
```
actual_dimension = round(calculated_dimension, 1)
```

## Unit Conversions

### Length Conversions

**Metric to Imperial:**
```
inches = centimeters / 2.54
stitches_per_inch = stitches_per_cm × 2.54
```

**Imperial to Metric:**
```
centimeters = inches × 2.54
stitches_per_cm = stitches_per_inch × (1 inch / 2.54 cm)
stitches_per_cm = stitches_per_inch × 0.393701
```

### Gauge Rate Conversions

The conversion factor between metric and imperial gauge measurements:
```
conversion_factor = 2.54  # cm per inch
```

Where:
- `CM_TO_INCH = 2.54`
- `INCH_TO_CM = 1/2.54 ≈ 0.393701`

## Pattern Generation Algorithms

### Checkerboard Pattern

For a checkerboard pattern with alternating boolean values:
```
cell_value = (x + y) mod 2 = 0
```
Where `(x, y)` represents the coordinate position in the grid.

### Seed Stitch Pattern

Seed stitch alternates knit and purl stitches in a checkerboard pattern:
```
stitch_type = {
    knit   if (x + y) mod 2 = 0
    purl   if (x + y) mod 2 = 1
}
```

### Stockinette Pattern

Stockinette alternates between all-knit rows and all-purl rows:
```
stitch_type = {
    knit   if y mod 2 = 0  (right-side rows)
    purl   if y mod 2 = 1  (wrong-side rows)
}
```

### Rib Pattern

For n×n rib patterns:
```
stitch_type = {
    knit   if (x ÷ n) mod n = 0
    purl   if (x ÷ n) mod n = 1
}
```

### Moss Pattern

Moss stitch creates n×n blocks of alternating stitch types:
```
stitch_type = {
    knit   if ((x ÷ n) + (y ÷ n)) mod n = 0
    purl   if ((x ÷ n) + (y ÷ n)) mod n = 1
}
```

## Geometric Transformations

### Pattern Scaling

When exporting patterns to different formats, cells are scaled by a constant factor:

**SVG/PNG/PDF Scaling:**
```
pixel_width = pattern_width × cell_size + (2 × padding)
pixel_height = pattern_height × cell_size + (2 × padding)
```

**Cell Position Mapping:**
```
x_pixel = padding + (x_stitch × cell_size)
y_pixel = padding + (y_row × cell_size)
```

For PDF output, Y-coordinates are inverted:
```
y_pdf = total_height - (padding + ((y_row + 1) × cell_size))
```

### Aspect Ratio Calculations

The aspect ratio of a finished piece:
```
aspect_ratio = width_cm / height_cm
```

Or in terms of stitches and gauge:
```
aspect_ratio = (width_stitches / gauge_stitches_per_cm) / (height_rows / gauge_rows_per_cm)
aspect_ratio = (width_stitches × gauge_rows_per_cm) / (height_rows × gauge_stitches_per_cm)
```

## Stitch Pattern Mathematics

### Pattern Repeat Detection

For identifying repeating motifs in stitch patterns, we analyze sequences:

**Horizontal Repeat Length:**
```
repeat_length = gcd(pattern_variations_in_row)
```

**Vertical Repeat Length:**
```
repeat_height = gcd(pattern_variations_between_rows)
```

### Cable Crossing Mathematics

Cable patterns involve crossing stitches over specific intervals:
```
cable_position = base_position + (crossing_width × direction)
```
Where `direction = ±1` for front/back crossings.

## Coordinate Systems

### Grid Coordinate System

PiNeedle uses a standard coordinate system:
- Origin `(0,0)` at top-left
- X-axis increases rightward (stitches)
- Y-axis increases downward (rows)

### Knitting Coordinate Mapping

Traditional knitting charts use a different coordinate system:
- Origin at bottom-left
- Y-axis increases upward (rows worked from bottom to top)

**Coordinate Transformation:**
```
knitting_y = total_rows - programming_y - 1
```

### Right-Side vs Wrong-Side Rows

Row orientation affects stitch interpretation:
```
is_right_side = (row_number mod 2) = 1
is_wrong_side = (row_number mod 2) = 0
```

## Statistical Measures

### Gauge Accuracy

Standard deviation in gauge measurements:
```
σ = √(Σ(gauge_i - gauge_mean)² / (n-1))
```

### Pattern Complexity

Measure of pattern regularity:
```
complexity = unique_stitch_combinations / total_stitches
```

### Tool Size Optimization

Closest tool size selection uses minimum distance:
```
optimal_size = argmin|tool_size - target_size|
```

## Error Tolerances

### Conversion Accuracy

When converting between measurement systems:
```
max_error = |converted_value - exact_value| < 0.001
```

## Performance Considerations

### Algorithmic Complexity

- Pattern generation: O(width × height)
- Gauge calculations: O(1)
- Pattern export: O(width × height)
- Unit conversions: O(1)

### Memory Usage

Grid storage requirements:
```
memory_bytes = width × height × cell_size_bytes
```

For boolean grids: `cell_size_bytes = 1`
For stitch enums: `cell_size_bytes = 4` (typical string/enum storage)
