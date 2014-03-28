#!/usr/bin/env fontforge

from sys import (argv, stdout, stderr, exit)
from math import radians as rad
from psMat import scale
import fontforge

BaseFontFile      = "TexturaLibera-Medium.sfdir"
BoldFontFile      = "TexturaLibera-Bold.sfdir"
ExpandedFontFile  = "TexturaLibera-Expanded.sfdir"
CondensedFontFile = "TexturaLibera-Condensed.sfdir"

penDegrees = (0, 45, 90, 135)

WorkScales = [1.0, 1.25, 1.6, 2.0, 2.5, 3.2, 4.0, 6.4, 8.0]

FamilyName = "TexturaLibera"
HumanReadableFamilyName = "Textura Libera"

WeightDat = [
	{'Name': 'Thin'      , 'HumanReadableName': 'Thin'       , 'Abbr': 'Thin'   ,},
	{'Name': 'ExtraLight', 'HumanReadableName': 'Extra-Light', 'Abbr': 'ExLight',},
	{'Name': 'Light'     , 'HumanReadableName': 'Light'      , 'Abbr': 'Light'  ,},
	{'Name': 'Book'      , 'HumanReadableName': 'Book'       , 'Abbr': 'Book'   ,},
	{'Name': 'Medium'    , 'HumanReadableName': 'Medium'     , 'Abbr': 'Medium' ,},
	{'Name': 'Demi'      , 'HumanReadableName': 'Demi-Bold'  , 'Abbr': 'Demi'   ,},
	{'Name': 'Bold'      , 'HumanReadableName': 'Bold'       , 'Abbr': 'Bold'   ,},
	{'Name': 'ExtraBold' , 'HumanReadableName': 'Extra-Bold' , 'Abbr': 'ExBold' ,},
	{'Name': 'Black'     , 'HumanReadableName': 'Black'      , 'Abbr': 'Black'  ,},
]

WidthDat = [
	{'Name': 'UC', 'HumanReadableName': ' Ultra-Condensed', 'Abbr': ' UCond'   , 'Panose': 2},
	{'Name': 'XC', 'HumanReadableName': ' Extra-Condensed', 'Abbr': ' ExCond'  , 'Panose': 2},
	{'Name': 'C' , 'HumanReadableName': ' Condensed'      , 'Abbr': ' Cond'    , 'Panose': 3},
	{'Name': 'SC', 'HumanReadableName': ' Semi-Condensed' , 'Abbr': ' SemiCond', 'Panose': 3},
	{'Name': ''  , 'HumanReadableName': ''                , 'Abbr': ''         , 'Panose': 4},
	{'Name': 'SX', 'HumanReadableName': ' Semi-Expanded'  , 'Abbr': ' SemiEx'  , 'Panose': 5},
	{'Name': 'X' , 'HumanReadableName': ' Expanded'       , 'Abbr': ' Expand'  , 'Panose': 5},
	{'Name': 'XX', 'HumanReadableName': ' Extra-Expanded' , 'Abbr': ' ExEx'    , 'Panose': 6},
	{'Name': 'UX', 'HumanReadableName': ' Ultra-Expanded' , 'Abbr': ' UEx'     , 'Panose': 6},
]

WeightCode = None #yet. This will be set later.
WidthCode = None #yet. This will be set later.

# Duplicate a layer
def dupLayer(layer):
	newLayer = fontforge.layer()
	for contour in glyph.layers[layerID]:
		newLayer += contour
	return newLayer

# Check arguments
if len(argv) <= 4:
	stderr.write("Usage: "+argv[0]+" out-sfd font-weight font-width pen-breadth-ratio\n")
	exit(1)
try:
	if not (0 < int(argv[2]) < 1000):
		raise ValueError
except ValueError:
	stderr.write("Error: Font weight must be more than 0 and less than 1000\n")
	exit(2)
try:
	if not (0.5 <= float(argv[3]) <= 2.0):
		raise ValueError
except ValueError:
	stderr.write("Error: Font width must be between 0.5 and 2.0\n")
	exit(2)
try:
	if not (0.1 <= float(argv[4]) <= 0.3):
		raise ValueError
except ValueError:
	stderr.write("Error: Pen breadth ratio must be between 0.1 and 0.3\n")
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

# Set width code
if   float(argv[3]) < 0.5625: WidthCode = 0 # UltraCondensed
elif float(argv[3]) < 0.6875: WidthCode = 1 # ExtraCondensed
elif float(argv[3]) < 0.8125: WidthCode = 2 # Condensed
elif float(argv[3]) < 0.9375: WidthCode = 3 # SemiCondensed
elif float(argv[3]) < 1.0625: WidthCode = 4 # Medium
elif float(argv[3]) < 1.1875: WidthCode = 5 # SemiExpanded
elif float(argv[3]) < 1.3750: WidthCode = 6 # Expanded
elif float(argv[3]) < 1.7500: WidthCode = 7 # ExtraExpanded
else:                         WidthCode = 8 # UltraExpanded

# Pen breadth name
if float(argv[4]) < 0.25:
	FamilyName += "Tenuis"
	HumanReadableFamilyName = " Tenuis"

# Interpolate
WeightInterpol = BaseFont.interpolateFonts((float(argv[2]) - 500.0) / 200.0 + 500.0 * (0.3 - float(argv[4])) / 150.0, BoldFontFile)
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
BaseFont.fontname = FamilyName + WidthDat[WidthCode]['Name'] + "-" + WeightDat[WeightCode]['Name']
BaseFont.familyname = HumanReadableFamilyName + WidthDat[WidthCode]['HumanReadableName']
BaseFont.fullname = HumanReadableFamilyName + WidthDat[WidthCode]['Abbr'] + " " + WeightDat[WeightCode]['Abbr']
BaseFont.weight = WeightDat[WeightCode]['HumanReadableName']
BaseFont.os2_weight = (WeightCode + 1) * 100
BaseFont.os2_width = (WidthCode + 1)
BaseFont.os2_panose = (
	BaseFont.os2_panose[0],
	BaseFont.os2_panose[1],
	WeightCode + 2,
	BaseFont.os2_panose[3],
	WidthDat[WidthCode]['Panose'],
	BaseFont.os2_panose[5],
	BaseFont.os2_panose[6],
	BaseFont.os2_panose[7],
	BaseFont.os2_panose[8],
	BaseFont.os2_panose[9])

# Stroke
for glyph in Interpolated.glyphs():
	if glyph.isWorthOutputting():
		stdout.write("\r" + (" " * 40) + "\r" + glyph.glyphname)
		stdout.flush()
		glyph.round()
		for layerID in range(1, 4):
			if not glyph.layers[layerID].isEmpty():
				for WorkScale in WorkScales:
					layer = dupLayer(glyph.layers[layerID])
					layer.transform(scale(WorkScale))
					penScale = 0.8 if BaseFont[glyph.glyphname].color == 0x00ff00 else 1.0
					layer.stroke(
						"caligraphic",
						float(argv[2]) / 5.0 * WorkScale * penScale,
						float(argv[2]) / 5.0 * float(argv[4]) * WorkScale * penScale,
						rad(penDegrees[layerID]),
						("removeinternal",) if BaseFont[glyph.glyphname].color == 0xffff00 else (None,))
					layer.transform(scale(1.0 / WorkScale))
					allClosed = True
					for contour in layer:
						if not contour.closed:
							allClosed = False
					if allClosed: break
				else:
					raise RuntimeError("Failed to generate the stroke")
				glyph.layers[layerID] = layer
		for layerID in range(2, 4):
			if not glyph.layers[layerID].isEmpty():
				glyph.layers[1] += dupLayer(glyph.layers[layerID])
		glyph.round()
		glyph.removeOverlap()
		glyph.round()
		for layerID in range(1, 4):
			BaseFont[glyph.glyphname].layers[layerID] = dupLayer(glyph.layers[1])
stdout.write("\r" + (" " * 40) + "\rDone\n")
stdout.flush()

# Hinting
BaseFont.selection.none()
for glyph in BaseFont.glyphs():
	if glyph.isWorthOutputting():
		BaseFont.selection.select(("more",), glyph.glyphname)
BaseFont.autoHint()

# Save font
BaseFont.save(argv[1])
