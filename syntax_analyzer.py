import lexical_analyzer as lexer

lexeme_table = []
error_message = ""

# For the lexeme table
def table_contents(source):
    prev = ""
    temp, code_delim = "", ""
    global error, error_message
    error = 0

    for line in source:                     # Iterate through the source code by line
        if line[0] == "\n":                 # Add line break to signify that next element is a new line
            lexeme_table.append([line[0], "line break"])
            continue
        tokens = lexer.tokenize_line(line)  # Split line into tokens

        for position, lexeme in enumerate(tokens):      # Checking the lexemes one by one

            if lexer.re.match(lexer.my.RE_hai_kw, lexeme):         # If this line contains HAI
                if code_delim == "":                               # If this is the first HAI enocuntered in the program
                    if len(tokens) == 2:                                # Check if line includes a version number
                        lexeme_table.append([tokens[0], "code_delimiter"])
                        code_delim = lexer.my.CODE_DELIMITER
                        prev = lexer.my.VERSION
                        continue                        # Proceed to version number token
                else:                                              # Code Delimiter keyword has been repeated
                    error_message = str("Syntax Error: Expected statement or expression at:" + str(lexeme))

            if code_delim != lexer.my.CODE_DELIMITER or code_delim == 0:    # If code delimiter has not been encountered yet, all other statements
                if lexeme not in ["BTW", "OBTW", "TLDR"]:                   # except for comments will result to an error
                    error = 1
                    error_message = "Syntax Error: Statement or expression not inside the program's main function"
                    break

            para = [lexeme, prev, temp, code_delim, lexeme_table]   # Parameters to be passed to lexical analyzer
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
                            error_message = "Syntax Error: OBTW must have its own line"
                            break
                        else: continue
                            
                    elif lexer.re.match(lexer.my.RE_tldr_kw, lexeme):       # Checks if there is another statement in the same
                        if position != len(tokens)-1:                       # line as TLDR
                            error = 1
                            error_message = "Syntax Error: TLDR must have its own line"
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
            
            if position == len(tokens)-1:   # End of line
                if prev != 0:
                    error = 1
                    error_message = str("Syntax Error: Expected token" + str(prev))

        if error == 1: break
    
    # If end of code has been processed but code delimiter is either not found or not in pair
    if code_delim == lexer.my.CODE_DELIMITER:
        error_message = "Syntax Error: Expected token: KTHXBYE"
    elif code_delim == "":
        error_message = "Syntax Error: Expected token: HAI"


# Returns list of lexemes
def get_lexemes():
    return lexeme_table

def get_error():
    return error, error_message