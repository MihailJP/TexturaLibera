.SUFFIXES: .recipe .sfd .ttf .otf .woff
SRCFONTS = $(wildcard *.recipe)
SFDFILES = $(SRCFONTS:.recipe=.sfd)
TTFONTS = $(SRCFONTS:.recipe=.ttf)
OTFONTS = $(SRCFONTS:.recipe=.otf)
WOFFONTS = $(SRCFONTS:.recipe=.woff)
TARGETS = $(TTFONTS) $(OTFONTS) $(WOFFONTS)
DOCUMENTS = LICENSE NEWS README.md TexturaLibera-Specimen.pdf
DISTTYPE = zip

VERSION = 0.2.0

.PHONY: all clean dist ttf otf woff version

all: $(TARGETS)

.recipe.sfd: TexturaLibera-Medium.sfdir TexturaLibera-Bold.sfdir TexturaLibera-Condensed.sfdir TexturaLibera-Expanded.sfdir
	sh $< $@
.sfd.ttf:
	./makefont.py $< $@
.sfd.otf:
	./makefont.py $< $@
.sfd.woff:
	./makefont.py $< $@

ttf: $(TTFONTS)
otf: $(OTFONTS)
woff: $(WOFFONTS)

dist: TexturaLibera-TTF-$(VERSION).$(DISTTYPE) TexturaLibera-OTF-$(VERSION).$(DISTTYPE) TexturaLibera-WOFF-$(VERSION).$(DISTTYPE)

version:
	for i in $(wildcard TexturaLibera-*.sfdir); do sed -i -e '/^Version:/c Version: $(VERSION)' $$i/font.props; done

TexturaLibera.css:
	./makecss.rb > $@

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
	rm -f $(SFDFILES) $(TTFONTS) $(OTFONTS) $(WOFFONTS) TexturaLibera-TTF-* TexturaLibera-OTF-* TexturaLibera-WOFF-* TexturaLibera.css 
