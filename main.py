
import syntax_analyzer as parser
from tkinter import Tk
from tkinter import filedialog


root = Tk()
root.title = ('Main Window')
root.filename = filedialog.askopenfilename(title="Select Folder", filetypes= (("LOLCode files","*.lol"),
                                          ("All files","*.*")))

file = open(root.filename, 'r')
program = file.read()
source_code = program.split('\n')   # Splits the contents of the file by line


# Function that puts each line into a list
def remove_spaces(program):
    scanned_program = []
    for line in program:                            # Reads per line
        if (line.strip() != ''):
            scanned_program.append(line.strip())
    return scanned_program


source_code = remove_spaces(source_code)


# Syntax Analyzer
parser.parse(source_code)
lexemes = parser.get_lexemes()


# Printing lexemes
for item in lexemes:
    print(item[0], "-", item[1])

    
root.mainloop()