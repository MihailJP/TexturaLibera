#!/usr/bin/env fontforge

from sys import (argv, stdout, stderr, exit)
from math import radians as rad
from psMat import scale, rotate
import fontforge

BaseFontFile      = "TexturaLibera-Medium.sfdir"
BoldFontFile      = "TexturaLibera-Bold.sfdir"

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

WeightCode = None #yet. This will be set later.

# Duplicate a layer
def dupLayer(layer):
	newLayer = fontforge.layer()
	for contour in layer:
		newLayer += contour
	return newLayer

# Break strokes
def breakStrokes(layer):
	newLayer = fontforge.layer()
	for contour in layer:
		newContour = fontforge.contour()
		for point in contour:
			if point.on_curve and (not newContour.isEmpty()):
				newContour += point
				newContour.closed = False
				newLayer += newContour
				newContour = fontforge.contour()
			newContour += point
		if contour.closed:
			newContour += contour[0]
			newContour.closed = False
			newLayer += newContour
	return newLayer

# Check arguments
if len(argv) <= 4:
	stderr.write("Usage: "+argv[0]+" out-sfd font-weight reserved pen-breadth-ratio\n")
	exit(1)
try:
	if not (0 < int(argv[2]) < 1000):
		raise ValueError
except ValueError:
	stderr.write("Error: Font weight must be more than 0 and less than 1000\n")
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

# Pen breadth name
if float(argv[4]) < 0.25:
	FamilyName += "Tenuis"
	HumanReadableFamilyName += " Tenuis"

# Interpolate
Interpolated = BaseFont.interpolateFonts((float(argv[2]) - 500.0) / 200.0 + 500.0 * (0.3 - float(argv[4])) / 150.0, BoldFontFile)

# Set output font properties
BaseFont.strokedfont = False
BaseFont.fontname = FamilyName + "-" + WeightDat[WeightCode]['Name']
BaseFont.familyname = HumanReadableFamilyName
BaseFont.fullname = HumanReadableFamilyName + " " + WeightDat[WeightCode]['Abbr']
BaseFont.weight = WeightDat[WeightCode]['HumanReadableName']
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
		stdout.write("\r" + (" " * 40) + "\r" + glyph.glyphname)
		stdout.flush()
		glyph.transform(rotate(rad(45)))
		glyph.addExtrema()
		glyph.transform(rotate(rad(-45)))
		glyph.round()
		for layerID in range(1, 4):
			if not glyph.layers[layerID].isEmpty():
				for WorkScale in WorkScales:
					layer = breakStrokes(glyph.layers[layerID]) if layerID != 2 and BaseFont[glyph.glyphname].color != 0xffff00 else dupLayer(glyph.layers[layerID])
					layer.transform(scale(WorkScale))
					penScale = 0.8 if BaseFont[glyph.glyphname].color == 0x00ff00 else 1.0
					layer.stroke(
						"caligraphic",
						float(argv[2]) / 5.0 * WorkScale * penScale,
						float(argv[2]) / 5.0 * float(argv[4]) * WorkScale * penScale,
						rad(penDegrees[layerID]),
						removeinternal = (BaseFont[glyph.glyphname].color == 0xffff00),
						extrema = False,
						simplify = (glyph.glyphname == "FleuronCenter"),
						removeoverlap = "contour")
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
		BaseFont[glyph.glyphname].layers[1] = dupLayer(glyph.layers[1])
		for layerID in range(2, 4):
			BaseFont[glyph.glyphname].layers[layerID] = fontforge.layer()
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
