"""Core pattern and chart representation with stitch semantics."""

from enum import Enum
from typing import List, Optional


class KnitStitch(str, Enum):
    """Knitting stitches."""

    K = "k"  # knit
    P = "p"  # purl
    YO = "yo"  # yarn over (increase)
    K2TOG = "k2tog"  # knit two together (decrease)
    SSK = "ssk"  # slip, slip, knit (decrease)
    SL1 = "sl1"  # slip one
    C4F = "c4f"  # cable 4 front
    C4B = "c4b"  # cable 4 back
    M1 = "m1"  # make one (increase)
    EMPTY = "."  # empty / background


class CrochetStitch(str, Enum):
    """Crochet stitches."""

    CH = "ch"  # chain
    SC = "sc"  # single crochet
    DC = "dc"  # double crochet
    HDC = "hdc"  # half double crochet
    TR = "tr"  # treble crochet
    SL = "sl"  # slip stitch
    INC = "inc"  # increase
    DEC = "dec"  # decrease
    BLO = "blo"  # back loop only
    FLO = "flo"  # front loop only
    EMPTY = "."  # empty / background


# Keep backwards compatibility
Stitch = KnitStitch


class Pattern:
    """A simple grid-based pattern (boolean cells)."""

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = [[False] * width for _ in range(height)]

    def set_cell(self, x: int, y: int, value=True):
        self.grid[y][x] = value

    def fill_checkerboard(self):
        for y in range(self.height):
            for x in range(self.width):
                self.grid[y][x] = (x + y) % 2 == 0

    def as_rows(self):
        return self.grid


class KnitPattern(Pattern):
    """Pattern specifically for knitting with additional knitting-specific features."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.gauge_stitches = None  # stitches per cm
        self.gauge_rows = None  # rows per cm
        self.needle_size_mm = None

    def set_gauge(
        self, stitches_per_cm: float, rows_per_cm: float, needle_size_mm: float = None
    ):
        """Set knitting gauge information."""
        self.gauge_stitches = stitches_per_cm
        self.gauge_rows = rows_per_cm
        self.needle_size_mm = needle_size_mm


class CrochetPattern(Pattern):
    """Pattern specifically for crochet with additional crochet-specific features."""

    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        self.gauge_stitches = None  # stitches per cm
        self.gauge_rows = None  # rows per cm
        self.hook_size_mm = None
        self.work_in_rounds = False

    def set_gauge(
        self, stitches_per_cm: float, rows_per_cm: float, hook_size_mm: float = None
    ):
        """Set crochet gauge information."""
        self.gauge_stitches = stitches_per_cm
        self.gauge_rows = rows_per_cm
        self.hook_size_mm = hook_size_mm

    def set_rounds(self, rounds: bool = True):
        """Set whether this pattern is worked in rounds (like granny squares)."""
        self.work_in_rounds = rounds


class KnitChartRow:
    """A row of knitting stitches."""

    def __init__(
        self, stitches: List[KnitStitch], rs: bool = True, row_number: int = 1
    ):
        self.stitches = stitches
        self.rs = rs  # Right side (True) or Wrong side (False)
        self.row_number = row_number

    def __str__(self):
        side = "RS" if self.rs else "WS"
        return f"Row {self.row_number} ({side}): " + ", ".join(
            s.value for s in self.stitches
        )


class CrochetChartRow:
    """A row/round of crochet stitches."""

    def __init__(
        self, stitches: List[CrochetStitch], is_round: bool = False, row_number: int = 1
    ):
        self.stitches = stitches
        self.is_round = is_round
        self.row_number = row_number

    def __str__(self):
        work_type = "Rnd" if self.is_round else "Row"
        return f"{work_type} {self.row_number}: " + ", ".join(
            s.value for s in self.stitches
        )


# Keep backwards compatibility
ChartRow = KnitChartRow


class KnitChart:
    """Knitting chart pattern representation."""

    def __init__(self, rows: List[KnitChartRow]):
        self.rows = rows

    def as_text(self):
        return "\n".join(str(r) for r in self.rows)

    def count_stitches(self):
        return [len(r.stitches) for r in self.rows]

    def get_pattern_repeat(self):
        """Find the stitch repeat pattern if one exists."""
        if not self.rows:
            return None
        first_row = self.rows[0].stitches
        # Simple repeat detection - can be enhanced
        for repeat_len in range(1, len(first_row) // 2 + 1):
            if len(first_row) % repeat_len == 0:
                repeat = first_row[:repeat_len]
                if all(
                    first_row[i] == repeat[i % repeat_len]
                    for i in range(len(first_row))
                ):
                    return repeat
        return None


class CrochetChart:
    """Crochet chart pattern representation."""

    def __init__(self, rows: List[CrochetChartRow]):
        self.rows = rows

    def as_text(self):
        return "\n".join(str(r) for r in self.rows)

    def count_stitches(self):
        return [len(r.stitches) for r in self.rows]

    def is_worked_in_rounds(self):
        """Check if this pattern is worked in rounds."""
        return any(row.is_round for row in self.rows)


# Keep backwards compatibility
Chart = KnitChart


# --- Shaping helper ----------------------------------------------------------


class ShapingPanel:
    """Track stitch count changes due to increases/decreases."""

    def __init__(self, base_stitches: int):
        self.rows = []
        self.count = base_stitches

    def add_row(self, increases=0, decreases=0):
        self.count += increases - decreases
        self.rows.append(self.count)

    def suggest_evenly_spaced_increases(self, total_incs, row_length_cm):
        """Return approximate positions for increases."""
        spacing = row_length_cm / (total_incs + 1)
        return [int((i + 1) * spacing) for i in range(total_incs)]
