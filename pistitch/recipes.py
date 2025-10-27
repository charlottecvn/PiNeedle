"""Example pattern recipes using Chart and Stitch semantics."""

from .patterns import (
    KnitStitch,
    CrochetStitch,
    KnitChart,
    CrochetChart,
    KnitChartRow,
    CrochetChartRow,
    # Keep backwards compatibility
    Stitch,
    Chart,
    ChartRow,
)


def garter_pattern(width=24, height=16):
    """Create a garter pattern (knit every row)."""
    rows = []
    for y in range(height):
        stitches = [KnitStitch.K] * width
        rows.append(KnitChartRow(stitches, rs=(y % 2 == 0), row_number=y + 1))
    return KnitChart(rows)


def stockinette_pattern(width=24, height=16):
    """Create a stockinette pattern (knit RS, purl WS)."""
    rows = []
    for y in range(height):
        if y % 2 == 0:  # RS rows
            stitches = [KnitStitch.K] * width
        else:  # WS rows
            stitches = [KnitStitch.P] * width
        rows.append(KnitChartRow(stitches, rs=(y % 2 == 0), row_number=y + 1))
    return KnitChart(rows)


def rib_pattern(width=24, height=16, rib=2):
    """Create a knitting rib pattern (e.g., 2x2 rib)."""
    rows = []
    for y in range(height):
        stitches = []
        for x in range(width):
            if (x // rib) % 2 == 0:
                stitches.append(KnitStitch.K)
            else:
                stitches.append(KnitStitch.P)
        rows.append(KnitChartRow(stitches, rs=(y % 2 == 0), row_number=y + 1))
    return KnitChart(rows)


def seed_pattern(width=24, height=16):
    """Create a knitting seed pattern."""
    rows = []
    for y in range(height):
        stitches = []
        for x in range(width):
            if (x + y) % 2 == 0:
                stitches.append(KnitStitch.K)
            else:
                stitches.append(KnitStitch.P)
        rows.append(KnitChartRow(stitches, rs=(y % 2 == 0), row_number=y + 1))
    return KnitChart(rows)


def moss_pattern(width=24, height=16):
    """Create a knitting moss pattern (2x2 block alternation)."""
    rows = []
    for y in range(height):
        stitches = []
        for x in range(width):
            if ((x // 2) + (y // 2)) % 2 == 0:
                stitches.append(KnitStitch.K)
            else:
                stitches.append(KnitStitch.P)
        rows.append(KnitChartRow(stitches, rs=(y % 2 == 0), row_number=y + 1))
    return KnitChart(rows)


def granny_square(size=8, rounds=4):
    """Create a traditional crochet granny square pattern."""
    from .patterns import CrochetPattern

    # For simple visualization, return a grid pattern
    p = CrochetPattern(size, size)
    p.set_rounds(True)
    for r in range(rounds):
        for x in range(r, size - r):
            p.set_cell(x, r, True)
            p.set_cell(x, size - r - 1, True)
        for y in range(r, size - r):
            p.set_cell(r, y, True)
            p.set_cell(size - r - 1, y, True)
    return p


def granny_square_chart(rounds=4):
    """Create a detailed crochet granny square chart with actual crochet stitches."""
    rows = []

    # Round 1: Magic ring with chains and double crochets
    round1 = [CrochetStitch.CH] * 3 + [CrochetStitch.DC] * 3 + [CrochetStitch.CH] * 2
    rows.append(CrochetChartRow(round1, is_round=True, row_number=1))

    # Round 2: Work into chain spaces
    for round_num in range(2, rounds + 1):
        round_stitches = []
        # Simplified: alternating DC and CH for corner spaces
        pattern_length = 4 + (round_num - 1) * 3
        for i in range(pattern_length):
            if i % 4 == 0:
                round_stitches.extend([CrochetStitch.CH, CrochetStitch.CH])
            else:
                round_stitches.append(CrochetStitch.DC)
        rows.append(
            CrochetChartRow(round_stitches, is_round=True, row_number=round_num)
        )

    return CrochetChart(rows)


def cable_swatch(width=24, height=16, cable_width=6):
    """Create a knitting cable swatch pattern."""
    rows = []
    for y in range(height):
        stitches = []
        for x in range(width):
            if cable_width <= x < 2 * cable_width:
                # cable area - add cable crosses every 4 rows
                if y % 8 == 0:
                    stitches.append(KnitStitch.C4F)  # cable 4 front
                elif y % 8 == 4:
                    stitches.append(KnitStitch.C4B)  # cable 4 back
                else:
                    stitches.append(KnitStitch.K)
            else:
                stitches.append(KnitStitch.P)
        rows.append(KnitChartRow(stitches, rs=(y % 2 == 0), row_number=y + 1))
    return KnitChart(rows)


def single_crochet_rectangle(width=20, height=12):
    """Create a simple single crochet rectangle pattern."""
    rows = []

    # Foundation chain
    foundation = [CrochetStitch.CH] * (width + 1)  # Extra chain for turning
    rows.append(CrochetChartRow(foundation, is_round=False, row_number=0))

    # Work in rows
    for row_num in range(1, height + 1):
        row_stitches = [CrochetStitch.CH]  # turning chain
        row_stitches.extend([CrochetStitch.SC] * width)
        rows.append(CrochetChartRow(row_stitches, is_round=False, row_number=row_num))

    return CrochetChart(rows)


def shell_stitch_pattern(width=24, height=8):
    """Create a crochet shell stitch pattern."""
    rows = []

    # Foundation
    foundation = [CrochetStitch.CH] * (width + 2)
    rows.append(CrochetChartRow(foundation, is_round=False, row_number=0))

    for row_num in range(1, height + 1):
        row_stitches = [CrochetStitch.CH] * 3  # turning chain

        # Create shell pattern (5 DC in same stitch)
        for x in range(0, width, 6):
            if row_num % 2 == 1:
                # Shell row
                row_stitches.extend([CrochetStitch.DC] * 5)
                if x + 6 < width:
                    row_stitches.append(CrochetStitch.SC)
            else:
                # Single crochet between shells
                row_stitches.extend([CrochetStitch.SC, CrochetStitch.SC])

        rows.append(CrochetChartRow(row_stitches, is_round=False, row_number=row_num))

    return CrochetChart(rows)


# Backwards compatibility aliases
def garter_stitch(width=24, height=16):
    """Create a garter stitch pattern (knit every row).

    DEPRECATED: Use garter_pattern() instead.
    """
    return garter_pattern(width, height)


def stockinette_stitch(width=24, height=16):
    """Create a stockinette stitch pattern (knit RS, purl WS).

    DEPRECATED: Use stockinette_pattern() instead.
    """
    return stockinette_pattern(width, height)
