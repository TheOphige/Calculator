


















import tkinter as tk
from tkinter import ttk, scrolledtext, Menu, Spinbox, filedialog as fd, messagebox as mBox 
from PIL import Image, ImageTk
from math import pi, e, sin, cos, tan, log, log10, exp, sqrt, pow, atan2, hypot, asinh, degrees, radians, asin, acos, atan, acosh, atanh
from cmath import log, log10, pi, e, sin, cos, sqrt, tan, sinh, cosh, tanh
from callbacks import *

# Creating a Window ===========================================================
win = tk.Tk()
win.title('Calculator')
win.iconbitmap('CALCULATOR LOGO.ico')
#win.geometry('+%d+%d'%(350, 350))
#win.state('zoomed')
#win.attributes('-fullscreen', True)


#logo
logo= Image.open('Calculator.jpg')
logo= logo.resize((int(logo.size[0]/1.8), int(logo.size[1]/1.5)))
logo= ImageTk.PhotoImage(logo)
logo_label = tk.Label(image= logo, bg='white')
logo_label.image= logo
logo_label.grid(column=0, row=0, rowspan=2, sticky='NW', padx=20, pady=10)

entry1= tk.Entry(win)
entry1.grid(row=3, column=0, columnspan=4, padx=10, pady=0)
#entry= tk.Text(win, height=5, width=48)
#entry.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

entry2= tk.Entry(win)
entry2.grid(row=4, column=0, columnspan=4, padx=10, pady=0)

last_equal= ''
last_operation= ''


# Creating tabs ===============================================================
tabControl= ttk.Notebook(win)
numbers= ttk.Frame(tabControl)
tabControl.add(numbers, text='123')
functions= ttk.Frame(tabControl)
tabControl.add(functions, text='Fx')
tabControl.grid(row=6, column=0, padx=4, pady=6)

# Creating a Menu Bar ==========================================================
win.bind('<F1>', lambda e: help())
win.bind('<F11>', lambda event: full())
win.bind('<Escape>', lambda event: win.attributes('-fullscreen', False))


menuBar = Menu(numbers)
win.config(menu=menuBar)
        
# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New           Ctrl-N')
fileMenu.add_separator()
fileMenu.add_command(label='Exit          Ctrl-X', command= lambda e: _quit())
menuBar.add_cascade(label='File', menu=fileMenu)
        
# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command= lambda e: _msg())
helpMenu.add_command(label='Instructions  F1', command= lambda e: help())
menuBar.add_cascade(label='Help', menu=helpMenu)

# Add another Menu to the Menu Bar and an item
viewMenu = Menu(menuBar, tearoff=0)
viewMenu.add_command(label= 'Fullscreen  F11', command= lambda e: full())
menuBar.add_cascade(label='View', menu=viewMenu)

###################################################################################
entries= [entry1, entry2]


button_OPENBCKT = tk.Button(numbers, text='(', width=3, bg='grey', padx=40, pady=20, command=lambda e: button_openbckt())
button_OPENBCKT.grid(row=1, column=0)

button_CLOSEBCKT = tk.Button(numbers, text=')', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_closebckt())
button_CLOSEBCKT.grid(row=1, column=1)

button_Modulus = tk.Button(numbers, text='%', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_modulus())
button_Modulus.grid(row=1, column=2)


button_AC = tk.Button(numbers, text='AC', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_clear())
button_AC.grid(row=1, column=3)

button_7 = tk.Button(numbers, text='7', padx=47, pady=20, command=lambda: button_click(7))
button_7.grid(row=2, column=0)

button_8 = tk.Button(numbers, text='8', padx=47, pady=20, command=lambda: button_click(8))
button_8.grid(row=2, column=1)

button_9 = tk.Button(numbers, text='9', padx=47, pady=20, command=lambda: button_click(9))
button_9.grid(row=2, column=2)

button_divide = tk.Button(numbers, text='/', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_divide())
button_divide.grid(row=2, column=3)

button_4 = tk.Button(numbers, text='4', padx=47, pady=20, command=lambda: button_click(4))
button_4.grid(row=3, column=0)

button_5 = tk.Button(numbers, text='5', padx=47, pady=20, command=lambda: button_click(5))
button_5.grid(row=3, column=1)

button_6 = tk.Button(numbers, text='6', padx=47, pady=20, command=lambda: button_click(6))
button_6.grid(row=3, column=2)

button_times = tk.Button(numbers, text='x', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_multiply())
button_times.grid(row=3, column=3)

button_1 = tk.Button(numbers, text='1', padx=47, pady=20, command=lambda: button_click(1))
button_1.grid(row=4, column=0)

button_2 = tk.Button(numbers, text='2', padx=47, pady=20, command=lambda: button_click(2))
button_2.grid(row=4, column=1)

button_3 = tk.Button(numbers, text='3', padx=47, pady=20, command=lambda: button_click(3))
button_3.grid(row=4, column=2)

button_minus = tk.Button(numbers, text='-', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_subtract())
button_minus.grid(row=4, column=3)

button_0 = tk.Button(numbers, text='0', padx=47, pady=20, command=lambda: button_click(0))
button_0.grid(row=5, column=0)

button_dot = tk.Button(numbers, text='.', padx=48, pady=20, command=lambda: button_click('.'))
button_dot.grid(row=5, column=1)

button_equal = tk.Button(numbers, text='=', width=3, bg='#00CCFF', fg='white', padx=40, pady=20, command= lambda e: button_equal())
button_equal.grid(row=5, column=2)

button_plus = tk.Button(numbers, text='+', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_add())
button_plus.grid(row=5, column=3)

###################################################################################

button_Rad = tk.Button(functions, text='Rad', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_Rad.grid(row=1, column=0)

button_Deg = tk.Button(functions, text='Deg', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_Deg.grid(row=1, column=1)

button_factorial = tk.Button(functions, text='x!', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_factorial.grid(row=1, column=2)

button_AC = tk.Button(functions, text='AC', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_AC.grid(row=1, column=3)

button_log = tk.Button(functions, text='log', width=3, bg='grey',padx=40, pady=20, command=lambda: button_click)
button_log.grid(row=2, column=0)

button_ln = tk.Button(functions, text='ln', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_ln.grid(row=2, column=1)

button_power = tk.Button(functions, text='X^y', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_power.grid(row=2, column=2)

button_reciprocal = tk.Button(functions, text='1/x', width=3, bg='grey',padx=40, pady=20, command=lambda: button_click)
button_reciprocal.grid(row=2, column=3)

button_sin = tk.Button(functions, text='sin', width=3, bg='grey',padx=40, pady=20, command=lambda: button_click)
button_sin.grid(row=3, column=0)

button_cos = tk.Button(functions, text='cos', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_cos.grid(row=3, column=1)

button_tan = tk.Button(functions, text='tan', width=3, bg='grey',padx=40, pady=20, command=lambda: button_click)
button_tan.grid(row=3, column=2)

button_sqrt = tk.Button(functions, text='sqrt', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_sqrt.grid(row=3, column=3)

button_sinI = tk.Button(functions, text='sin^-1', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_ans())
button_sinI.grid(row=4, column=0)

button_cosI = tk.Button(functions, text='cos^-1', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_cosI.grid(row=4, column=1)

button_tanI = tk.Button(functions, text='tan^-1', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_tanI.grid(row=4, column=2)

button_xroot = tk.Button(functions, text='xroot', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_xroot.grid(row=4, column=3)

button_ans = tk.Button(functions, text='Ans', width=3, bg='grey', padx=40, pady=20, command= lambda e: button_ans())
button_ans.grid(row=5, column=0)

button_Exp = tk.Button(functions, text='Exp', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_Exp.grid(row=5, column=1)

button_pi = tk.Button(functions, text='pi', width=3, bg='grey', padx=40, pady=20, command=lambda: button_click)
button_pi.grid(row=5, column=2)

button_equal = tk.Button(functions, text='=', width=3, bg='#00CCFF', fg='white', padx=40, pady=20, command=lambda: button_click)
button_equal.grid(row=5, column=3)

win.mainloop()