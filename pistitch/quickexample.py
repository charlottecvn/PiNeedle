from pistitch import KnitPattern
from pistitch.exporters import to_svg, to_ascii

p = KnitPattern(width=24, height=16)
p.fill_checkerboard()

# save an SVG
to_svg(p, "sample_knit.svg")

# print ASCII preview
print(to_ascii(p))
