# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:14:43 2021

@author: Mark, Lara
"""


import re
import tokens as my
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


# Function that puts each line into a list
def remove_Spaces(program):
    scanned_Program = []
    for line in program:                            # Reads per line
        if (line.strip() != ''):
            scanned_Program.append(line.strip())
    return scanned_Program

noSpaceCode = remove_Spaces(source_code)
print(noSpaceCode)


prev = 0
for i in noSpaceCode:
    tokens = my.mwe.tokenize(wordpunct_tokenize(i))     # Tokenizes the line
    # print(tokens)

    for position, token in enumerate(tokens):
        # print(token)

        if prev == my.STRING_DELIMITER:               # catches string literal
            if (token != "\""):
                print(token, end=" ")
                continue
            else:
                print("- string literal")
                print(token, "- delimiter_string")
                prev = 0                              # reset value of prev

        elif re.match(my.RE_btw_kw, token):
            print(token, "- comment keyword")

            for j in range(position + 1, len(tokens)):  # catch single-line comments
                print(tokens[j], end=" ")               # end=" " replaces the default newline for printing with a whitespace
            print("- comment")
            break                                       # proceed to next line

        elif re.match(my.RE_obtw_kw, token):
            prev = my.COMMENT
            print(token, "- multi-line comment keyword")
        
        elif re.match(my.RE_tldr_kw, token):
            prev = 0                        # reset value of prev
            print(token, "- multi-line comment keyword")

        elif prev == my.COMMENT:            # catching multi-line comments
            if position == 0:               # whole line is a comment
                str1 = " ".join(tokens)
                print(str1, "- comment")    
            else:                           # comment is places the same line as the comment keyword
                for j in range(position, len(tokens)):
                    print(tokens[j], end=" ")               # end=" " replaces the default newline for printing with a whitespace
                print("- comment")
            break                                           # proceed to next line

        elif re.match(my.RE_hai_kw, token) or re.match(my.RE_kthxbye_kw, token):
            print(token, "- code delimiter")
        
        elif re.match(my.RE_data_type, token):
            print(token, "- data type")

        elif re.match(my.RE_ihasa_kw, token):
            print(token, "- variable declaration")
        
        elif re.match(my.RE_itz_kw, token):
            print(token, "- variable initialization")

        elif re.match(my.RE_r_kw, token):
            print(token, "- assignment operator")

        elif re.match(my.RE_an_kw, token):
            print(token, "- separator")

        elif token in [my.RE_sumof_kw, my.RE_diffof_kw, my.RE_produktof_kw,
                        my.RE_quoshuntof_kw, my.RE_modof_kw, my.RE_biggrof_kw,
                        my.RE_smallrof_kw]:
            print(token, "- arithmetic operator")

        elif token in [my.RE_bothof_kw, my.RE_eitherof_kw, my.RE_wonof_kw,
                        my.RE_not_kw, my.RE_anyof_kw, my.RE_allof_kw]:
            print(token, "- boolean operator")

        elif re.match(my.RE_bothsaem_kw, token) or re.match(my.RE_diffrint_kw, token):
            print(token, "- comparison operator")

        elif re.match(my.RE_smoosh_kw, token):
            print(token, "- concatenation")
        
        elif re.match(my.RE_maek_kw, token) or re.match(my.RE_isnowa_kw, token):
            print(token, "- typecasting")
        
        elif re.match(my.RE_a_kw, token):
            print(token, "- A")                 # di ko pa alam ano tawag dito
        
        elif re.match(my.RE_visible_kw, token):
            print(token, "- output keyword")
        
        elif re.match(my.RE_gimmeh_kw, token):
            print(token, "- input keyword")

        elif re.match(my.RE_orly_kw, token):
            print(token, "- if-then identifier")
        
        elif re.match(my.RE_yarly_kw, token):
            print(token, "- if keyword")
        
        elif re.match(my.RE_nowai_kw, token):
            print(token, "- else keyword")
        
        elif re.match(my.RE_oic_kw, token):
            print(token, "- if-then identifier")
        
        elif re.match(my.RE_wtf_kw, token):
            print(token, "- switch-case identifier")
        
        elif re.match(my.RE_omg_kw, token):
            print(token, "- case keyword")
        
        elif re.match(my.RE_omgwtf_kw, token):
            print(token, "- default case keyword")

        elif re.match(my.RE_iminyr_kw, token) or re.match(my.RE_imouttayr_kw, token):
            print(token, "- loop keyword")

        elif re.match(my.RE_yr_kw, token):
            print(token, "- variable identifier")

        elif re.match(my.RE_uppin_kw, token) or re.match(my.RE_nerfin_kw, token):
            print(token, "- loop operation")

        elif re.match(my.RE_til_kw, token) or re.match(my.RE_wile_kw, token):
            print(token, "- terminating condition keyword")

        elif re.match(my.RE_literal_numbr, token):
            print(token, "- numbr literal")
        
        elif re.match(my.RE_literal_numbar, token):
            print(token, "- numbar literal")

        elif re.match(my.RE_literal_troof, token):
            print(token, "- troof literal")

        elif re.match(my.RE_identifiers, token):
            print(token, "- identifier")
        
        else:   # delimiters
            if token in my.RE_delimiters:       # delimiter_string
                prev = my.STRING_DELIMITER
                print(token, "- delimiter_string")
                

root.mainloop()