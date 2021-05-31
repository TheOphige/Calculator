from bing_calculator import *
# tabs and menubar
def _quit():
      win.quit()
      win.destroy()
      exit() 

def _msg():
      mBox.showinfo('About: Calculator', 'Calculator \nWritten by Theophilus Ige')

def help():
      def _quithelp():
            help_win.destroy()
      
      help_win= tk.Toplevel(win)
      help_win.title('Help: Calculator')
      help_win.iconbitmap('CALCULATOR LOGO.ico')
      texts= 'This tool can be used to download a variety of corpora and models \nthat can be used with NLTK.  Each corpus or model is distributed \nin a single zip file, known as a "package file."  You can \ndownload packages individually, or you can download pre-defined \ncollections of packages.\n\nWhen you download a package, it will be saved to the "download \ndirectory."  A default download directory is chosen when you run \nthe downloader; but you may also select a different download \ndirectory.  On Windows, the default download directory is \n"package." \n\nThe NLTK downloader can be used to download a variety of corpora, \nmodels, and other data packages. '

      ttk.Label(help_win, text= texts).pack(side=tk.TOP, padx=8, pady=4)
      tk.Button(help_win, text="Ok", command= _quithelp).pack(side=tk.BOTTOM, padx=8, pady=4)

def full():
      win.attributes('-fullscreen', not win.attributes('-fullscreen'))
      mBox.showinfo('Fullscreen: Calculator', 'press ESC to exit fullscreen.')

############################################################################################################################################
# numbers tab

def button_click(number):
  #entry.delete(0, END)
  for entry in entries:
      current = entry.get()
      entry.delete(0, tk.END)
      entry.insert(0, str(current) + str(number))
 
def button_clear():
      for entry in entries:
            entry.delete(0, tk.END)

def button_add():
      current = entry1.get()
      entry1.delete(0, tk.END)
      entry1.insert(0, str(current) + '+')

      first_number= entry2.get()
      global f_num
      global math
      math = "addition"
      f_num = float(first_number)
      entry2.delete(0, tk.END)

def button_equal():
      second_number = entry2.get()
      entry2.delete(0, tk.END)
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
            global last_equal
            global last_operation
            last_equal = entry2.get()
            last_operation= entry1.get()
      except:
            entry2.insert(0, 'Invalid Syntax')

def button_subtract():
      current = entry1.get()
      entry1.delete(0, tk.END)
      entry1.insert(0, str(current) + '-')

      first_number= entry2.get()
      global f_num
      global math
      math = "subtraction"
      f_num = float(first_number)
      entry2.delete(0, tk.END)

def button_multiply():
      current = entry1.get()
      entry1.delete(0, tk.END)
      entry1.insert(0, str(current) + 'x')

      first_number= entry2.get()
      global f_num
      global math
      math = "multiplication"
      f_num = float(first_number)
      entry2.delete(0, tk.END)

def button_divide():
      current = entry1.get()
      entry1.delete(0, tk.END)
      entry1.insert(0, str(current) + '/')

      first_number= entry2.get()
      global f_num
      global math
      math = "division"
      f_num = float(first_number)
      entry2.delete(0, tk.END)

def button_modulus():
      current = entry1.get()
      entry1.delete(0, tk.END)
      entry1.insert(0, str(current) + '%')

      first_number= entry2.get()
      global f_num
      global math
      math = "modulus"
      f_num = float(first_number)
      entry2.delete(0, tk.END)

def button_openbckt():
      current = entry1.get()
      entry1.delete(0, tk.END)
      entry1.insert(0, str(current) + '(')

      first_number= entry2.get()
      global f_num
      global math
      math = "openbckt"
      f_num = first_number
      entry2.delete(0, tk.END)

def button_closebckt():
      current = entry1.get()
      entry1.delete(0, tk.END)
      entry1.insert(0, str(current) + ')')

      first_number= entry2.get()
      global f_num
      global math
      math = "closebckt"
      f_num = float(first_number)
      entry2.delete(0, tk.END)


############################################################################################################################################
# functions tab

def function_add():
  return
def clear(e): display.set('')

def ac(e):
    global mem
    clear(e)
    mem=0

def mp(e):
    global mem
    mem=eval(str(mem)+'+'+display.get())

def Min(e):
    global mem
    mem=eval(display.get())

def MR(e):
    global mem
    display.set(display.get()+str(mem))
    
def ln(x): return log(x,e) 

def button_ans():
      entry1.delete(0, tk.END)
      entry1.insert(0, last_operation)
      entry2.delete(0, tk.END)
      entry2.insert(0, last_equal)




    
  degrees(x)
