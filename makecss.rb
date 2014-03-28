#!/usr/bin/env ruby

print <<FINIS
/* This is the @font-face definition file for Textura Libera web fonts. */

/*
 * Usage:
 * 
 * 1. Put this stylesheet into an HTML directory of your server
 *    together with the woff files.
 * 2. Link this stylesheet from your hypertext or @import to your stylesheet.
 */

FINIS

def fontface(widthSymbol, widthTxt, widthProp, weight)
	weightName = {
		100 => 'Thin',
		200 => 'ExtraLight',
		300 => 'Light',
		400 => 'Book',
		500 => 'Medium',
		600 => 'Demi',
		700 => 'Bold',
		800 => 'ExtraBold',
		900 => 'Black'}
	print <<FINIS
@font-face {
	font-family: 'Textura Libera#{widthTxt}';
	src: url('TexturaLibera#{widthSymbol}-#{weightName[weight]}.woff');
	font-variant: normal;
	font-stretch: #{widthProp};
	font-weight: #{weight};
	font-style: normal;
}
FINIS
end

for weight in [100, 200, 300, 400, 500, 600, 700, 800, 900]
	fontface("", "", "normal", weight)
end
print "\n"
for weight in [100, 200, 300, 400, 500, 600]
	fontface("C", " Condensed", "condensed", weight)
end
print "\n"
for weight in [100, 200, 300, 400, 500, 600, 700, 800, 900]
	fontface("X", " Expanded", "expanded", weight)
end
print "\n"
