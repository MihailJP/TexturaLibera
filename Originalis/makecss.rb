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
	require "#{Dir::pwd}/cssparam.rb"
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
	font-family: '#{FontFamilyName}#{widthTxt}#{FontFamilySuffix}';
	src: url('#{FontFilePrefix}#{widthSymbol}#{FontFileSuffix}-#{weightName[weight]}.woff');
	font-variant: normal;
	font-stretch: #{widthProp};
	font-weight: #{weight};
	font-style: normal;
}
FINIS
end

require "#{Dir::pwd}/cssparam.rb"

for weight in WeightsOfNormalWidth
	fontface("", "", "normal", weight)
end
print "\n"
for weight in WeightsOfCondensedWidth
	fontface("C", " Condensed", "condensed", weight)
end
print "\n"
for weight in WeightsOfExpandedWidth
	fontface("X", " Expanded", "expanded", weight)
end
print "\n"


for weight in WeightsOfNormalWidth
	fontface("Tenuis", " Tenuis", "normal", weight)
end
print "\n"
for weight in WeightsOfCondensedWidth
	fontface("TenuisC", " Tenuis Condensed", "condensed", weight)
end
print "\n"
for weight in WeightsOfExpandedWidth
	fontface("TenuisX", " Tenuis Expanded", "expanded", weight)
end
print "\n"
