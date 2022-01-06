import semantic_analyzer as sem
from tkinter import *
from tkinter import filedialog, ttk

from tokens import RE_wonof_kw
import lexical_analyzer as lexer

##### SYNTAX ANALYZER #####

lexeme_table = []

# For the lexeme table
def table_contents(source):
    prev = ""
    temp, code_delim = "", ""
    global error, lexeme_table
    error = 0

    for line in source:                     # Iterate through the source code by line
        line_lexemes = []
        if line[0] == "\n":                 # Add line break to signify that next element is a new line
            line_lexemes.append([line[0], "line break"])
            continue
        tokens = lexer.tokenize_line(line)  # Split line into tokens

        for position, lexeme in enumerate(tokens):      # Checking the lexemes one by one

            if lexer.re.match(lexer.my.RE_hai_kw, lexeme):         # If this line contains HAI
                if code_delim == "":                               # If this is the first HAI enocuntered in the program
                    if len(tokens) == 2:                                # Check if line includes a version number
                        line_lexemes.append([tokens[0], "code_delimiter"])
                        code_delim = lexer.my.CODE_DELIMITER
                        prev = lexer.my.VERSION
                        continue                        # Proceed to version number token
                else:                                              # Code Delimiter keyword has been repeated
                    console_print("Syntax Error: Expected statement or expression at:", lexeme)

            if code_delim != lexer.my.CODE_DELIMITER or code_delim == 0:    # If code delimiter has not been encountered yet, all other statements
                if lexeme not in ["BTW", "OBTW", "TLDR"]:                   # except for comments will result to an error
                    error = 1
                    console_print("Syntax Error: Statement or expression not inside the program's main function")
                    break

            para = [lexeme, prev, temp, code_delim, line_lexemes]   # Parameters to be passed to lexical analyzer
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
                        
                        line_lexemes.append([temp, "comment"])
                        temp = ""
                        prev = 0
                        break
                    
                    elif lexer.re.match(lexer.my.RE_obtw_kw, lexeme):       # Checks if there is another statement in the same
                        if position != 0:                                   # line as OBTW
                            error = 1
                            console_print("Syntax Error: OBTW must have its own line")
                            break
                        else: continue
                            
                    elif lexer.re.match(lexer.my.RE_tldr_kw, lexeme):       # Checks if there is another statement in the same
                        if position != len(tokens)-1:                       # line as TLDR
                            error = 1
                            console_print("Syntax Error: TLDR must have its own line")
                            break
                    
                    elif prev == lexer.my.MULTI_LINE_COMMENT:               # Catches multi-line comments
                        if position == 0 and lexeme != "OBTW":              # The whole line is a comment
                                temp = " ".join(tokens)
                                line_lexemes.append([temp, "comment"])
                                temp = ""
                        else:                                               # Comment is placed the same line as the comment keyword
                            for j in range(position, len(tokens)):
                                if temp != "": temp = temp + " " + tokens[j]
                                else: temp = tokens[j]

                            line_lexemes.append([temp, "comment"])
                            temp = ""
                        break
            
            if position == len(tokens)-1:   # End of line
                if prev != 0:
                    error = 1
                    console_print("Syntax Error: Expected token", prev)                

        if error == 1: break
        lexeme_table = lexeme_table + line_lexemes
        global sym_table
        sym_table = sem.get_variables()
        pop_sym()
        print(line_lexemes)
        #sem.program(line_lexemes)
    
    # If end of code has been processed but code delimiter is either not found or not in pair
    if code_delim == lexer.my.CODE_DELIMITER:
        console_print("Syntax Error: Expected token: KTHXBYE")
    elif code_delim == "":
        console_print("Syntax Error: Expected token: HAI")

##### MAIN #####

root = Tk()
root.title = ('Main Window')

# Function that puts each line into a list
def remove_spaces(program):
    scanned_program = []
    for line in program:                            # Reads per line
        if (line.strip() != ''):
            scanned_program.append(line.strip())
            scanned_program.append("\n")
    return scanned_program


# Open lolcode file
def loadfile():
    root.filename = filedialog.askopenfilename(title="Select Folder", filetypes= (("LOLCode files","*.lol"),
                                              ("All files","*.*")))

    file = open(root.filename, 'r')
    program = file.read()

    editor.delete("1.0", "end")
    editor.insert(1.0, program)

def parse_program(program):
    code_lines = program.split('\n')        # Splits the contents of the file by line
    source_code = remove_spaces(code_lines)

    # Syntax Analyzer
    global lexeme_table
    lexeme_table = []
    table_contents(source_code)
    global lexemes
    lexemes = lexeme_table

    # Semantic Analyzer
    if error == 0: 
        lexemes_list = lexemes.copy()       # Create a copy of lexemes
        # sem.program(lexemes_list)
        

# Populate Lexeme Table
def pop_lex():
    lex_table.delete(*lex_table.get_children())
    for item in lexemes:    
        if item[0] == "\n": continue    # Skip line breaks
        lex_table.insert('', 'end', text=str(item[0]), values=(str(item[0]), str(item[1])))

# Populate Symbol Table
def pop_sym():
    # Temporary testing code
    symbol_table.delete(*symbol_table.get_children())
    for key, value in sym_table.items():
        symbol_table.insert('', 'end', text=str(key), values=(str(key), str(value)))

# Run lolcode program
def exec_lolcode():
    console_clear()
    program = editor.get(1.0, 'end')
    parse_program(program)

    # Temporary testing code
    pop_lex()
    pop_sym()

# Print to GUI console 
def console_print(text):
    console.configure(state=NORMAL)
    console.insert('end', text + '\n')
    console.configure(state=DISABLED)
    console.see('end')

# Clear console
def console_clear():
    console.configure(state=NORMAL)
    console.delete(1.0, 'end')
    console.configure(state=DISABLED)


# Give input
def submit():
    # Temporary testing code
    response = console_in.get(1.0, 'end').strip()
    console_in.delete(1.0, 'end')
    console_print(response)

    ### GUI ###

# File Button
file_button = Button(root, text="Load File", command=loadfile)
file_button.grid(row=0, column=0, sticky=E+W, pady=2)

# Code Editor
editor = Text(root, wrap=None)
editor.grid(row=1, column=0)

# Label
interpreter_label = Label(root, text="LOL CODE Interpreter")
interpreter_label.grid(row=0, column=1, columnspan=2)

# Lexeme Label
lex_label = Label(root, text="Lexemes")
lex_label.grid(row=1, column=1)

# Symbol Table Label
symbol_label = Label(root, text="SYMBOL TABLE")
symbol_label.grid(row=1, column=2)

# Lexeme Table
lex_table = ttk.Treeview(root, columns=("Lexeme", "Classification"), show='headings')
lex_table.column("Lexeme", anchor=CENTER)
lex_table.heading("Lexeme", text="Lexeme")
lex_table.column("Classification", anchor=CENTER)
lex_table.heading("Classification", text="Classification")
lex_table.grid(row=1, column=1, sticky=N+S+E+W)

# Symbol Table
symbol_table = ttk.Treeview(root, columns=("Identifier", "Value"), show='headings')
symbol_table.column("Identifier", anchor=CENTER)
symbol_table.heading("Identifier", text="Identifier")
symbol_table.column("Value", anchor=CENTER)
symbol_table.heading("Value", text="Value")
symbol_table.grid(row=1, column=2, sticky=N+S+E+W)


# Execute Button
exec_button = Button(root, text="EXECUTE", command=exec_lolcode)
exec_button.grid(row=14, column=0, columnspan=3, sticky=E+W, pady=2)

# Console Label
console_label = Label(root, text="Console Output")
console_label.grid(row=15, column=0, sticky=W, padx=10)

# Input Button
console_in_label = Button(root, text="Submit Input", command=submit)
console_in_label.grid(row=15, column=2, sticky=E+W, pady=2, padx=10)

# Console
console = Text(root, wrap=None, state=DISABLED)
console.grid(row=16, column=0, columnspan=2, sticky=E+W)

# Console Input
console_in = Text(root, wrap=None)
console_in.grid(row=16, column=2, sticky=E+W, padx=10)

### END GUI ###

root.mainloop()
