# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:14:43 2021

@author: Mark, Lara
"""


import re
from nltk.tokenize import MWETokenizer
from nltk.tokenize import wordpunct_tokenize
from tkinter import Tk
from tkinter import filedialog

root = Tk()
root.title = ('Main Window')
root.filename = filedialog.askopenfilename(title="Select Folder", filetypes= (("LOLCode files","*.lol"),
                                          ("All files","*.*")))

file = open(root.filename, 'r')
program = file.read()
source_code = program.split('\n')
# print(source_code)

#list of regular expressions
RE_identifiers = "(^[a-zA-Z][a-zA-Z0-9_]*$)|(^[a-zA-Z][a-zA-Z0-9_]*$)|(^[a-zA-Z][a-zA-Z0-9_]*$)"
RE_literals = "(^-?[1-9][0-9]*$|^0$)|(^-?[0-9]*\.[0-9]+$)|(^”.*”$)|(^WIN$|^FAIL$)|(^(TROOF)$|^(NUMBR)$|^(NUMBAR)$|^(YARN)$|^(TYPE)$)"
RE_hai_kw = "(^HAI$)"
RE_kthxbye_kw = "(^KTHXBYE$)"
RE_btw_kw = "(^BTW$)"
RE_obtw_kw = "(^OBTW$)"
RE_tldr_kw =  "(^TLDR$)"
RE_ihasa_kw = "(^I HAS A$)"
RE_itz_kw = "(^ITZ$)"
RE_r_kw = "(^R$)"
RE_sumof_kw = "(^SUM OF$)"
RE_diffof_kw = "(^DIFF OF$)"
RE_produktof_kw = "(^PRODUKT OF$)"
RE_quoshuntof_kw = "(^QUOSHUNT OF$)"
RE_modof_kw = "(^MOD OF$)"
RE_biggrof_kw = "(^BIGGR OF$)"
RE_smallrof_kw = "(^SMALLR OF$)"
RE_bothof_kw = "(^BOTH OF$)"
RE_eitherof_kw = "(^EITHER OF$)"
RE_wonof_kw = "(^WON OF$)"
RE_not_kw = "(^NOT$)"
RE_anyof_kw = "(^ANY OF$)"
RE_allof_kw = "(^ALL OF$)"
RE_bothsaem_kw = "(^BOTH SAEM$)"
RE_diffrint_kw = "(^DIFFRINT$)"
RE_smoosh_kw = "(^SMOOSH$)"
RE_maek_kw = "(^MAEK$)"
RE_a_kw = "(^A$)"
RE_isnowa_kw = "(^IS NOW A$)"
RE_visible_kw = "(^VISIBLE$)"
RE_gimmeh_kw = "(^GIMMEH$)"
RE_oryl_kw = "(^O RLY\?$)"
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


# Multi-word lexemes
mwe = MWETokenizer([("I", "HAS", "A"), ("SUM", "OF"), ("DIFF", "OF"),
                    ("PRODUKT", "OF"), ("QUOSHUNT", "OF"), ("MOD", "OF"),
                    ("BIGGR", "OF"), ("SMALLR", "OF"), ("BOTH", "OF"),
                    ("EITHER", "OF"), ("WON", "OF"), ("ANY", "OF"),
                    ("BOTH", "SAEM"), ("IS", "NOW", "A"), ("O", "RLY?"),
                    ("YA", "RLY"), ("NO", "WAI"), ("IM", "IN", "YR"),
                    ("IM", "OUTTA", "YR")], separator = " ")



# Function that puts the lines in the file into a list
def remove_Spaces(program):
    scanned_Program = []
    for line in program:                            # Reads per line
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program

noSpaceCode = remove_Spaces(source_code)
print(noSpaceCode)


# Removes whitespaces
for i in noSpaceCode:
    tokens = mwe.tokenize(wordpunct_tokenize(i))
    for token in tokens:
        print(token)
    
    

root.mainloop()