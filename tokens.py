from nltk.tokenize import MWETokenizer

#list of regular expressions
RE_identifiers = "(^[a-zA-Z][a-zA-Z0-9_]*$)"
# RE_literals = "(^-?[1-9][0-9]*$|^0$)|(^-?[0-9]*\.[0-9]+$)^WIN$|^FAIL$)"
RE_literal_numbr = "(^-?[1-9][0-9]*$|^0$)"
RE_literal_numbar = "(^-?[0-9]*\.[0-9]+$)"
# RE_literal_yarn = "(^”.*”$)"
RE_literal_troof = "(^WIN$|^FAIL$)"
RE_data_type = "(^(TROOF)$|^(NUMBR)$|^(NUMBAR)$|^(YARN)$|^(TYPE)$)"
RE_hai_kw = "(^HAI$)"
RE_kthxbye_kw = "(^KTHXBYE$)"
RE_btw_kw = "(^BTW$)"
RE_obtw_kw = "(^OBTW$)"
RE_tldr_kw =  "(^TLDR$)"
RE_ihasa_kw = "(^I HAS A$)"
RE_itz_kw = "(^ITZ$)"
RE_r_kw = "(^R$)"
RE_it_kw = "^IT$"
RE_an_kw = "^AN$"
RE_sumof_kw = "SUM OF"
RE_diffof_kw = "DIFF OF"
RE_produktof_kw = "PRODUKT OF"
RE_quoshuntof_kw = "QUOSHUNT OF"
RE_modof_kw = "MOD OF"
RE_biggrof_kw = "BIGGR OF"
RE_smallrof_kw = "SMALLR OF"
RE_bothof_kw = "BOTH OF"
RE_eitherof_kw = "EITHER OF"
RE_wonof_kw = "WON OF"
RE_not_kw = "NOT"
RE_anyof_kw = "ANY OF"
RE_allof_kw = "ALL OF"
RE_bothsaem_kw = "(^BOTH SAEM$)"
RE_diffrint_kw = "(^DIFFRINT$)"
RE_smoosh_kw = "(^SMOOSH$)"
RE_maek_kw = "(^MAEK$)"
RE_a_kw = "(^A$)"
RE_isnowa_kw = "(^IS NOW A$)"
RE_visible_kw = "(^VISIBLE$)"
RE_gimmeh_kw = "(^GIMMEH$)"
RE_orly_kw = "(^O RLY\?$)"
RE_yarly_kw = "(^YA RLY$)"
RE_mebbe_kw = "(^MEBBE$)"
RE_nowai_kw = "(^NO WAI$)"
RE_oic_kw = "(^OIC$)"
RE_wtf_kw = "(^WTF\?$)"
RE_omg_kw = "(^OMG$)"
RE_omgwtf_kw = "(^OMGWTF$)"
RE_iminyr_kw = "(^IM IN YR$)"
RE_uppin_kw = "(^UPPIN$)"
RE_nerfin_kw = "(^NERFIN$)"
RE_yr_kw = "(^YR$)"
RE_til_kw = "(^TIL$)"
RE_wile_kw = "(^WILE$)"
RE_imouttayr_kw = "(^IM OUTTA YR$)"
RE_delimiters = "\""          # string delimiter lang ba meron sa lolcode?


# Multi-word lexemes
mwe = MWETokenizer([("I", "HAS", "A"), ("SUM", "OF"), ("DIFF", "OF"),
                    ("PRODUKT", "OF"), ("QUOSHUNT", "OF"), ("MOD", "OF"),
                    ("BIGGR", "OF"), ("SMALLR", "OF"), ("BOTH", "OF"),
                    ("EITHER", "OF"), ("WON", "OF"), ("ANY", "OF"),
                    ("BOTH", "SAEM"), ("IS", "NOW", "A"), ("O", "RLY?"),
                    ("YA", "RLY"), ("NO", "WAI"), ("IM", "IN", "YR"),
                    ("IM", "OUTTA", "YR")], separator = " ")