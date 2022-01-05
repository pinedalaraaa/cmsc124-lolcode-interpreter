import sys

variables = {"IT":None}
data_types = {"NUMBR":int, "NUMBAR":float, "YARN": str, "TROOF":bool, "NOOB":None}
values = {"WIN":True, "FAIL":False}

def get_variables():
    return variables

# Terminal Symbol
def literal(lexemes_list):
    try:
        print("literal")
        types = ["numbr_literal","numbar_literal", "troof_literal", "yarn_literal"]
        if lexemes_list[1][0] == "ITZ":             # Variable has been initialized
            if lexemes_list[2][0] in variables:     # If variable value is the value of another variable
                variables[lexemes_list[0][0]] = variables[lexemes_list[2][0]]
            else:                                   
                if lexemes_list[2][1] in types:     # The value is a literal

                    variables[lexemes_list[0][0]] = lexemes_list[2][0]
                else:                               # The value is an expression
                    variables[lexemes_list[0][0]] = "expression"    # Di pa ayos to
            
            lexemes_list.remove(lexemes_list[2])
            lexemes_list.remove(lexemes_list[1])
        else:
            variables[lexemes_list[0][0]] = None

        print(variables)
        lexemes_list.remove(lexemes_list[0])

    except:
        print("Error! Invalid Variable Declaration")

#===============================================================================================================================================================
# STATEMENTS

def loop():
    print("loop")
def if_block():
    print("if")
def switch():
    print("switch")

def declaration(lexemes_list):
    print("declaration")
    
    lexemes_list.remove(lexemes_list[0])    # Remove variable declaration keyword
    try:
        if lexemes_list[0][0] in variables:     # Variable has already been declared
            raise Exception
        else:                                   # Add to dictionary of variables
            literal(lexemes_list)

    except Exception:
        print("Error! Invalid Variable Declaration")
    
def comment(lexemes_list):
    if lexemes_list[0][0] == "BTW":         # Single-line comment
        lexemes_list.remove(lexemes_list[1])    # Remvoe the comment
        lexemes_list.remove(lexemes_list[0])    # Remove comment keyword
    else:                                   # Multi-line comment
        lexemes_list.remove(lexemes_list[0])    # Remove starting comment keyword
        while lexemes_list[0][1] != "multi-line comment keyword":   # Remove all comments
            lexemes_list.remove(lexemes_list[0])
        lexemes_list.remove(lexemes_list[0])    # Remove end of comment keyword

def input():
    print("input")

def print_code(lexemes_list):
    print("print")
    global variables
    lexemes_list.remove(lexemes_list[0])
    try:
        if lexemes_list[0][1] == "string_delimiter":    # Lexeme to be printed is a yarn literal
            if lexemes_list[3] == "\n":                 # End of statement
                print(lexemes_list[1][0])
                variables["IT"] = lexemes_list[1][0]        # Store to implicit variable IT
                lexemes_list.remove(lexemes_list[2])        # Remove end delimiter
                lexemes_list.remove(lexemes_list[1])        # Remove yarn literal
            else:                                       # There are more to be printed aside from the yarn literal
                print("typecast to yarns then concatenate")
        else:
            if lexemes_list [1][0] == "\n":
                print(variables[lexemes_list[0][0]])        # Lexeme to be printed is a variable
            else:                                       # There are more to be printed aside from the yarn literal
                print("typecast to yarns then concatenate")
        lexemes_list.remove(lexemes_list[0])            # Remove the start delimiter or the variable
    except:
        print("Error! Invalid Statement")

def assignment(lexemes_list):
    print("assignment")
    lexemes_list.remove(lexemes_list[1])            # Remove assignment statement keyword 
    var_name = lexemes_list.remove(lexemes_list[0]) # Variable name

       

#===============================================================================================================================================================
# EXPRESSIONS

def add():
    print("add")
def sub():
    print("sub")
def mul():
    print("mul")
def div():
    print("div")
def mod():
    print("mod")
def max_expr():
    print("max")
def min_expr():
    print("min")
def equal():
    print("equal")
def not_equal():
    print("not equal")
def not_expr():
    print("not")
def greater():
    print("greater")
def less():
    print("less")
def both():
    print("both")
def either():
    print("either")
def xor():
    print("xor")
def cast():
    print("typecast")
def concat():
    print("concat")
def infinite_and():
    print("infinite_and")
def infinite_or():
    print("infinite_or")


def expression(lexemes_list):
    # eto yung mga pwedeng nested operations
    arith = ["SUM OF","DIFF OF","PRODUKT OF","QUOSHUNT OF","MOD OF","BIGGR OF","SMALLR OF"]
    print("expression")
    
    # while lexemes_list[0][0]!="\n":  # ipagpatuloy yung loop for nested operations hanggang sa makakita ng newline
    #     for token in lexemes_list[0]:
    #         if token == "SUM OF": add()
    #         elif token == "DIFF OF": sub()
    #         elif token == "PRODUKT OF": mul()
    #         elif token == "QUOSHUNT OF": div()
    #         elif token == "MOD OF": mod()
    #         elif token == "BIGGR OF": max_expr()
    #         elif token == "SMALLR OF": min_expr()
    #         elif token == "BOTH SAEM":
    #             equal()
    #             greater()
    #             less()
    #         elif token == "DIFFRINT":
    #             not_equal() 
    #             greater()
    #             less()
    #         elif token == "NOT": not_expr()
    #         elif token == "BOTH OF": both()
    #         elif token == "EITHER OF": either()
    #         elif token == "WON OF": xor()
    #         elif token == "MAEK" or "MAEK" in lexemes_list[0]: cast()
    #         elif token == "SMOOSH": concat()
    #         elif token == "ALL OF": infinite_and()
    #         elif token == "ANY OF": infinite_or()
    #         #pano yung production rule ng to_infinity

    #         else:   # maybe a literal?
    #             literal()


def program(lexemes_list):
    code_start = 0
    while code_start != 1:
        if lexemes_list[0][0] == "HAI":
            code_start = 1
            if lexemes_list[1][1] == "version_number":
                lexemes_list.remove(lexemes_list[1])
        lexemes_list.remove(lexemes_list[0])
    
    i=0
    while len(lexemes_list) > 0:                    # Iterates through the list of lexemes
        if i==10:
            print(lexemes_list)
            break

        if lexemes_list[0][0] != "KTHXBYE":         # Check which statement is given
            if lexemes_list[0][0] == "\n": lexemes_list.remove(lexemes_list[0])
            if lexemes_list[0][0] == "IM IN YR": loop()
            elif lexemes_list[0][0] == "O RLY?": if_block()
            elif lexemes_list[0][0] == "WTF?": switch()
            elif lexemes_list[0][0] == "I HAS A": declaration(lexemes_list)
            elif lexemes_list[0][0] in ("BTW", "OBTW"): comment(lexemes_list)
            elif lexemes_list[0][0] == "GIMMEH": input(lexemes_list)
            elif lexemes_list[0][0] == "VISIBLE": print_code(lexemes_list)
            elif lexemes_list[0][0] in variables.keys() and lexemes_list[1][0] == "R": assignment(lexemes_list)
            else:                                   # It's probably an expression
                expression(lexemes_list)
        else:
            break

        i += 1