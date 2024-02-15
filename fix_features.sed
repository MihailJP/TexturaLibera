/^lookup .*Removedotfromiandj/,/^} .*Removedotfromiandj;/ c\
lookup dotlessforms {\
  lookupflag 0;\
    sub \\i  by \\dotlessi;\
    sub \\j  by \\dotlessj;\
    sub \\v  by \\v.alt;\
    sub \\w  by \\w.alt;\
    sub \\iogonek  by \\dotlessiogonek;\
    sub \\vdotbelow  by \\vdotbelow.alt;\
    sub \\wdotbelow  by \\wdotbelow.alt;\
    sub \\idotbelow  by \\dotlessidotbelow;\
    sub \\ibreveinvertedbelow by \\dotlessibreveinvertedbelow;\
	sub \\jdotbelow  by \\dotlessjdotbelow;\
} dotlessforms;\
\
lookup Removedotfromiandj {\
  lookupflag 0;\
    @cc3_match_1 = [\\i \\j \\v \\w \\iogonek \\vdotbelow \\wdotbelow \\idotbelow \\ibreveinvertedbelow\
	\\jdotbelow ];\
    @cc3_match_2 = [\\gravecmb \\acutecmb \\circumflexcmb \\tildecmb \\macroncmb \\brevecmb \
	\\dotaccentcmb \\dieresiscmb \\hookcmb \\ringcmb \\hungarumlautcmb \
	\\caroncmb \\acmb \\ecmb \\icmb \\ocmb \\ucmb \\ccmb \\dcmb \\hcmb \\mcmb \\rcmb \\tcmb \
	\\vcmb \\xcmb \\wcmb ];\
    sub @cc3_match_1' lookup dotlessforms @cc3_match_2';\
} Removedotfromiandj;
s/lookup .*Removedotfromiandj;/lookup Removedotfromiandj;/
