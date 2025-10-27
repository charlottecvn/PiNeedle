"""Textual pattern format for knit charts."""


def chart_to_text(chart):
    lines = []
    for row in chart.rows:
        side = "RS" if row.rs else "WS"
        lines.append(
            f"Row {row.row_number} ({side}): "
            + ", ".join(s.value for s in row.stitches)
        )
    return "\n".join(lines)
