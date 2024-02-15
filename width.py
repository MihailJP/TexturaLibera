#!/usr/bin/env fontforge

from sys import argv
import fontforge
from psMat import scale

font = fontforge.open(argv[2])
font.selection.none()
for glyph in font:
	if font[glyph].isWorthOutputting():
		font.selection.select(("more",), glyph)
font.transform(scale(float(argv[3]), 1), ("simplePos", "kernClasses"))
font.save(argv[1])
