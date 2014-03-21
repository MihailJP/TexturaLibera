.SUFFIXES: .sfdir .ttf .otf
SRCFONTS = $(wildcard *.sfdir)
TTFONTS = $(SRCFONTS:.sfdir=.ttf)

.PHONY: all clean

all: $(TTFONTS)

.sfdir.ttf:
	./makefont.py $< $@

clean:
	rm -f $(TTFONTS)
