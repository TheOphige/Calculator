from tkinter import Tk, Label, Button, Entry, Text, Toplevel, TOP, BOTTOM, LEFT, RIGHT, CENTER, END, ttk, scrolledtext, Menu, Spinbox, filedialog as fd, messagebox as mBox 
from PIL import Image, ImageTk
from math import pi, e, sin, cos, tan, log, log10, exp, sqrt, pow, atan2, hypot, asinh, degrees, radians, factorial, asin, acos, atan, acosh, atanh

# Creating a Window ===========================================================
win = Tk()
win.title('Calculator')
win.iconbitmap('CALCULATOR LOGO.ico')
#win.geometry('+%d+%d'%(350, 350))
#win.state('zoomed')
#win.attributes('-fullscreen', True)


#logo
logo= Image.open('Calculator.jpg')
logo= logo.resize((int(logo.size[0]/1.8), int(logo.size[1]/1.5)))
logo= ImageTk.PhotoImage(logo)
logo_label = Label(image= logo, bg='white')
logo_label.image= logo
logo_label.grid(column=0, row=0, rowspan=2, sticky='NW', padx=20, pady=10)

entry1= Entry(win)
entry1.grid(row=3, column=0, columnspan=4, padx=10, pady=0)
#entry= Text(win, height=5, width=48)
#entry.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

entry2= Entry(win)
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
def _quit():
      win.quit()
      win.destroy()
      exit() 
def _msg():
      mBox.showinfo('About: Calculator', 'Calculator \nWritten by Theophilus Ige')
def help():
      def _quithelp():
            help_win.destroy()
      
      help_win= Toplevel(win)
      help_win.title('Help: Calculator')
      help_win.iconbitmap('CALCULATOR LOGO.ico')
      texts= 'This tool can be used to download a variety of corpora and models \nthat can be used with NLTK.  Each corpus or model is distributed \nin a single zip file, known as a "package file."  You can \ndownload packages individually, or you can download pre-defined \ncollections of packages.\n\nWhen you download a package, it will be saved to the "download \ndirectory."  A default download directory is chosen when you run \nthe downloader; but you may also select a different download \ndirectory.  On Windows, the default download directory is \n"package." \n\nThe NLTK downloader can be used to download a variety of corpora, \nmodels, and other data packages. '

      ttk.Label(help_win, text= texts).pack(side=TOP, padx=8, pady=4)
      Button(help_win, text="Ok", command= _quithelp).pack(side=BOTTOM, padx=8, pady=4)
win.bind('<F1>', lambda e: help())

def full():
      win.attributes('-fullscreen', not win.attributes('-fullscreen'))
      mBox.showinfo('Fullscreen: Calculator', 'press ESC to exit fullscreen.')
win.bind('<F11>', lambda event: full())

win.bind('<Escape>', lambda event: win.attributes('-fullscreen', False))


menuBar = Menu(numbers)
win.config(menu=menuBar)
        
# Add menu items
fileMenu = Menu(menuBar, tearoff=0)
fileMenu.add_command(label='New           Ctrl-N')
fileMenu.add_separator()
fileMenu.add_command(label='Exit          Ctrl-X', command=_quit)
menuBar.add_cascade(label='File', menu=fileMenu)
        
# Add another Menu to the Menu Bar and an item
helpMenu = Menu(menuBar, tearoff=0)
helpMenu.add_command(label='About', command=_msg)
helpMenu.add_command(label='Instructions  F1', command=help)
menuBar.add_cascade(label='Help', menu=helpMenu)

# Add another Menu to the Menu Bar and an item
viewMenu = Menu(menuBar, tearoff=0)
viewMenu.add_command(label= 'Fullscreen  F11', command=full)
menuBar.add_cascade(label='View', menu=viewMenu)

###################################################################################
entries= [entry1, entry2]
# numbers tab

def Button_click(number):
  #entry.delete(0, END)
  for entry in entries:
      current = entry.get()
      entry.delete(0, END)
      entry.insert(0, str(current) + str(number))
 
def Button_clear():
      for entry in entries:
            entry.delete(0, END)

def Button_add():
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '+')

      first_number= entry2.get()
      global f_num
      global math
      math = "addition"
      f_num = float(first_number)
      entry2.delete(0, END)

def Button_equal():
      second_number = entry2.get()
      entry2.delete(0, END)
      try:
            if math == 'addition':
                  entry2.insert(0, f_num + float(second_number))

            if math == 'subtraction':
                  entry2.insert(0, f_num - float(second_number))

            if math == 'multiplication':
                  entry2.insert(0, f_num * float(second_number))

            if math == 'division':
                  entry2.insert(0, f_num / float(second_number))
            
            if math == 'modulus':
                  entry2.insert(0, f_num % float(second_number))
            
            if math == 'openbckt':
                  entry2.insert(0, f_num)

            if math == 'closebckt':
                  entry2.insert(0, f_num * float(second_number))

            if math == 'degrees':
                  entry2.delete(0, END)
                  entry2.insert(0, degrees(f_num))

            if math == 'radians':
                  entry2.delete(0, END)
                  entry2.insert(0, radians(f_num))

            if math == 'factorial':
                  entry2.delete(0, END)
                  entry2.insert(0, factorial(f_num))

            if math == 'log':
                  entry1.insert(0, entry1.get() + ')') 
                  entry2.insert(0, log(f_num, float(second_number)))

            if math == 'ln':
                  entry2.insert(0, log(f_num))

            if math == 'power':
                  entry2.insert(0, f_num ** float(second_number))

            if math == 'reciprocal':
                  entry2.delete(0, END)
                  entry2.insert(0, 1 / f_num )
            
            if math == 'sin':
                  entry2.delete(0, END)
                  entry2.insert(0, sin(f_num) )

            if math == 'cos':
                  entry2.delete(0, END)
                  entry2.insert(0, cos(f_num) )

            if math == 'tan':
                  entry2.delete(0, END)
                  entry2.insert(0, tan(f_num))

            if math == 'sqrt':
                  entry2.delete(0, END)
                  entry2.insert(0, sqrt(f_num) )
            
            if math == 'asin':
                  entry2.delete(0, END)
                  entry2.insert(0, asin(f_num) )

            if math == 'acos':
                  entry2.delete(0, END)
                  entry2.insert(0, acos(f_num) )

            if math == 'atan':
                  entry2.delete(0, END)
                  entry2.insert(0, atan(f_num))

            if math == 'xroot':
                  entry2.insert(0, f_num % float(second_number))

            if math == 'exp':
                  entry2.insert(0, exp(float(current)))

            if math == 'pi':
                  entry2.delete(0, END)
                  entry2.insert(0, f_num * pi )
                  
      except:
            entry2.insert(0, 'Invalid Syntax')

      global last_equal
      global last_operation
      last_equal = entry2.get()
      last_operation= entry1.get()

def Button_subtract():
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '-')

      first_number= entry2.get()
      global f_num
      global math
      math = "subtraction"
      f_num = float(first_number)
      entry2.delete(0, END)

def Button_multiply():
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + 'x')

      first_number= entry2.get()
      global f_num
      global math
      math = "multiplication"
      f_num = float(first_number)
      entry2.delete(0, END)

def Button_divide():
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '/')

      first_number= entry2.get()
      global f_num
      global math
      math = "division"
      f_num = float(first_number)
      entry2.delete(0, END)

def Button_modulus():
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '%')

      first_number= entry2.get()
      global f_num
      global math
      math = "modulus"
      f_num = float(first_number)
      entry2.delete(0, END)

def Button_openbckt():
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '(')

      first_number= entry2.get()
      global f_num
      global math
      math = "openbckt"
      f_num = first_number
      entry2.delete(0, END)

def Button_closebckt():
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + ')')

      first_number= entry2.get()
      global f_num
      global math
      math = "closebckt"
      f_num = float(first_number)
      entry2.delete(0, END)

button_OPENBCKT = Button(numbers, text='(', width=3, bg='grey', padx=40, pady=20, command=Button_openbckt)
button_OPENBCKT.grid(row=1, column=0)

button_CLOSEBCKT = Button(numbers, text=')', width=3, bg='grey', padx=40, pady=20, command= Button_closebckt)
button_CLOSEBCKT.grid(row=1, column=1)

button_Modulus = Button(numbers, text='%', width=3, bg='grey', padx=40, pady=20, command= Button_modulus)
button_Modulus.grid(row=1, column=2)


button_AC = Button(numbers, text='AC', width=3, bg='grey', padx=40, pady=20, command= Button_clear)
button_AC.grid(row=1, column=3)

button_7 = Button(numbers, text='7', padx=47, pady=20, command=lambda: Button_click(7))
button_7.grid(row=2, column=0)

button_8 = Button(numbers, text='8', padx=47, pady=20, command=lambda: Button_click(8))
button_8.grid(row=2, column=1)

button_9 = Button(numbers, text='9', padx=47, pady=20, command=lambda: Button_click(9))
button_9.grid(row=2, column=2)

button_divide = Button(numbers, text='÷', width=3, bg='grey', padx=40, pady=20, command=Button_divide)
button_divide.grid(row=2, column=3)

button_4 = Button(numbers, text='4', padx=47, pady=20, command=lambda: Button_click(4))
button_4.grid(row=3, column=0)

button_5 = Button(numbers, text='5', padx=47, pady=20, command=lambda: Button_click(5))
button_5.grid(row=3, column=1)

button_6 = Button(numbers, text='6', padx=47, pady=20, command=lambda: Button_click(6))
button_6.grid(row=3, column=2)

button_times = Button(numbers, text='x', width=3, bg='grey', padx=40, pady=20, command=Button_multiply)
button_times.grid(row=3, column=3)

button_1 = Button(numbers, text='1', padx=47, pady=20, command=lambda: Button_click(1))
button_1.grid(row=4, column=0)

button_2 = Button(numbers, text='2', padx=47, pady=20, command=lambda: Button_click(2))
button_2.grid(row=4, column=1)

button_3 = Button(numbers, text='3', padx=47, pady=20, command=lambda: Button_click(3))
button_3.grid(row=4, column=2)

button_minus = Button(numbers, text='-', width=3, bg='grey', padx=40, pady=20, command=Button_subtract)
button_minus.grid(row=4, column=3)

button_0 = Button(numbers, text='0', padx=47, pady=20, command=lambda: Button_click(0))
button_0.grid(row=5, column=0)

button_dot = Button(numbers, text='.', padx=48, pady=20, command=lambda: Button_click('.'))
button_dot.grid(row=5, column=1)

button_equal = Button(numbers, text='=', width=3, bg='#00CCFF', fg='white', padx=40, pady=20, command= Button_equal)
button_equal.grid(row=5, column=2)

button_plus = Button(numbers, text='+', width=3, bg='grey', padx=40, pady=20, command= Button_add)
button_plus.grid(row=5, column=3)

###################################################################################

# functions tab

def Button_Rad():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'Rad(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "radians"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax')  
  

def Button_Deg():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'Deg(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "degrees"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax')  

def Button_factorial():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '!')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "factorial"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax')  
  
def Button_log():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'log(' + str(current) + ',')

      first_number= entry2.get()
      global f_num
      global math
      math = "log"
      f_num = float(first_number)
      entry2.delete(0, END)
  except:
      entry2.insert(0, 'Invalid Syntax') 
  
def Button_ln():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'ln(' + str(current) + ')')

      first_number= entry2.get()
      global f_num
      global math
      math = "ln"
      f_num = float(first_number)
      entry2.delete(0, END)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_power():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '^')

      first_number= entry2.get()
      global f_num
      global math
      math = "power"
      f_num = float(first_number)
      entry2.delete(0, END)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_reciprocal():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, '1 / ' + str(current) )
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "reciprocal"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax')  
 
def Button_sin():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'sin(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "sin"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_cos():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'cos(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "cos"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_tan():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'tan(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "tan"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_sqrt():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, '√' + str(current) + ' ')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "sqrt"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_asin():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'asin(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "asin"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_acos():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'acos(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "acos"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_atan():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'atan(' + str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "atan"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_xroot():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + '√‾')

      first_number= entry2.get()
      global f_num
      global math
      math = "xroot"
      f_num = float(first_number)
      entry2.delete(0, END)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_ans():
      entry1.delete(0, END)
      entry1.insert(0, last_operation)
      entry2.delete(0, END)
      entry2.insert(0, last_equal)

def Button_exp():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, 'Exp('+ str(current) + ')')
      entry2.delete(0, END)
      entry2.insert(0, str(current))
      
      first_number= current
      global f_num
      global math
      math = "pi"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 

def Button_pi():
  try:
      current = entry1.get()
      entry1.delete(0, END)
      entry1.insert(0, str(current) + 'π')
      entry2.delete(0, END)
      entry2.insert(0, pi)
      
      first_number= current
      global f_num
      global math
      math = "pi"
      f_num = float(first_number)
  except:
      entry2.insert(0, 'Invalid Syntax') 


button_Rad = Button(functions, text='Rad', width=3, bg='grey', padx=40, pady=20, command= Button_Rad)
button_Rad.grid(row=1, column=0)

button_Deg = Button(functions, text='Deg', width=3, bg='grey', padx=40, pady=20, command= Button_Deg)
button_Deg.grid(row=1, column=1)

button_factorial = Button(functions, text='x!', width=3, bg='grey', padx=40, pady=20, command= Button_factorial)
button_factorial.grid(row=1, column=2)

button_AC = Button(functions, text='AC', width=3, bg='grey', padx=40, pady=20, command= Button_clear)
button_AC.grid(row=1, column=3)

button_log = Button(functions, text='log', width=3, bg='grey',padx=40, pady=20, command= Button_log)
button_log.grid(row=2, column=0)

button_ln = Button(functions, text='ln', width=3, bg='grey', padx=40, pady=20, command= Button_ln)
button_ln.grid(row=2, column=1)

button_power = Button(functions, text='X^y', width=3, bg='grey', padx=40, pady=20, command= Button_power)
button_power.grid(row=2, column=2)

button_reciprocal = Button(functions, text='1/x', width=3, bg='grey',padx=40, pady=20, command= Button_reciprocal)
button_reciprocal.grid(row=2, column=3)

button_sin = Button(functions, text='sin', width=3, bg='grey',padx=40, pady=20, command= Button_sin)
button_sin.grid(row=3, column=0)

button_cos = Button(functions, text='cos', width=3, bg='grey', padx=40, pady=20, command=Button_cos)
button_cos.grid(row=3, column=1)

button_tan = Button(functions, text='tan', width=3, bg='grey',padx=40, pady=20, command= Button_tan)
button_tan.grid(row=3, column=2)

button_sqrt = Button(functions, text='√‾', width=3, bg='grey', padx=40, pady=20, command= Button_sqrt)
button_sqrt.grid(row=3, column=3)

button_asin = Button(functions, text='asin', width=3, bg='grey', padx=40, pady=20, command= Button_asin)
button_asin.grid(row=4, column=0)

button_acos = Button(functions, text='acos', width=3, bg='grey', padx=40, pady=20, command=Button_acos)
button_acos.grid(row=4, column=1)

button_atan = Button(functions, text='atan', width=3, bg='grey', padx=40, pady=20, command=Button_atan)
button_atan.grid(row=4, column=2)

button_xroot = Button(functions, text='□√‾', width=3, bg='grey', padx=40, pady=20, command=Button_xroot)
button_xroot.grid(row=4, column=3)

button_ans = Button(functions, text='Ans', width=3, bg='grey', padx=40, pady=20, command=Button_ans)
button_ans.grid(row=5, column=0)

button_Exp = Button(functions, text='Exp', width=3, bg='grey', padx=40, pady=20, command=Button_exp)
button_Exp.grid(row=5, column=1)

button_pi = Button(functions, text='π', width=3, bg='grey', padx=40, pady=20, command=Button_pi)
button_pi.grid(row=5, column=2)

button_equal = Button(functions, text='=', width=3, bg='#00CCFF', fg='white', padx=40, pady=20, command= Button_equal)
button_equal.grid(row=5, column=3)

win.mainloop()