import lexical_analyzer as lexer

lexeme_table = []

# For the lexeme table
def table_contents(source):
    prev = ""
    temp, code_delim = "", ""
    first, error = 0, 0

    for line in source:                     # Iterate through the source code by line
        if line[0] == "\n":                 # Add line break to signify that next element is a new line
            lexeme_table.append([line[0], "line break"])
            continue
        tokens = lexer.tokenize_line(line)  # Split line into tokens

        for position, lexeme in enumerate(tokens):      # Checking the lexemes one by one
            para = [lexeme, prev, temp, code_delim, lexeme_table]    # Parameters to be passed

            if first == 0:                              # For the first line in file
                if len(tokens) == 2:                    # File includes a version number
                    code_delim = lexer.my.CODE_DELIMITER
                    lexeme_table.append([tokens[0], "code_delimiter"])
                    prev = lexer.my.VERSION
                first = 1
            
            if (error == 0):
                para = lexer.check_validity(para)       # Check the validity of current lexeme
                prev = para[1]                          # Overwriting the variables with the returned value in the list
                temp = para[2]
                code_delim = para[3]
                
                if prev != 0:
                    if prev == lexer.my.SINGLE_LINE_COMMENT:
                        for j in range(position + 1, len(tokens)):          # catch single-line comments
                            if temp != "": temp = temp + " " + tokens[j]
                            else: temp = tokens[j]
                        
                        lexeme_table.append([temp, "comment"])
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
                                lexeme_table.append([temp, "comment"])
                                temp = ""
                        else:                                               # Comment is placed the same line as the comment keyword
                            for j in range(position, len(tokens)):
                                if temp != "": temp = temp + " " + tokens[j]
                                else: temp = tokens[j]

                            lexeme_table.append([temp, "comment"])
                            temp = ""
                        break
            
            if position == len(tokens)-1:
                if not ((prev != 0 or prev != "") or code_delim!=1):
                    error = 1
                    print("Error!")

        if error == 1: break


# Returns list of lexemes
def get_lexemes():
    return lexeme_table

def clear():
    global lexeme_table
    lexeme_table = []