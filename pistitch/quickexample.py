from tokenize import Token
from pistitch import KnitPattern
from pistitch.exporters import to_svg, to_ascii, to_pdf, to_png, to_text

p = KnitPattern(width=10, height=8)
p.set_gauge(1.8, 2.4, 4.5)  # 1.8 sts/cm, 2.4 rows/cm, 4.5mm needles
p.fill_stockinette()

# save
print(p.as_text())
to_svg(p, "sample_knit.svg")
to_png(p, "sample_knit.png")
to_pdf(p, "sample_knit.pdf")

# print ASCII preview
print(to_ascii(p))
