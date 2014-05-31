.SUFFIXES: .recipe .sfd .ttf .otf .woff
SRCFONTS = $(wildcard *.recipe)
SFDFILES = $(SRCFONTS:.recipe=.sfd)
TTFONTS = $(SRCFONTS:.recipe=.ttf)
OTFONTS = $(SRCFONTS:.recipe=.otf)
WOFFONTS = $(SRCFONTS:.recipe=.woff)
TARGETS = $(TTFONTS) $(OTFONTS) $(WOFFONTS)
DOCUMENTS = FONTLOG.txt LICENSE README.md TexturaLiberaSP-Specimen.pdf
DISTTYPE = zip

VERSION = 0.2.2

.PHONY: all clean dist ttf otf woff version

all: $(IMPORTED_SCRIPTS) $(TARGETS)

.recipe.sfd: TexturaLiberaSP-Medium.sfdir TexturaLiberaSP-Bold.sfdir
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

dist: TexturaLiberaSP-TTF-$(VERSION).$(DISTTYPE) TexturaLiberaSP-OTF-$(VERSION).$(DISTTYPE) TexturaLiberaSP-WOFF-$(VERSION).$(DISTTYPE)

version:
	for i in $(wildcard TexturaLiberaSP-*.sfdir); do sed -i -e '/^Version:/c Version: $(VERSION)' $$i/font.props; done

TexturaLiberaSP.css:
	./makecss.rb > $@

TexturaLiberaSP-TTF-$(VERSION).zip: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
TexturaLiberaSP-TTF-$(VERSION).tar.gz: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
TexturaLiberaSP-TTF-$(VERSION).tar.bz2: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
TexturaLiberaSP-TTF-$(VERSION).tar.xz: $(TTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

TexturaLiberaSP-OTF-$(VERSION).zip: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
TexturaLiberaSP-OTF-$(VERSION).tar.gz: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
TexturaLiberaSP-OTF-$(VERSION).tar.bz2: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
TexturaLiberaSP-OTF-$(VERSION).tar.xz: $(OTFONTS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

TexturaLiberaSP-WOFF-$(VERSION).zip: $(WOFFONTS) $(DOCUMENTS) TexturaLiberaSP.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
TexturaLiberaSP-WOFF-$(VERSION).tar.gz: $(WOFFONTS) $(DOCUMENTS) TexturaLiberaSP.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
TexturaLiberaSP-WOFF-$(VERSION).tar.bz2: $(WOFFONTS) $(DOCUMENTS) TexturaLiberaSP.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
TexturaLiberaSP-WOFF-$(VERSION).tar.xz: $(WOFFONTS) $(DOCUMENTS) TexturaLiberaSP.css
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

clean:
	rm -f $(SFDFILES) $(TTFONTS) $(OTFONTS) $(WOFFONTS) TexturaLiberaSP-TTF-* TexturaLiberaSP-OTF-* TexturaLiberaSP-WOFF-* TexturaLiberaSP.css LICENSE *.pyc
