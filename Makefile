.SUFFIXES: .sfdir .ttf .otf .woff
SRCFONTS = $(wildcard *.sfdir)
TTFONTS = $(SRCFONTS:.sfdir=.ttf)
OTFONTS = $(SRCFONTS:.sfdir=.otf)
WOFFONTS = $(SRCFONTS:.sfdir=.woff)
TARGETS = $(TTFONTS) $(OTFONTS) $(WOFFONTS)
DOCUMENTS = LICENSE NEWS README.md TexturaLibera-Specimen.pdf
DISTTYPE = zip

VERSION = 0.1.0

.PHONY: all clean dist ttf otf woff

all: $(TARGETS)

.sfdir.ttf:
	./makefont.py $< $@
.sfdir.otf:
	./makefont.py $< $@
.sfdir.woff:
	./makefont.py $< $@

ttf: $(TTFONTS)
otf: $(OTFONTS)
woff: $(WOFFONTS)

dist: TexturaLibera-TTF-$(VERSION).$(DISTTYPE) TexturaLibera-OTF-$(VERSION).$(DISTTYPE) TexturaLibera-WOFF-$(VERSION).$(DISTTYPE)

TexturaLibera-TTF-$(VERSION).zip: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
TexturaLibera-TTF-$(VERSION).tar.gz: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
TexturaLibera-TTF-$(VERSION).tar.bz2: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
TexturaLibera-TTF-$(VERSION).tar.xz: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

TexturaLibera-OTF-$(VERSION).zip: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
TexturaLibera-OTF-$(VERSION).tar.gz: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
TexturaLibera-OTF-$(VERSION).tar.bz2: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
TexturaLibera-OTF-$(VERSION).tar.xz: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

TexturaLibera-WOFF-$(VERSION).zip: $(WOFFONTS) $(DOCUMENTS) TexturaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
TexturaLibera-WOFF-$(VERSION).tar.gz: $(WOFFONTS) $(DOCUMENTS) TexturaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
TexturaLibera-WOFF-$(VERSION).tar.bz2: $(WOFFONTS) $(DOCUMENTS) TexturaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
TexturaLibera-WOFF-$(VERSION).tar.xz: $(WOFFONTS) $(DOCUMENTS) TexturaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

clean:
	rm -f $(TTFONTS) $(OTFONTS) $(WOFFONTS) TexturaLibera-TTF-* TexturaLibera-OTF-* TexturaLibera-WOFF-* 
