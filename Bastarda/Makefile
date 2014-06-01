.SUFFIXES: .recipe .sfd .ttf .otf .woff
SRCFONTS = $(wildcard *.recipe)
SFDFILES = $(SRCFONTS:.recipe=.sfd)
TTFONTS = $(SRCFONTS:.recipe=.ttf)
OTFONTS = $(SRCFONTS:.recipe=.otf)
WOFFONTS = $(SRCFONTS:.recipe=.woff)
TARGETS = $(TTFONTS) $(OTFONTS) $(WOFFONTS)
DOCUMENTS = FONTLOG.txt LICENSE README.md BastardaLibera-Specimen.pdf
DISTTYPE = zip

VERSION = 0.2.2

.PHONY: all clean dist ttf otf woff version

all: $(IMPORTED_SCRIPTS) $(TARGETS)

.recipe.sfd: BastardaLibera-Medium.sfdir BastardaLibera-Bold.sfdir
	sh $< $@
.sfd.ttf:
	./makefont.py $< $@
.sfd.otf:
	./makefont.py $< $@
.sfd.woff:
	./makefont.py $< $@

LICENSE:
	ln ../$@ .

ttf: $(TTFONTS)
otf: $(OTFONTS)
woff: $(WOFFONTS)

dist: BastardaLibera-TTF-$(VERSION).$(DISTTYPE) BastardaLibera-OTF-$(VERSION).$(DISTTYPE) BastardaLibera-WOFF-$(VERSION).$(DISTTYPE)

version:
	for i in $(wildcard BastardaLibera-*.sfdir); do sed -i -e '/^Version:/c Version: $(VERSION)' $$i/font.props; done

BastardaLibera.css:
	./makecss.rb > $@

BastardaLibera-TTF-$(VERSION).zip: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
BastardaLibera-TTF-$(VERSION).tar.gz: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
BastardaLibera-TTF-$(VERSION).tar.bz2: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
BastardaLibera-TTF-$(VERSION).tar.xz: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

BastardaLibera-OTF-$(VERSION).zip: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
BastardaLibera-OTF-$(VERSION).tar.gz: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
BastardaLibera-OTF-$(VERSION).tar.bz2: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
BastardaLibera-OTF-$(VERSION).tar.xz: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

BastardaLibera-WOFF-$(VERSION).zip: $(WOFFONTS) $(DOCUMENTS) BastardaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
BastardaLibera-WOFF-$(VERSION).tar.gz: $(WOFFONTS) $(DOCUMENTS) BastardaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
BastardaLibera-WOFF-$(VERSION).tar.bz2: $(WOFFONTS) $(DOCUMENTS) BastardaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
BastardaLibera-WOFF-$(VERSION).tar.xz: $(WOFFONTS) $(DOCUMENTS) BastardaLibera.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

clean:
	rm -f $(SFDFILES) $(TTFONTS) $(OTFONTS) $(WOFFONTS) BastardaLibera-TTF-* BastardaLibera-OTF-* BastardaLibera-WOFF-* BastardaLibera.css LICENSE *.pyc
