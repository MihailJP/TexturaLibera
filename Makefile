.SUFFIXES: .recipe .sfd .ttf .otf .woff .ufo
STROKEFONTS = TexturaLibera-Medium.sfdir TexturaLibera-Bold.sfdir TexturaLibera-Condensed.sfdir TexturaLibera-Expanded.sfdir
SFDFILES = TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd TexturaLibera-Minimum.sfd TexturaLibera-Book.sfd TexturaLibera-Maximum.sfd
UFOS = $(SFDFILES:.sfd=.ufo)
TARGETS = variable_ttf/TexturaLibera.ttf
DOCUMENTS = FONTLOG.txt LICENSE README.md TexturaLibera-Specimen.pdf
DISTTYPE = zip

VERSION = 0.2.2

.PHONY: all clean dist ttf otf woff version

all: $(TARGETS)

TexturaLibera-ExtraLight.sfd: $(STROKEFONTS)
	./make-outline.py $@ 200 1 .3
TexturaLibera-Light.sfd: $(STROKEFONTS)
	./make-outline.py $@ 300 1 .3
TexturaLibera-Minimum.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ -1.99
TexturaLibera-Book.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ 2
TexturaLibera-Maximum.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ 8

.sfd.ufo:
	./makefont.py $< $@ && sed -i~ -f fix_features.sed $@/features.fea

TexturaLibera.designspace: TexturaLibera-Book.ufo TexturaLibera-Minimum.ufo TexturaLibera-Maximum.ufo
	./make_designspace.py $@ $^

variable_ttf/TexturaLibera.ttf: TexturaLibera.designspace
	fontmake -m $< -o variable

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
	rm -f $(SFDFILES) TexturaLibera.designspace TexturaLibera-TTF-* TexturaLibera-OTF-* TexturaLibera-WOFF-* TexturaLibera.css
	rm -rf $(UFOS) variable_ttf
