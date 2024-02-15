.SUFFIXES: .recipe .sfd .ttf .otf .woff .ufo
STROKEFONTS = TexturaLibera-Medium.sfdir TexturaLibera-Bold.sfdir
SFDFILES = TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd \
           TexturaLibera-Book.sfd TexturaLibera-Minimum.sfd TexturaLibera-Maximum.sfd \
           TexturaLibera-ExtraLight1.sfd TexturaLibera-Light1.sfd \
           TexturaLibera-BookExpanded.sfd TexturaLibera-ExtraLightExpanded.sfd TexturaLibera-LightExpanded.sfd \
           TexturaLibera-MinimumExpanded.sfd TexturaLibera-MaximumExpanded.sfd\
           TexturaLibera-BookCondensed.sfd TexturaLibera-ExtraLightCondensed.sfd TexturaLibera-LightCondensed.sfd \
           TexturaLibera-MinimumCondensed.sfd TexturaLibera-MaximumCondensed.sfd
UFOS = $(SFDFILES:.sfd=.ufo)
TARGETS = variable_ttf/TexturaLibera-VF.ttf
DOCUMENTS = FONTLOG.txt LICENSE README.md
DISTTYPE = zip

VERSION = 1.0.0

.PHONY: all clean dist ttf otf woff version

all: $(TARGETS)

TexturaLibera-ExtraLight.sfd: $(STROKEFONTS)
	./make-outline.py $@ 200 1 .3
TexturaLibera-Light.sfd: $(STROKEFONTS)
	./make-outline.py $@ 300 1 .3

TexturaLibera-ExtraLight1.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ -1
TexturaLibera-Light1.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ -0.5
TexturaLibera-ExtraLightExpanded.sfd: TexturaLibera-ExtraLight1.sfd
	./width.py $@ $< 2
TexturaLibera-LightExpanded.sfd: TexturaLibera-Light1.sfd
	./width.py $@ $< 2

TexturaLibera-ExtraLightCondensed.sfd: TexturaLibera-ExtraLight.sfd
	./width.py $@ $< 0.5
TexturaLibera-LightCondensed.sfd: TexturaLibera-Light.sfd
	./width.py $@ $< 0.5

TexturaLibera-Minimum.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ -1.99
TexturaLibera-Book.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ 2
TexturaLibera-Maximum.sfd: TexturaLibera-ExtraLight.sfd TexturaLibera-Light.sfd
	./interpolate.py $@ $^ 8
TexturaLibera-MinimumExpanded.sfd: TexturaLibera-ExtraLightExpanded.sfd TexturaLibera-LightExpanded.sfd
	./interpolate.py $@ $^ -1.99
TexturaLibera-BookExpanded.sfd: TexturaLibera-ExtraLightExpanded.sfd TexturaLibera-LightExpanded.sfd
	./interpolate.py $@ $^ 2
TexturaLibera-MaximumExpanded.sfd: TexturaLibera-ExtraLightExpanded.sfd TexturaLibera-LightExpanded.sfd
	./interpolate.py $@ $^ 8
TexturaLibera-MinimumCondensed.sfd: TexturaLibera-ExtraLightCondensed.sfd TexturaLibera-LightCondensed.sfd
	./interpolate.py $@ $^ -1.99
TexturaLibera-BookCondensed.sfd: TexturaLibera-ExtraLightCondensed.sfd TexturaLibera-LightCondensed.sfd
	./interpolate.py $@ $^ 2
TexturaLibera-MaximumCondensed.sfd: TexturaLibera-ExtraLightCondensed.sfd TexturaLibera-LightCondensed.sfd
	./interpolate.py $@ $^ 8

.sfd.ufo:
	./makefont.py $< $@ && sed -i~ -f fix_features.sed $@/features.fea

TexturaLibera.designspace: TexturaLibera-Book.ufo TexturaLibera-Minimum.ufo TexturaLibera-Maximum.ufo TexturaLibera-BookExpanded.ufo TexturaLibera-MinimumExpanded.ufo TexturaLibera-MaximumExpanded.ufo TexturaLibera-BookCondensed.ufo TexturaLibera-MinimumCondensed.ufo TexturaLibera-MaximumCondensed.ufo
	./make_designspace.py $@ $^

variable_ttf/TexturaLibera-VF.ttf: TexturaLibera.designspace
	fontmake -m $< -o variable

dist: TexturaLibera-Variabilis-$(VERSION).$(DISTTYPE)

version:
	for i in $(wildcard TexturaLibera-*.sfdir); do sed -i -e '/^Version:/c Version: $(VERSION)' $$i/font.props; done

TexturaLibera-Variabilis-$(VERSION).zip: $(TARGETS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && zip -m9r $@ txlibera
TexturaLibera-Variabilis-$(VERSION).tar.gz: $(TARGETS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | gzip -9 - > $@) && rm -rf txlibera
TexturaLibera-Variabilis-$(VERSION).tar.bz2: $(TARGETS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | bzip2 -z9 - > $@) && rm -rf txlibera
TexturaLibera-Variabilis-$(VERSION).tar.xz: $(TARGETS) $(DOCUMENTS)
	rm -f $@; rm -rf txlibera
	mkdir txlibera && cp $^ txlibera && (tar cO txlibera | xz -z9 - > $@) && rm -rf txlibera

clean:
	rm -f $(SFDFILES) TexturaLibera.designspace TexturaLibera-Variabilis-*
	rm -rf $(UFOS) variable_ttf
