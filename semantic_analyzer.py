import sys
import re
import tokens as my

variables = {"IT":None}
data_types = {"NUMBR":int, "NUMBAR":float, "YARN": str, "TROOF":bool, "NOOB":None}
values = {"WIN":True, "FAIL":False}
types = ["numbr_literal","numbar_literal", "troof_literal", "yarn_literal"]
expressions = ["SUM OF","DIFF OF","PRODUKT OF","QUOSHUNT OF","MOD OF","BIGGR OF","SMALLR OF"]

def get_variables():
    return variables

#terminal symbol
def literal(lexemes_list):
    try:
        print("literal")

        if lexemes_list[1][0] == "ITZ":             # Variable has been initialized
            if lexemes_list[2][0] in variables:     # If variable value is the value of another variable
                variables[lexemes_list[0][0]] = variables[lexemes_list[2][0]]
            else:                                   
                if lexemes_list[2][1] in types:     # The value is a literal                     
                    variables[lexemes_list[0][0]] = lexemes_list[2][0]
                elif lexemes_list [2][0] == "\"":   #for strings
                    variables[lexemes_list[0][0]] = lexemes_list[3][0]
                    lexemes_list.remove(lexemes_list[4])
                    lexemes_list.remove(lexemes_list[2])
                else:                               # The value is an expression
                    for exprn in expressions:                       
                        if lexemes_list[2][0] == exprn:
                            temp = lexemes_list[0][0]
                            lexemes_list.remove(lexemes_list[1])
                            lexemes_list.remove(lexemes_list[0])
                            print("MY EXPR: "+str(lexemes_list[0]))
                            variables[temp] = expression(lexemes_list)
            
            lexemes_list.remove(lexemes_list[2])
            lexemes_list.remove(lexemes_list[1])
        else:
            variables[lexemes_list[0][0]] = None

        print(variables)

    except:
        print("Error! Invalid Variable Declaration")

#===============================================================================================================================================================
# STATEMENTS
def loop(lexemes_list):
    print("loop")
    if lexemes_list[1][1] == "identifier":
        if lexemes_list[2][0] == "UPPIN" and lexemes_list[3][0] == "YR":
            print()
        elif lexemes_list[2][0] == "NERFIN" and lexemes_list[3][0] == "YR":
            print()
        else:
            print("Error! Loop operation not found")
    else:
        print("Error! Loop must have a proper label")
        
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
        lexemes_list.remove(lexemes_list[1])
        lexemes_list.remove(lexemes_list[0])
    else:                                   # Multi-line comment
        lexemes_list.remove(lexemes_list[0])
        while lexemes_list[0][1] != "multi-line comment keyword":
            lexemes_list.remove(lexemes_list[0])
        lexemes_list.remove(lexemes_list[0])

def userinput(lexemes_list):
    lexemes_list.remove(lexemes_list[0])
    print("Enter: ")
    variables[lexemes_list[0][0]] = input()
    print("input")

def print_code(lexemes_list):
    print("print")
    lexemes_list.remove(lexemes_list[0])
    try:
        if lexemes_list[0][1] == "string_delimiter":    # Lexeme to be printed is a yarn literal
            print(lexemes_list[1][0])
            lexemes_list.remove(lexemes_list[2])
            lexemes_list.remove(lexemes_list[1])
        else:
            print(variables[lexemes_list[0][0]])    # Lexeme to be printed is a variable
        lexemes_list.remove(lexemes_list[0])
    except:
        print("Error! Invalid Statement")

def function(lexemes_list):
    print("function")

def assignment(lexemes_list):
    print("assignment")
    if lexemes_list[2][1] in types: #value that will be assigned is a literal 
        variables[lexemes_list[0][0]] = lexemes_list[2][0]
        print(variables) 

    elif lexemes_list[2][0] in variables:   #value will come from a variable
        print("in variables")
        print(variables[lexemes_list[2][0]])
        
        for key, value in variables.items():    #check if variable exists  
            if key == lexemes_list[0][0]:
                variables[key] = variables[lexemes_list[2][0]]
                
        variables[lexemes_list[0][0]] == variables[lexemes_list[2][0]]
        print(variables) 

    else:
        temp = lexemes_list
        temp.remove(temp[0])
        temp.remove(temp[1])
        expression(temp)
        variables[lexemes_list[0][0]] = variables["IT"]
        
    lexemes_list.remove(lexemes_list[2])
    lexemes_list.remove(lexemes_list[1]) 
 
#===============================================================================================================================================================
# EXPRESSIONS    
def add(op1, op2):
    print("add")
    print("OP1: "+str(op1)+" : "+str(type(op1)))
    print("OP2: "+str(op2)+" : "+str(type(op2)))
    itsum = op1 + op2
    return itsum 
    
def sub(op1, op2):
    print("sub")
    print("OP1: "+str(op1)+" : "+str(type(op1)))
    print("OP2: "+str(op2)+" : "+str(type(op2)))
    itdiff = op1 + op2
    return itdiff 

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
    if lexemes_list[0][0] == "SUM OF":
        op1 = 0
        op2 = 0
        if lexemes_list[1][1] in types: 
            if lexemes_list[1][1] == "numbr_literal":
                op1 = int(lexemes_list[1][0])
                if lexemes_list[3][1] in types:
                    
                    if lexemes_list[3][1] == "numbr_literal":   #int + int
                        op2 = int(lexemes_list[3][0])                       
                    
                    elif lexemes_list[3][1] == "numbar_literal":    #int + float
                        op2 = float(lexemes_list[3][0])
                        
                    elif lexemes_list[3][0] == "WIN":   #int + true
                        op2 = 1
                    elif lexemes_list[3][0] == "FAIL":    #int+false
                        op2 = 0    
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    
                elif lexemes_list[3][1] == "string_delimiter":  #int + string
                    if lexemes_list[4][1] == "yarn_literal":
                        if re.match(my.RE_literal_numbr, lexemes_list[4][0]):   #string is a int
                            op2 = int(lexemes_list[4][0])
                        elif re.match(my.RE_literal_numbar, lexemes_list[4][0]):    #string is a float
                            op2 = float(lexemes_list[4][0])
                        else:
                            print("Error! Invalid YARN format for number typecasting")
                            exit()
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                
                elif lexemes_list[3][0] in variables:   #int + variable
                    if re.match(my.RE_literal_numbr, variables[lexemes_list[3][0]]):
                        op2 = int(variables[lexemes_list[3][0]])
                    elif re.match(my.RE_literal_numbar, variables[lexemes_list[3][0]]):
                        op2 = float(variables[lexemes_list[3][0]])
                    elif variables[lexemes_list[3][0]] == "WIN":
                        op2 = 1
                    elif variables[lexemes_list[3][0]] == "FAIL":
                        op2 = 0
                    else:
                        print("Error! Invalid variable value for operand in addition")
                        exit()                        
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                elif lexemes_list[3][0] in expressions:
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    lexemes_list.remove(lexemes_list[0])
                    op2 = expression(lexemes_list)
                    
                    
            elif lexemes_list[1][1] == "numbar_literal":     #operand 1 is a float
                op1 = float(lexemes_list[1][0])
                if lexemes_list[3][1] in types:
                    
                    if lexemes_list[3][1] == "numbr_literal":   #float + int
                        op2 = int(lexemes_list[3][0])                       
                    
                    elif lexemes_list[3][1] == "numbar_literal":    #float + float
                        op2 = float(lexemes_list[3][0])
                        
                    elif lexemes_list[3][0] == "WIN":   #float + true
                        op2 = 1
                    elif lexemes_list[3][0] == "FAIL":    #float+false
                        op2 = 0    
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    
                elif lexemes_list[3][1] == "string_delimiter":  #float + string
                    if lexemes_list[4][1] == "yarn_literal":
                        if re.match(my.RE_literal_numbr, lexemes_list[4][0]):   #string is a int
                            op2 = int(lexemes_list[4][0])
                        elif re.match(my.RE_literal_numbar, lexemes_list[4][0]):    #string is a float
                            op2 = float(lexemes_list[4][0])
                        else:
                            print("Error! Invalid YARN format for number typecasting")
                            exit()
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                
                elif lexemes_list[3][0] in variables:   #float + variable
                    if re.match(my.RE_literal_numbr, variables[lexemes_list[3][0]]):
                        op2 = int(variables[lexemes_list[3][0]])
                    elif re.match(my.RE_literal_numbar, variables[lexemes_list[3][0]]):
                        op2 = float(variables[lexemes_list[3][0]])
                    elif variables[lexemes_list[3][0]] == "WIN":
                        op2 = 1
                    elif variables[lexemes_list[3][0]] == "FAIL":
                        op2 = 0
                    else:
                        print("Error! Invalid variable value for operand in addition")
                        exit()                        
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    
                elif lexemes_list[3][0] in expressions: #float + expression
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    lexemes_list.remove(lexemes_list[0])
                    op2 = expression(lexemes_list)
                    
            elif lexemes_list[1][0] == "WIN":
                op1 = 1
                if lexemes_list[3][1] in types:
                    
                    if lexemes_list[3][1] == "numbr_literal":   #1 + int
                        op2 = int(lexemes_list[3][0])                       
                    
                    elif lexemes_list[3][1] == "numbar_literal":    #1 + float
                        op2 = float(lexemes_list[3][0])
                        
                    elif lexemes_list[3][0] == "WIN":   #1 + true
                        op2 = 1
                    elif lexemes_list[3][0] == "FAIL":    #1+false
                        op2 = 0    
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    
                elif lexemes_list[3][1] == "string_delimiter":  #1 + string
                    if lexemes_list[4][1] == "yarn_literal":
                        if re.match(my.RE_literal_numbr, lexemes_list[4][0]):   #string is a int
                            op2 = int(lexemes_list[4][0])
                        elif re.match(my.RE_literal_numbar, lexemes_list[4][0]):    #string is a float
                            op2 = float(lexemes_list[4][0])
                        else:
                            print("Error! Invalid YARN format for number typecasting")
                            exit()
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                
                elif lexemes_list[3][0] in variables:   #1 + variable
                    if re.match(my.RE_literal_numbr, variables[lexemes_list[3][0]]):
                        op2 = int(variables[lexemes_list[3][0]])
                    elif re.match(my.RE_literal_numbar, variables[lexemes_list[3][0]]):
                        op2 = float(variables[lexemes_list[3][0]])
                    elif variables[lexemes_list[3][0]] == "WIN":
                        op2 = 1
                    elif variables[lexemes_list[3][0]] == "FAIL":
                        op2 = 0
                    else:
                        print("Error! Invalid variable value for operand in addition")
                        exit()                        
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    
                elif lexemes_list[3][0] in expressions: #1 + expression
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    lexemes_list.remove(lexemes_list[0])
                    op2 = expression(lexemes_list)
                    
            elif lexemes_list[1][0] == "FAIL":
                op1 = 0
                if lexemes_list[3][1] in types:
                    
                    if lexemes_list[3][1] == "numbr_literal":   #0 + int
                        op2 = int(lexemes_list[3][0])                       
                    
                    elif lexemes_list[3][1] == "numbar_literal":    #0 + float
                        op2 = float(lexemes_list[3][0])
                        
                    elif lexemes_list[3][0] == "WIN":   #0 + true
                        op2 = 1
                    elif lexemes_list[3][0] == "FAIL":    #0+false
                        op2 = 0    
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    
                elif lexemes_list[3][1] == "string_delimiter":  #0 + string
                    if lexemes_list[4][1] == "yarn_literal":
                        if re.match(my.RE_literal_numbr, lexemes_list[4][0]):   #string is a int
                            op2 = int(lexemes_list[4][0])
                        elif re.match(my.RE_literal_numbar, lexemes_list[4][0]):    #string is a float
                            op2 = float(lexemes_list[4][0])
                        else:
                            print("Error! Invalid YARN format for number typecasting")
                            exit()
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                
                elif lexemes_list[3][0] in variables:   #0 + variable
                    if re.match(my.RE_literal_numbr, variables[lexemes_list[3][0]]):
                        op2 = int(variables[lexemes_list[3][0]])
                    elif re.match(my.RE_literal_numbar, variables[lexemes_list[3][0]]):
                        op2 = float(variables[lexemes_list[3][0]])
                    elif variables[lexemes_list[3][0]] == "WIN":
                        op2 = 1
                    elif variables[lexemes_list[3][0]] == "FAIL":
                        op2 = 0
                    else:
                        print("Error! Invalid variable value for operand in addition")
                        exit()                        
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    
                elif lexemes_list[3][0] in expressions:
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                    lexemes_list.remove(lexemes_list[0])
                    op2 = expression(lexemes_list)
            
        elif lexemes_list[1][1] == "string_delimiter":          #operand 1  is a string
            if lexemes_list[2][1] == "yarn_literal":
                if re.match(my.RE_literal_numbr, lexemes_list[2][0]):
                    op1 = int(lexemes_list[2][0]) #typecasting string to int
                    if lexemes_list[5][1] in types:                    
                        if lexemes_list[5][1] == "numbr_literal":   #string(int) + int
                            op2 = int(lexemes_list[5][0])                       
                    
                        elif lexemes_list[5][1] == "numbar_literal":    #string(int) + float
                            op2 = float(lexemes_list[5][0])
                        
                        elif lexemes_list[5][0] == "WIN":   #string(int) + true
                            op2 = 1
                        elif lexemes_list[5][0] == "FAIL":    #string(int) + false
                            op2 = 0    
                        lexemes_list.remove(lexemes_list[5])    
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                    
                    elif lexemes_list[5][1] == "string_delimiter":  #string(int) + string
                        if lexemes_list[6][1] == "yarn_literal":
                            if re.match(my.RE_literal_numbr, lexemes_list[6][0]):   #string is a int
                                op2 = int(lexemes_list[6][0])
                            elif re.match(my.RE_literal_numbar, lexemes_list[6][0]):    #string is a float
                                op2 = float(lexemes_list[6][0])
                            else:
                                print("Error! Invalid YARN format for number typecasting")
                                exit()
                        lexemes_list.remove(lexemes_list[7])
                        lexemes_list.remove(lexemes_list[6])
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                
                    elif lexemes_list[5][0] in variables:   #string(int) + variable
                        if re.match(my.RE_literal_numbr, variables[lexemes_list[5][0]]):
                            op2 = int(variables[lexemes_list[5][0]])
                        elif re.match(my.RE_literal_numbar, variables[lexemes_list[5][0]]):
                            op2 = float(variables[lexemes_list[5][0]])
                        elif variables[lexemes_list[5][0]] == "WIN":
                            op2 = 1
                        elif variables[lexemes_list[5][0]] == "FAIL":
                            op2 = 0
                        else:
                            print("Error! Invalid variable value for operand in addition")
                            exit()
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                    elif lexemes_list[5][0] in expressions: #string(int) + expression
                        lexemes_list.remove(lexemes_list[4])
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                        lexemes_list.remove(lexemes_list[0])
                        op2 = expression(lexemes_list)

                    
                elif re.match(my.RE_literal_numbar, lexemes_list[2][0]):
                    op1 = float(lexemes_list[2][0])
                    if lexemes_list[5][1] in types:                    
                        if lexemes_list[5][1] == "numbr_literal":   #string(float) + int
                            op2 = int(lexemes_list[5][0])                       
                    
                        elif lexemes_list[5][1] == "numbar_literal":    #string(float) + float
                            op2 = float(lexemes_list[5][0])
                        
                        elif lexemes_list[5][0] == "WIN":   #string(float) + true
                            op2 = 1
                        elif lexemes_list[5][0] == "FAIL":    #string(float) + false
                            op2 = 0    
                        lexemes_list.remove(lexemes_list[5])    
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                    
                    elif lexemes_list[5][1] == "string_delimiter":  #string(float) + string
                        if lexemes_list[6][1] == "yarn_literal":
                            if re.match(my.RE_literal_numbr, lexemes_list[6][0]):   #string is a int
                                op2 = int(lexemes_list[6][0])
                            elif re.match(my.RE_literal_numbar, lexemes_list[6][0]):    #string is a float
                                op2 = float(lexemes_list[6][0])
                            else:
                                print("Error! Invalid YARN format for number typecasting")
                                exit()
                        lexemes_list.remove(lexemes_list[7])
                        lexemes_list.remove(lexemes_list[6])
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])    
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                
                    elif lexemes_list[5][0] in variables:   #string(float) + variable
                        if re.match(my.RE_literal_numbr, variables[lexemes_list[5][0]]):
                            op2 = int(variables[lexemes_list[5][0]])
                        elif re.match(my.RE_literal_numbar, variables[lexemes_list[5][0]]):
                            op2 = float(variables[lexemes_list[5][0]])
                        elif variables[lexemes_list[5][0]] == "WIN":
                            op2 = 1
                        elif variables[lexemes_list[5][0]] == "FAIL":
                            op2 = 0
                        else:
                            print("Error! Invalid variable value for operand in addition")
                            exit()
                        lexemes_list.remove(lexemes_list[5])
                        lexemes_list.remove(lexemes_list[4])
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                    elif lexemes_list[5][0] in expressions: #string(float) + expression
                        lexemes_list.remove(lexemes_list[4])
                        lexemes_list.remove(lexemes_list[3])
                        lexemes_list.remove(lexemes_list[2])
                        lexemes_list.remove(lexemes_list[1])
                        lexemes_list.remove(lexemes_list[0])
                        op2 = expression(lexemes_list)
                else:
                    print("Error! Invalid YARN format for number typecasting")
                    exit()
                
                
        elif lexemes_list[1][0] in variables:       #operand 1 is a variable
            if re.match(my.RE_literal_numbr, variables[lexemes_list[1][0]]):
                op1 = int(variables[lexemes_list[1][0]])
            elif re.match(my.RE_literal_numbar, variables[lexemes_list[1][0]]):
                op1 = float(variables[lexemes_list[1][0]])
            elif variables[lexemes_list[1][0]] == "WIN":
                op1 = 1
            elif variables[lexemes_list[1][0]] == "FAIL":
                op1 = 0
            else:
                print("Error! Invalid variable value for operand in addition")
                exit()
            
            if lexemes_list[3][1] in types:                    
                if lexemes_list[3][1] == "numbr_literal":   #var + int
                    op2 = int(lexemes_list[3][0])                       
                    
                elif lexemes_list[3][1] == "numbar_literal":    #var + float
                    op2 = float(lexemes_list[3][0])
                        
                elif lexemes_list[3][0] == "WIN":   #var + true
                    op2 = 1
                elif lexemes_list[3][0] == "FAIL":    #var+false
                    op2 = 0    
                lexemes_list.remove(lexemes_list[3])
                lexemes_list.remove(lexemes_list[2])
                lexemes_list.remove(lexemes_list[1])
                    
            elif lexemes_list[3][1] == "string_delimiter":  #var + string
                if lexemes_list[4][1] == "yarn_literal":
                    if re.match(my.RE_literal_numbr, lexemes_list[4][0]):   #string is a int
                        op2 = int(lexemes_list[4][0])
                    elif re.match(my.RE_literal_numbar, lexemes_list[4][0]):    #string is a float
                        op2 = float(lexemes_list[4][0])
                    else:
                        print("Error! Invalid YARN format for number typecasting")
                        exit()
                    lexemes_list.remove(lexemes_list[5])
                    lexemes_list.remove(lexemes_list[4])    
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                
            elif lexemes_list[3][0] in variables:   #var + variable
                if re.match(my.RE_literal_numbr, variables[lexemes_list[3][0]]):
                    op2 = int(variables[lexemes_list[3][0]])
                elif re.match(my.RE_literal_numbar, variables[lexemes_list[3][0]]):
                    op2 = float(variables[lexemes_list[3][0]])
                elif variables[lexemes_list[3][0]] == "WIN":
                    op2 = 1
                elif variables[lexemes_list[3][0]] == "FAIL":
                    op2 = 0
                else:
                    print("Error! Invalid variable value for operand in addition")
                    exit()                        
                lexemes_list.remove(lexemes_list[3])
                lexemes_list.remove(lexemes_list[2])
                lexemes_list.remove(lexemes_list[1])
            elif lexemes_list[3][0] in expressions: #var + expression
                lexemes_list.remove(lexemes_list[2])
                lexemes_list.remove(lexemes_list[1])
                lexemes_list.remove(lexemes_list[0])
                op2 = expression(lexemes_list)    

        elif lexemes_list[1][0] in expressions: 
            #remove first sum of
            #lexemes_list[0] = expr
            lexemes_list.remove(lexemes_list[0]) 
            op1 = expression(lexemes_list)
            if lexemes_list[2][1] in types:                    
                if lexemes_list[2][1] == "numbr_literal":   #expr + int
                    op2 = int(lexemes_list[2][0])                       
                    
                elif lexemes_list[0][1] == "numbar_literal":    #expr + float
                    op2 = float(lexemes_list[2][0])
                        
                elif lexemes_list[2][0] == "WIN":   #expr + true
                    op2 = 1
                elif lexemes_list[2][0] == "FAIL":    #expr+false                    op2 = 0    
                    op2 = 0
                lexemes_list.remove(lexemes_list[2])
                lexemes_list.remove(lexemes_list[1])
            elif lexemes_list[2][1] == "string_delimiter":  #expr + string
                if lexemes_list[3][1] == "yarn_literal":
                    if re.match(my.RE_literal_numbr, lexemes_list[3][0]):   #string is a int
                        op2 = int(lexemes_list[3][0])
                    elif re.match(my.RE_literal_numbar, lexemes_list[3][0]):    #string is a float
                        op2 = float(lexemes_list[3][0])
                    else:
                        print("Error! Invalid YARN format for number typecasting")
                    lexemes_list.remove(lexemes_list[4])    
                    lexemes_list.remove(lexemes_list[3])
                    lexemes_list.remove(lexemes_list[2])
                    lexemes_list.remove(lexemes_list[1])
                
            elif lexemes_list[2][0] in variables:   #expr + variable
                if re.match(my.RE_literal_numbr, variables[lexemes_list[2][0]]):
                    op2 = int(variables[lexemes_list[2][0]])
                elif re.match(my.RE_literal_numbar, variables[lexemes_list[2][0]]):
                    op2 = float(variables[lexemes_list[2][0]])
                elif variables[lexemes_list[2][0]] == "WIN":
                    op2 = 1
                elif variables[lexemes_list[2][0]] == "FAIL":
                    op2 = 0
                else:
                    print("Error! Invalid variable value for operand in addition")
                    exit()                        
                lexemes_list.remove(lexemes_list[2])
                lexemes_list.remove(lexemes_list[1])
            elif lexemes_list[2][0] in expressions:
                lexemes_list.remove(lexemes_list[1])
                lexemes_list.remove(lexemes_list[0])
                op2 = expression(lexemes_list)
                print("op2: "+str(op2))
        else:
            print("Error! Invalid operand")
            
        
        variables["IT"] = add(op1, op2)
        print(variables["IT"])
        return variables["IT"]
        

            
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
    

#main semantic_analyzer
def program(lexemes_list):
    code_start = 0
    while code_start != 1:
        if lexemes_list[0][0] == "HAI":
            code_start = 1
            lexemes_list.remove(lexemes_list[0])
            lexemes_list.remove(lexemes_list[0])
            if lexemes_list[1][1] == "version_number":
                lexemes_list.remove(lexemes_list[1])
        lexemes_list.remove(lexemes_list[0])        
    
    while (1):
        if lexemes_list[0][0] != "KTHXBYE":
            if lexemes_list[0][0] == "\n": #line breaks                
                lexemes_list.remove(lexemes_list[0])
            else:    #statements
                if lexemes_list[0][0] == "IM IN YR":
                    loop(lexemes_list)
                elif lexemes_list[0][0] == "O RYL?":
                    if_block(lexemes_list[0][0])
                elif lexemes_list[0][0] == "WTF?":
                    switch(lexemes_list)
                elif lexemes_list[0][0] == "HOW IZ I":
                    function(lexemes_list)
                elif lexemes_list[0][0] == "I HAS A":
                    declaration(lexemes_list)
                elif lexemes_list[0][0] == "BTW" or lexemes_list[0][0] == "OBTW":
                    comment(lexemes_list)
                elif lexemes_list[0][0] == "GIMMEH":
                    userinput(lexemes_list)
                elif lexemes_list[0][0] == "VISIBLE":
                    print_code(lexemes_list)
                elif lexemes_list[0][1] == "identifier" and lexemes_list[1][0] == "R":
                    assignment(lexemes_list)
                else:
                    expression(lexemes_list)
                lexemes_list.remove(lexemes_list[0])            

   
        else:
            print("end of program")
            break
