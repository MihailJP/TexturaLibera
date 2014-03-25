#!/usr/bin/env fontforge

from sys import (argv, stderr, exit)
from math import radians as rad
from psMat import scale
import fontforge

BaseFontFile      = "TexturaLibera-Medium.sfdir"
BoldFontFile      = "TexturaLibera-Bold.sfdir"
ExpandedFontFile  = "TexturaLibera-Expanded.sfdir"
CondensedFontFile = "TexturaLibera-Condensed.sfdir"

penDegrees = (0, 45, 90, 135)

WorkScale = 4.0

def dupLayer(layer):
	newLayer = fontforge.layer()
	for contour in glyph.layers[layerID]:
		newLayer += contour
	return newLayer

if len(argv) <= 2:
	stderr.write("Usage: "+argv[0]+" out-font weight\n")
	exit(1)
elif not (0 < int(argv[1]) < 1000):
	stderr.write("Weight must be more than 0 and less than 1000\n")
	exit(2)

BaseFont = fontforge.open(BaseFontFile)
BoldFont = fontforge.open(BoldFontFile)

Interpolated = BaseFont.interpolateFonts((float(argv[2]) - 500.0) / 200.0, BoldFontFile)

for glyph in Interpolated.glyphs():
	if glyph.isWorthOutputting():
		for layerID in range(1, 4):
			if not glyph.layers[layerID].isEmpty():
				layer = dupLayer(glyph.layers[layerID])
				layer.transform(scale(WorkScale))
				layer.stroke(
					"caligraphic",
					float(argv[2]) / 5.0 * WorkScale,
					float(argv[2]) * 0.06 * WorkScale,
					rad(penDegrees[layerID]))
				layer.transform(scale(1.0 / WorkScale))
				glyph.layers[layerID] = layer
		for layerID in range(2, 4):
			if not glyph.layers[layerID].isEmpty():
				glyph.layers[1] += dupLayer(glyph.layers[layerID])

Interpolated.save(argv[1])
