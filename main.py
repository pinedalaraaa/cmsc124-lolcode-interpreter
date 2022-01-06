import time
import semantic_analyzer as sem
from tkinter import *
from tkinter import filedialog, ttk
import syntax_analyzer as parser

from tokens import RE_wonof_kw

submit_now = False
response = ""

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
    # Ask to choose file
    root.filename = filedialog.askopenfilename(title="Select Folder", filetypes= (("LOLCode files","*.lol"),
                                              ("All files","*.*")))

    # Open file
    file = open(root.filename, 'r')
    program = file.read()

    # Put contents of file in editor
    editor.delete("1.0", "end")
    editor.insert(1.0, program)

def parse_program(program):
    code_lines = program.split('\n')        # Splits the contents of the file by line
    source_code = remove_spaces(code_lines)

    # Syntax Analyzer
    global lexemes
    lexemes = []
    parser.table_contents(source_code)

    # Check for errors
    error, error_message = parser.get_error()
    if error == 1:
        console_print(error_message)
    else:
        # If no errors, get the lexemes
        lexemes = parser.get_lexemes()
        global lex_copy
        lex_copy = lexemes.copy()
        pop_lex()

        # Split by line
        global lexeme_lines
        lexeme_lines = []
        lexeme_line = []
        while len(lexemes) > 0:
            if lexemes[0][0] =='\n':
                lexeme_lines.append(lexeme_line)
                lexemes.pop(0)
                lexeme_line = []
            else:
                lexeme_line.append(lexemes.pop(0))


# Populate Lexeme Table
def pop_lex():
    lex_table.delete(*lex_table.get_children())
    for item in lexemes:    
        if item[0] == "\n": continue    # Skip line breaks
        lex_table.insert('', 'end', text=str(item[0]), values=(str(item[0]), str(item[1])))

# Populate Symbol Table
def pop_sym(sym_table):
    symbol_table.delete(*symbol_table.get_children())
    for key, value in sym_table.items():
        symbol_table.insert('', 'end', text=str(key), values=(str(key), str(value)))

# Run lolcode program
def exec_lolcode():
    console_clear()                     # Clear console
    program = editor.get(1.0, 'end')    # Get program from editor
    parse_program(program)              # Parse program

    global submit_now, response, lexeme_lines, lex_copy

    # Main code execution loop
    line_index = 0
    for line in lexeme_lines:
        sem.reset()
        submit_now = False
        response = ""

        sem.program(lex_copy, line_index)               # Run lolcode
        pop_sym(sem.get_variables())    # Put variable data in symbol table

        # Print to console when lolcode says to
        if sem.output != "":
            console_print(sem.output)

        # Get input from GUI
        if sem.wait_for_input:
            # Wait until response is given
            while not submit_now:
                time.sleep(0.1)
            sem.given_input = response
            sem.wait_for_input = False
        
        line_index += 1

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
    global submit_now, response
    response = console_in.get(1.0, 'end').strip()
    submit_now = True
    console_in.delete(1.0, 'end')

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
