from cgitb import text
from concurrent.futures import process
import imp
from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename, asksaveasfilename
import subprocess

compiler = Tk()
compiler.title('VHCode IDE')
file_path = ''

def set_file_path(path):
    global file_path
    file_path = path

def open_file(path):
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r',) as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)

def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Salve seu código')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

menur_bar = Menu(compiler)

file_menu = Menu(menur_bar, tearoff=0)
file_menu.add_command(label='Abrir', command=open_file)
file_menu.add_command(label='Salvar', command=save_as)
file_menu.add_command(label='Salvar como', command=save_as)
file_menu.add_command(label='Sair', command=exit)
menur_bar.add_cascade(label='Arquivo', menu=file_menu)

run_bar = Menu(menur_bar, tearoff=0)
run_bar.add_command(label='Rodar', command=run)
menur_bar.add_cascade(label='Rodar', menu=run_bar)

compiler.config(menu=menur_bar)
editor = Text()
editor.pack()
code_output = Text(height=10)
code_output.pack()
compiler.mainloop()