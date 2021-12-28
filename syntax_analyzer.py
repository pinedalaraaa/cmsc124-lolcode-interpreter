import lexical_analyzer as lexer

lexeme_list = []

def parse(source):
    temp = ""
    prev = ""
    error = 0

    for line in source:                     # Iterate through the source code by line
        tokens = lexer.tokenize_line(line)  # Split line into tokens
        
        for position, lexeme in enumerate(tokens):      # Checking the lexemes one by one
            para = [lexeme, prev, temp, lexeme_list]    # Parameters to be passed

            if (error == 0):
                para = lexer.check_validity(para)       # Check the validity of current lexeme
                prev = para[1]                          # Overwriting the variables with the returned value in the list
                temp = para[2]

                if prev != 0:
                    if prev == lexer.my.SINGLE_LINE_COMMENT:
                        for j in range(position + 1, len(tokens)):          # catch single-line comments
                            if temp != "": temp = temp + " " + tokens[j]
                            else: temp = tokens[j]
                        
                        lexeme_list.append([temp, "comment"])
                        temp = ""
                        prev = 0
                        break         
                    
                    elif lexer.re.match(lexer.my.RE_obtw_kw, lexeme):       # Checks if there is another statement in the same
                        if position != 0:                                   # line as OBTW
                            error = 1
                            print("Error! OBTW must have its own line")
                            break
                        else: continue
                            
                    elif lexer.re.match(lexer.my.RE_tldr_kw, lexeme):       # Checks if there is another statement in the same
                        if position != len(tokens)-1:                       # line as TLDR
                            error = 1
                            print("Error! TLDR must have its own line")
                            break
                    
                    elif prev == lexer.my.MULTI_LINE_COMMENT:               # Catches multi-line comments
                        if position == 0 and lexeme != "OBTW":              # The whole line is a comment
                                temp = " ".join(tokens)
                                lexeme_list.append([temp, "comment"])
                                temp = ""
                        else:                                               # Comment is placed the same line as the comment keyword
                            for j in range(position, len(tokens)):
                                if temp != "": temp = temp + " " + tokens[j]
                                else: temp = tokens[j]

                            lexeme_list.append([temp, "comment"])
                            temp = ""
                        break     
                            
        
        if error == 1: break


# Returns list of lexemes
def get_lexemes():
    return lexeme_list

def clear():
    global lexeme_list
    lexeme_list = []