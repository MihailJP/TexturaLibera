.SUFFIXES: .sfdir .ttf .otf
SRCFONTS = $(wildcard *.sfdir)
TTFONTS = $(SRCFONTS:.sfdir=.ttf)
OTFONTS = $(SRCFONTS:.sfdir=.otf)
TARGETS = $(TTFONTS)
DISTFILE = txlibera.zip
DOCUMENTS = LICENSE README.md

.PHONY: all clean dist ttf otf

all: $(TARGETS)

.sfdir.ttf:
	./makefont.py $< $@
.sfdir.otf:
	./makefont.py $< $@

ttf: $(TTFONTS)
otf: $(OTFONTS)

dist: $(DISTFILE)

txlibera.zip: $(TARGETS) $(DOCUMENTS) 
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
txlibera.tar.gz: $(TARGETS) $(DOCUMENTS) 
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
txlibera.tar.bz2: $(TARGETS) $(DOCUMENTS) 
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
txlibera.tar.xz: $(TARGETS) $(DOCUMENTS) 
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

clean:
	rm -f $(TTFONTS) $(OTFONTS) txlibera.zip txlibera.tar.*
