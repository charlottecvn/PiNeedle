"""Exporters for PiNeedle patterns."""

import io
from PIL import Image, ImageDraw
import svgwrite
from reportlab.pdfgen import canvas as pdfcanvas


def to_ascii(pattern):
    rows = pattern.as_rows()
    return "\n".join("".join("#" if c else "." for c in r) for r in rows)


def to_svg(pattern, path, cell_size=12, padding=4):
    w = pattern.width * cell_size + padding * 2
    h = pattern.height * cell_size + padding * 2
    dwg = svgwrite.Drawing(filename=path, size=(w, h))
    for y, row in enumerate(pattern.as_rows()):
        for x, c in enumerate(row):
            if c:
                dwg.add(
                    dwg.rect(
                        insert=(padding + x * cell_size, padding + y * cell_size),
                        size=(cell_size, cell_size),
                        fill="black",
                    )
                )
    dwg.save()


def to_png(pattern, path, cell_size=12, padding=4):
    w = pattern.width * cell_size + padding * 2
    h = pattern.height * cell_size + padding * 2
    img = Image.new("RGB", (w, h), "white")
    draw = ImageDraw.Draw(img)
    for y, row in enumerate(pattern.as_rows()):
        for x, c in enumerate(row):
            if c:
                x0 = padding + x * cell_size
                y0 = padding + y * cell_size
                draw.rectangle([x0, y0, x0 + cell_size, y0 + cell_size], fill="black")
    img.save(path)


def to_pdf(pattern, path, cell_size=12, padding=4):
    w = pattern.width * cell_size + padding * 2
    h = pattern.height * cell_size + padding * 2
    pdf = pdfcanvas.Canvas(path, pagesize=(w, h))
    for y, row in enumerate(pattern.as_rows()):
        for x, c in enumerate(row):
            if c:
                x0 = padding + x * cell_size
                y0 = h - (padding + (y + 1) * cell_size)
                pdf.rect(x0, y0, cell_size, cell_size, fill=True, stroke=False)
    pdf.save()


def to_text(pattern):
    """Render a pattern to a text description.

    Works with both semantic charts (KnitChart, CrochetChart) and
    grid patterns (KnitPattern, CrochetPattern, Pattern).
    """
    if hasattr(pattern, "as_text"):
        return pattern.as_text()
    else:
        # Fallback for patterns without as_text method
        return f"Pattern: {pattern.width} × {pattern.height} stitches"
