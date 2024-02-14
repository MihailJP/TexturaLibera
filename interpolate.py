#!/usr/bin/env fontforge

from sys import argv
import fontforge

font1 = fontforge.open(argv[2])
font = font1.interpolateFonts(float(argv[4]), argv[3])
for lookup in font1.gsub_lookups:
    font.importLookups(font1, lookup)
for lookup in font1.gpos_lookups:
    font.importLookups(font1, lookup)
font.encoding = "UnicodeBmp"
font.familyname = font1.familyname
font.save(argv[1])
