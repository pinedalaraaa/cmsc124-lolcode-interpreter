import re
import tokens as my
# import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize


# Tokenizes the line
def tokenize_line(line):
    token_list = my.mwe.tokenize(word_tokenize(line))
    return token_list


# Checks if given lexeme is valid
def check_validity(para):
    token = para[0]
    prev = para[1]
    temp = para[2]
    code_delim = para[3]
    lexemes = para[4]

    if prev == my.STRING_DELIMITER:               # catches yarn literal
        if (token not in my.RE_delimiters):       # if the end of string has not been seen yet
            if temp == "":
                temp = temp + token               # concatenate strings
            else:
                temp = temp + " " + token

        else:
            lexemes.append([temp, "yarn_literal"])    # append to lexemes list
            if token == "``" or token == "''":
                lexemes.append(["\"", "string_delimiter"])
            else:
                lexemes.append([token, "string_delimiter"])
            temp = ""                                   # reset temp
            prev = 0                                    # reset value of prev

    elif re.match(my.RE_btw_kw, token):
        prev = my.SINGLE_LINE_COMMENT
        lexemes.append([token, "comment_keyword"])

    elif re.match(my.RE_obtw_kw, token):
        prev = my.MULTI_LINE_COMMENT
        lexemes.append([token, "multi-line comment keyword"])
        # set pairing to tldr
    
    elif re.match(my.RE_tldr_kw, token):
        prev = 0                                    # reset value of prev
        lexemes.append([token, "multi-line comment keyword"])
        # set pairing to obtw

    elif prev == my.MULTI_LINE_COMMENT: return para

    elif prev == my.VERSION:
        prev = 0
        lexemes.append([token, "version_number"])

    elif re.match(my.RE_hai_kw, token):
        code_delim = my.CODE_DELIMITER
        lexemes.append([token, "code_delimiter"])

    elif re.match(my.RE_kthxbye_kw, token):
        code_delim = 0
        lexemes.append([token, "code_delimiter"])
    
    elif re.match(my.RE_data_type, token):
        lexemes.append([token, "data_type"])

    elif re.match(my.RE_ihasa_kw, token):
        lexemes.append([token, "variable_declaration"])
    
    elif re.match(my.RE_itz_kw, token):
        lexemes.append([token, "variable_initialization"])

    elif re.match(my.RE_r_kw, token):
        lexemes.append([token, "assignment operator"])

    elif re.match(my.RE_an_kw, token):
        lexemes.append([token, "separator"])

    elif token in [my.RE_sumof_kw, my.RE_diffof_kw, my.RE_produktof_kw,
                    my.RE_quoshuntof_kw, my.RE_modof_kw, my.RE_biggrof_kw,
                    my.RE_smallrof_kw]:
        lexemes.append([token, "arithmetic_operator"])

    elif token in [my.RE_bothof_kw, my.RE_eitherof_kw, my.RE_wonof_kw,
                    my.RE_not_kw, my.RE_anyof_kw, my.RE_allof_kw]:
        lexemes.append([token, "boolean_operator"])

    elif re.match(my.RE_bothsaem_kw, token) or re.match(my.RE_diffrint_kw, token):
        lexemes.append([token, "comparison_operator"])

    elif re.match(my.RE_smoosh_kw, token):
        lexemes.append([token, "concatenation"])
    
    elif re.match(my.RE_maek_kw, token) or re.match(my.RE_isnowa_kw, token):
        lexemes.append([token, "typecasting"])
    
    elif re.match(my.RE_a_kw, token):
        lexemes.append([token, "typecasting"])

    elif re.match(my.RE_visible_kw, token):
        lexemes.append([token, "output_keyword"])
    
    elif re.match(my.RE_gimmeh_kw, token):
        lexemes.append([token, "input_keyword"])

    elif re.match(my.RE_orly_kw, token):
        lexemes.append([token, "if_then_delimiter"])
        # set to pair with oic
    
    elif re.match(my.RE_yarly_kw, token):
        lexemes.append([token, "if_keyword"])
    
    elif re.match(my.RE_nowai_kw, token):
        lexemes.append([token, "else_keyword"])
    
    elif re.match(my.RE_oic_kw, token):
        lexemes.append([token, "if_then_delimiter"])
        # set to pair with o rly?
    
    elif re.match(my.RE_wtf_kw, token):
        lexemes.append([token, "switch_case_delimiter"])
    
    elif re.match(my.RE_omg_kw, token):
        lexemes.append([token, "case_keyword"])
    
    elif re.match(my.RE_omgwtf_kw, token):
        lexemes.append([token, "default_case_keyword"])

    elif re.match(my.RE_iminyr_kw, token) or re.match(my.RE_imouttayr_kw, token):
        lexemes.append([token, "loop_delimiter"])
        # set to pair with each other

    elif re.match(my.RE_yr_kw, token):
        lexemes.append([token, "variable_identifier"])

    elif re.match(my.RE_uppin_kw, token) or re.match(my.RE_nerfin_kw, token):
        lexemes.append([token, "loop_operation"])

    elif re.match(my.RE_til_kw, token) or re.match(my.RE_wile_kw, token):
        lexemes.append([token, "terminating_condition_keyword"])

    elif re.match(my.RE_literal_numbr, token):
        lexemes.append([token, "numbr_literal"])
    
    elif re.match(my.RE_literal_numbar, token):
        lexemes.append([token, "numbar_literal"])

    elif re.match(my.RE_literal_troof, token):
        lexemes.append([token, "troof_literal"])

    elif re.match(my.RE_identifiers, token):
        lexemes.append([token, "identifier"])
        
    elif re.match(my.RE_howizi_kw, token) or re.match(my.RE_ifusayso_kw, token):
        lexemes.append([token, "function_delimiter"])
        
    elif re.match(my.RE_gtfo_kw, token) or re.match(my.RE_foundyr_kw, token):
        lexemes.append([token, "return_keyword"])
        
    elif re.match(my.RE_iiz_kw, token) or re.match(my.RE_mkay_kw, token):
        lexemes.append([token, "function_call_delimiter"])
    
    else:   # delimiters
        if token in my.RE_delimiters:       # string delimiter
            prev = my.STRING_DELIMITER
            if token == "``" or token == "''":
                lexemes.append(["\"", "string_delimiter"])
            else:
                lexemes.append([token, "string_delimiter"])

    return [token, prev, temp, code_delim, lexemes]