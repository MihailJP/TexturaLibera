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

FamilyName = "TexturaLibera"
HumanReadableFamilyName = "Textura Libera"

WeightDat = [
	{'Name': 'Thin'      ,},
	{'Name': 'ExtraLight',},
	{'Name': 'Light'     ,},
	{'Name': 'Book'      ,},
	{'Name': 'Medium'    ,},
	{'Name': 'Demi'      ,},
	{'Name': 'Bold'      ,},
	{'Name': 'ExtraBold' ,},
	{'Name': 'Black'     ,},
]

WeightCode = None #yet. This will be set later.

# Duplicate a layer
def dupLayer(layer):
	newLayer = fontforge.layer()
	for contour in glyph.layers[layerID]:
		newLayer += contour
	return newLayer

# Check arguments
if len(argv) <= 3:
	stderr.write("Usage: "+argv[0]+" out-font weight width\n")
	exit(1)
try:
	if not (0 < int(argv[2]) < 1000):
		raise ValueError
except ValueError:
	stderr.write("Error: Weight must be more than 0 and less than 1000\n")
	exit(2)
try:
	if not (0.5 <= float(argv[3]) <= 2.0):
		raise ValueError
except ValueError:
	stderr.write("Error: Width must be between 0.5 and 2.0\n")
	exit(2)

# Load fonts
BaseFont = fontforge.open(BaseFontFile)
BoldFont = fontforge.open(BoldFontFile)
ExpandedFont = fontforge.open(ExpandedFontFile)
CondensedFont = fontforge.open(CondensedFontFile)

# Set weight code
if   int(argv[2]) < 150: WeightCode = 0 # Thin
elif int(argv[2]) < 250: WeightCode = 1 # ExtraLight
elif int(argv[2]) < 350: WeightCode = 2 # Light
elif int(argv[2]) < 450: WeightCode = 3 # Book
elif int(argv[2]) < 550: WeightCode = 4 # Medium
elif int(argv[2]) < 650: WeightCode = 5 # DemiBold
elif int(argv[2]) < 750: WeightCode = 6 # Bold
elif int(argv[2]) < 850: WeightCode = 7 # ExtraBold
else:                    WeightCode = 8 # Black

# Interpolate
WeightInterpol = BaseFont.interpolateFonts((float(argv[2]) - 500.0) / 200.0, BoldFontFile)
WidthInterpol = None # yet. See below
if float(argv[3]) < 1.0: # Narrow
	WidthInterpol = BaseFont.interpolateFonts((1.0 - float(argv[3])) * 5.0, CondensedFontFile)
else: # Widen
	WidthInterpol = BaseFont.interpolateFonts((float(argv[3]) - 1.0) * 5.0, ExpandedFontFile)
MidInterpol = WeightInterpol.interpolateFonts(0.5, WidthInterpol.path)
Interpolated = BaseFont.interpolateFonts(2.0, MidInterpol.path)
WeightInterpol.close(); WeightInterpol = None
WidthInterpol.close(); WidthInterpol = None
MidInterpol.close(); MidInterpol = None

# Change width of font
for glyph in BaseFont.glyphs():
	if glyph.isWorthOutputting():
		glyph.transform(scale(float(argv[3]), 1.0), ("partialRefs",))
(kernFirst, kernSecond, kernVal) = BaseFont.getKerningClass("Kerning-1")
BaseFont.alterKerningClass(
	"Kerning-1",
	kernFirst,
	kernSecond,
	tuple(map(lambda x: int(round(float(x) * float(argv[3]))), kernVal))
	)

# Set output font properties
BaseFont.strokedfont = False
BaseFont.fontname = FamilyName + "-" + WeightDat[WeightCode]['Name']
BaseFont.familyname = HumanReadableFamilyName
BaseFont.fullname = HumanReadableFamilyName + " " + WeightDat[WeightCode]['Name']
BaseFont.weight = WeightDat[WeightCode]['Name']
BaseFont.os2_weight = (WeightCode + 1) * 100
BaseFont.os2_panose = (
	BaseFont.os2_panose[0],
	BaseFont.os2_panose[1],
	WeightCode + 2,
	BaseFont.os2_panose[3],
	BaseFont.os2_panose[4],
	BaseFont.os2_panose[5],
	BaseFont.os2_panose[6],
	BaseFont.os2_panose[7],
	BaseFont.os2_panose[8],
	BaseFont.os2_panose[9])

# Stroke
for glyph in Interpolated.glyphs():
	if glyph.isWorthOutputting():
		for layerID in range(1, 4):
			if not glyph.layers[layerID].isEmpty():
				layer = dupLayer(glyph.layers[layerID])
				layer.transform(scale(WorkScale))
				penScale = 0.8 if BaseFont[glyph.glyphname].color == 0x00ff00 else 1.0
				layer.stroke(
					"caligraphic",
					float(argv[2]) / 5.0 * WorkScale * penScale,
					float(argv[2]) * 0.06 * WorkScale * penScale,
					rad(penDegrees[layerID]),
					("removeinternal",) if BaseFont[glyph.glyphname].color == 0xffff00 else (None,))
				layer.transform(scale(1.0 / WorkScale))
				glyph.layers[layerID] = layer
		for layerID in range(2, 4):
			if not glyph.layers[layerID].isEmpty():
				glyph.layers[1] += dupLayer(glyph.layers[layerID])
		glyph.removeOverlap()
		glyph.round()
		for layerID in range(1, 4):
			BaseFont[glyph.glyphname].layers[layerID] = dupLayer(glyph.layers[1])
		BaseFont[glyph.glyphname].autoHint()

# Save font
BaseFont.save(argv[1])
