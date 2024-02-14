#!/usr/bin/env python3

import os, re
from sys import argv
from fontTools.designspaceLib import DesignSpaceDocument, AxisDescriptor, SourceDescriptor, InstanceDescriptor

root = os.getcwd()
doc = DesignSpaceDocument()

familyName = "Textura Libera Variabilis"

#------
# axes
#------

a1 = AxisDescriptor()
a1.maximum = 1000
a1.minimum = 1
a1.default = 400
a1.name = "Weight"
a1.tag = "wght"
doc.addAxis(a1)

#---------
# masters
#---------

s0 = SourceDescriptor()
s0.path = argv[2]
s0.name = "master.TexturaLibera.Book.0"
s0.familyName = familyName
s0.styleName = "Book"
s0.location = dict(Weight=400)
s0.copyLib = True
s0.copyInfo = True
s0.copyGroups = True
s0.copyFeatures = True
doc.addSource(s0)

s1 = SourceDescriptor()
s1.path = argv[3]
s1.name = "master.TexturaLibera.Minimum.0"
s1.familyName = familyName
s1.styleName = "Minimum"
s1.location = dict(Weight=1)
doc.addSource(s1)

s2 = SourceDescriptor()
s2.path = argv[4]
s2.name = "master.TexturaLibera.Maximum.0"
s2.familyName = familyName
s2.styleName = "Maximum"
s2.location = dict(Weight=1000)
doc.addSource(s2)

#----------
# instances
#----------

i1 = InstanceDescriptor()
i1.styleName = "Thin"
i1.designLocation = dict(Weight=100)
doc.addInstance(i1)

i2 = InstanceDescriptor()
i2.styleName = "Extra Light"
i2.designLocation = dict(Weight=200)
doc.addInstance(i2)

i3 = InstanceDescriptor()
i3.styleName = "Light"
i3.designLocation = dict(Weight=300)
doc.addInstance(i3)

i4 = InstanceDescriptor()
i4.styleName = "Regular"
i4.designLocation = dict(Weight=400)
doc.addInstance(i4)

i5 = InstanceDescriptor()
i5.styleName = "Medium"
i5.designLocation = dict(Weight=500)
doc.addInstance(i5)

i6 = InstanceDescriptor()
i6.styleName = "DemiBold"
i6.designLocation = dict(Weight=600)
doc.addInstance(i6)

i7 = InstanceDescriptor()
i7.styleName = "Bold"
i7.designLocation = dict(Weight=700)
doc.addInstance(i7)

i8 = InstanceDescriptor()
i8.styleName = "Extra Bold"
i8.designLocation = dict(Weight=800)
doc.addInstance(i8)

i9 = InstanceDescriptor()
i9.styleName = "Black"
i9.designLocation = dict(Weight=900)
doc.addInstance(i9)


#--------
# saving
#--------

path = os.path.join(root, argv[1])
doc.write(path)
