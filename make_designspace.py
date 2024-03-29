#!/usr/bin/env python3

import os, re
from sys import argv
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor, AxisLabelDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Textura Libera"

weightList = [
	(100, "Thin"),
	(200, "Extra Light"),
	(300, "Light"),
	(400, None),
	(500, "Medium"),
	(600, "DemiBold"),
	(700, "Bold"),
	(800, "Extra Bold"),
	(900, "Black"),
]
widthList = [
	(100,   None),
	( 87.5, "Semi Condensed"),
	( 75,   "Condensed"),
	( 62.5, "Extra Condensed"),
	( 50,   "Ultra Condensed"),
	(112.5, "Semi Expanded"),
	(125,   "Expanded"),
	(150,   "Extra Expanded"),
	(200,   "Ultra Expanded"),
]

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 1000
a1.minimum = 1
a1.default = 400
a1.name = "Weight"
a1.tag = "wght"
a1.axisLabels = []
for weight in weightList:
	l1 = AxisLabelDescriptor(
		name = "Regular" if weight[1] is None else weight[1],
		userValue = weight[0],
	)
	if weight[0] == 400:
		l1.elidable = True
		l1.linkedUserValue = 700
	a1.axisLabels = a1.axisLabels + [l1]
a1.axisOrdering = 1
doc.addAxis(a1)

a2 = AxisDescriptor()
a2.maximum = 200
a2.minimum = 50
a2.default = 100
a2.name = "Width"
a2.tag = "wdth"
a2.axisLabels = []
for width in widthList:
	l1 = AxisLabelDescriptor(
		name = "" if width[1] is None else width[1],
		userValue = width[0],
	)
	a2.axisLabels = a2.axisLabels + [l1]
a2.axisOrdering = 0
doc.addAxis(a2)

#---------
# masters
#---------

sourceList = [
	("Regular",           argv[ 2],  400, 100),
	("Minimum",           argv[ 3],    1, 100),
	("Maximum",           argv[ 4], 1000, 100),
	("Expanded",          argv[ 5],  400, 200),
	("Expanded Minimum",  argv[ 6],    1, 200),
	("Expanded Maximum",  argv[ 7], 1000, 200),
	("Condensed",         argv[ 8],  400,  50),
	("Condensed Minimum", argv[ 9],    1,  50),
	("Condensed Maximum", argv[10], 1000,  50),
]

for source in sourceList:
	s0 = SourceDescriptor()
	s0.path = source[1]
	s0.name = familyName + " " + source[0]
	s0.familyName = familyName
	s0.styleName = source[0]
	s0.location = dict(Weight=source[2], Width=source[3])
	if source[2] == a1.default and source[3] == a2.default:
		s0.copyLib = True
		s0.copyInfo = True
		s0.copyGroups = True
		s0.copyFeatures = True
	doc.addSource(s0)

#----------
# instances
#----------

for width in widthList:
	for weight in weightList:
		i1 = InstanceDescriptor()
		styleNameList = [i for i in [width[1], weight[1]] if i is not None]
		i1.familyName = familyName
		i1.styleName = " ".join(styleNameList)
		if i1.styleName == "":
			i1.styleName = "Regular"
		i1.name = i1.familyName + " " + i1.styleName
		i1.postscriptFontName = (i1.familyName + "-" + i1.styleName).replace(" ", "")
		i1.path = i1.postscriptFontName + ".ufo"
		i1.designLocation = dict(Weight=weight[0], Width=width[0])
		doc.addInstance(i1)


#--------
# saving
#--------

path = os.path.join(root, argv[1])
doc.write(path)
