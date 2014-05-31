#!/usr/bin/env fontforge

from sys import (argv, stderr, exit)
import fontforge

if len(argv) <= 2:
	stderr.write("Usage: "+argv[0]+" in-sfd out-font\n")
	exit(1)

font = fontforge.open(argv[1])
font.generate(argv[2])
