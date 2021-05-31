import tkinter
from tkinter import *
from cmath import log, log10, pi, e, sin, cos, sqrt, tan, sinh, cosh, tanh
from math import pow, atan2, hypot, asinh, degrees, radians, asin, acos, atan, acosh, atanh #, factorialcarry2
def get_list(event=None):
  global carry
  index = list1.curselection()[0]
  seltext = list1.get(index) + '\n'
  text1.delete(0, last='end')
  text1.insert(0, seltext)
  if 'Law' in seltext and 'Cosines' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'side 1')
    input2.delete(0, last='end')
    input2.insert(0,'side 2')
    input3.delete(0, last='end')
    input3.insert(0,'angle')
    input4.delete(0, last='end')
    carry = seltext
  if 'Law' in seltext and 'Sines' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'side 1')
    input2.delete(0, last='end')
    input2.insert(0,'angle 1')
    input3.delete(0, last='end')
    input3.insert(0,'angle 2')
    input4.delete(0, last='end')
    carry = seltext
  elif 'Volume' in seltext and 'Sphere' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'radius')
    input2.delete(0, last='end')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext
  elif 'Surface' in seltext and 'Sphere' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'radius')
    input2.delete(0, last='end')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext
  elif 'Volume' in seltext and 'Cylinder' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'radius')
    input2.delete(0, last='end')
    input2.insert(0,'height')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Surface' in seltext and 'Cylinder' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'radius')
    input2.delete(0, last='end')
    input2.insert(0,'height')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Volume' in seltext and 'Cone' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'radius')
    input2.delete(0, last='end')
    input2.insert(0,'height')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Surface' in seltext and 'Cone' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'radius')
    input2.delete(0, last='end')
    input2.insert(0,'height')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Hypot' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'side 1')
    input2.delete(0, last='end')
    input2.insert(0,'side 2')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Own' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'Enter Formula')
    input2.delete(0, last='end')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Compound' in seltext and 'Interest' in seltext and 'Rate' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'principle')
    input2.delete(0, last='end')
    input2.insert(0,'final amount')
    input3.delete(0, last='end')
    input3.insert(0,'Times/Year Calculated')
    input4.delete(0, last='end')
    input4.insert(0,'number of years')
    carry = seltext

  elif 'Compound' in seltext and 'Interest' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'principle')
    input2.delete(0, last='end')
    input2.insert(0,'annual %')
    input3.delete(0, last='end')
    input3.insert(0,'Times/Year Calculated (use c for continuous)')
    input4.delete(0, last='end')
    input4.insert(0,'number of years')
    carry = seltext

  elif 'Decay' in seltext and 'Time' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'half life')
    input2.delete(0, last='end')
    input2.insert(0,'% remaining')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Decay' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'initial amount')
    input2.delete(0, last='end')
    input2.insert(0,'half life')
    input3.delete(0, last='end')
    input3.insert(0,'time in same unit as half life')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Annuity' in seltext and 'Sum' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'amount added')
    input2.delete(0, last='end')
    input2.insert(0,'interest')
    input3.delete(0, last='end')
    input3.insert(0,'years')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Annuity' in seltext and 'Addition' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'total')
    input2.delete(0, last='end')
    input2.insert(0,'interest')
    input3.delete(0, last='end')
    input3.insert(0,'years')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Annuity' in seltext and 'Years' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'total')
    input2.delete(0, last='end')
    input2.insert(0,'interest')
    input3.delete(0, last='end')
    input3.insert(0,'addition')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Mortgage' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'principle')
    input2.delete(0, last='end')
    input2.insert(0,'interest')
    input3.delete(0, last='end')
    input3.insert(0,'years')
    input4.delete(0, last='end')
    carry = seltext

  elif 'Fibon' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'number of iterations')
    input2.delete(0, last='end')
    input3.delete(0, last='end')
    input4.delete(0, last='end')
    carry = seltext
  elif 'Progress' in seltext:
    input1.delete(0, last='end')
    input1.insert(0,'number')
    input2.delete(0, last='end')
    input2.insert(0,'power')
    input3.delete(0, last='end')
    input3.insert(0,'number of iterations')
    input4.delete(0, last='end')
    carry = seltext

  input1.focus()

def get_list2(event=None):
  global carry2
  index2 = list2.curselection()[0]
  seltext2 = list2.get(index2) + '\n'
  carry2 = seltext2

def callback():
  text1.delete(0, last='end')
  if 'Law' in carry and 'Cosines' in carry:
    b = eval(input1.get()) + 0j
    c = eval(input2.get()) + 0j
    cosa = eval(input3.get())
    cosa = cos(radians(cosa)) + 0j
    a = sqrt((b**2 + c**2) - (2*b*c*cosa))
  elif 'Law' in carry and 'Sines' in carry:
    sinv1 = eval(input2.get())
    sinv2 = eval(input3.get())
    sinv1 = sin(radians(sinv1)) + 0j
    sinv2 = sin(radians(sinv2)) + 0j
    v2 = eval(input1.get())
    a = v2 * (sinv2/sinv1)
  elif 'Volume' in carry and 'Sphere' in carry:
    a = eval(input1.get())
    a = (pi * a ** 3) * (4/ 3)
  elif 'Surface' in carry and 'Sphere' in carry:
    a = eval(input1.get())
    a = 4 * pi * a**2
  elif 'Volume' in carry and 'Cylinder' in carry:
    a = pi * eval(input1.get())**2 * eval(input2.get())
  elif 'Surface' in carry and 'Cylinder' in carry:
    a = 2 * pi * eval(input1.get())**2 +  2 * pi * eval(input1.get())  * eval(input2.get())
  elif 'Volume' in carry and 'Cone' in carry:
    a = (pi * eval(input1.get())**2 * eval(input2.get())) / 3
  elif 'Surface' in carry and 'Cone' in carry:
    a = pi*eval(input1.get())*eval(input2.get())+ pi*eval(input1.get())**2
  elif 'Compound' in carry and 'Interest' in carry and 'Rate' in carry:
    p,fv,f,n = eval(input1.get()),eval(input2.get()),eval(input3.get()),eval(input4.get())
    n = n * f
    a = (((fv/p)**(1/n)) - 1) *f*100
  elif 'Compound' in carry and 'Interest' in carry:
    if input3.get() == 'c':
      a = eval(input1.get()) * (e**((eval(input2.get())/100) * eval(input4.get())))
    else:
      p = eval(input1.get())
      i = eval(input2.get())
      f = eval(input3.get())
      n = eval(input4.get())
      a = p*((1 + (i/100) /f)**(f*n))
  elif 'Decay' in carry and 'Time' in carry:
    k,rem = (-log(2))/ eval(input1.get()),(eval(input2.get()))/100
    a = (log(rem))/k
  elif 'Decay' in carry:
    k = (-log(2))/ eval(input2.get())
    a = eval(input1.get()) * (e**(k * eval(input3.get())))
  elif 'Hypot' in carry:
    b = eval(input1.get())
    c =  eval(input2.get())
    a = hypot(b,c)
  elif 'Annuity' in carry and 'Sum' in carry:
    a = eval(input1.get()) * ((1 + eval(input2.get())/100) ** (eval(input3.get()) + 1)- 1) / (eval(input2.get())/100) - eval(input1.get())
  elif 'Annuity' in carry and 'Addition' in carry:
    r = eval(input2.get()) / 100
    a = eval(input1.get()) / ((((1 + r) ** (eval(input3.get()) + 1) - 1) / r) - 1)
  elif 'Annuity' in carry and 'Years' in carry:
    r = (eval(input2.get()) / 100) + 0j
    t = eval(input1.get()) + 0j
    i = eval(input3.get()) + 0j
    a =   (log((r * (t/i)) + (1 + r))) / log(1 + r)
  elif 'Mortgage' in carry:
    r = eval(input2.get()) / 1200
    t = eval(input3.get()) * 12
    a = r * eval(input1.get()) / ( 1 - (1 + r) ** -t)
  elif 'Fibon' in carry:
    lim = eval(input1.get())
    y,x,z,a=0,1,0,0
    b=''
    while z < lim:
      z = z + 1
      b = ' ' + str(y)
      y,x=x,x+y
      text1.insert(END, b)
  elif 'Progress' in carry:
    n,p,z,lim,a,x,c=0,0,0,0,0,0,0
    b = ''
    n = eval(input1.get())
    c = n
    x = n
    p = eval(input2.get())
    lim = eval(input3.get())
    while z < lim:
      z = z + 1
      b =' ' + str(n)
      text1.insert(END, b)
      n = c**p + x
      x = n
  elif 'Own' in carry:
    a = eval(input1.get())
    if abs(a - 0.00000000000) < .0000000001:
      a = 0
    if abs(a - .50000000000) < .0000000001:
      a = .5
    if abs(a - 1.00000000000) < .0000000001:
      a = 1.0
    if abs(a - 2.00000000000) < .0000000001:
      a = 2.0
    if abs(a - -.50000000000) < .0000000001:
      a = -.5
    if abs(a - 30.00000000000) < .0000000001:
      a = 30.0
    if abs(a - 45.00000000000) < .0000000001:
      a = 45.0
    if abs(a - 60.00000000000) < .0000000001:
      a = 60.0
    if abs(a - 90.00000000000) < .0000000001:
      a = 90.0
    if abs(a - 120.00000000000) < .0000000001 or abs(a - -60.00000000000) < .0000000001:
      a = 120.0
    if abs(a - 135.00000000000) < .0000000001:
      a = 135.0
    if abs(a - 150.00000000000) < .0000000001 or abs(a - -30.00000000000) < .0000000001:
      a = 150.0
    if abs(a - 180.00000000000) < .0000000001:
      a = 180.0
  if 'general' in carry2:
    a =  '{0:g}'.format(a)
  elif 'expon' in carry2:
    a =  '{0:e}'.format(a)
  elif 'binary' in carry2:
    a =  '{0:b}'.format(a)
  elif 'oct' in carry2:
    a =  '{0:o}'.format(a)
  elif 'hex' in carry2:
    a =  '{0:x}'.format(a)
  elif '1 decimal' in carry2:
    a = '{0:.1f}'.format(a)
  elif '2 decimal' in carry2:
    a = '{0:.2f}'.format(a)
  elif '3 decimal' in carry2:
    a = '{0:.3f}'.format(a)
  elif '4 decimal' in carry2:
    a = '{0:.4f}'.format(a)
  elif '5 decimal' in carry2:
    a = '{0:.5f}'.format(a)
  elif '6 decimal' in carry2:
    a = '{0:.6f}'.format(a)

  text1.insert(0, str(a))

window = tkinter.Tk()
window.title('GUI Calculator')
window.geometry('+%d+%d'%(1200, 480))
text1 = tkinter.Entry(window, width=200)
input1 = tkinter.Entry(window, width=200)
input2 = tkinter.Entry(window, width=200)
input3 = tkinter.Entry(window, width=200)
input4 = tkinter.Entry(window, width=200)
list1 = tkinter.Listbox(window, height='22', width='100')
list2 = tkinter.Listbox(window, height='22', width='100')
b = Button(text='Calculate', width='20',command=callback)

text1.grid(row=0, columnspan=2)
input1.grid(row=1, columnspan=2)
input2.grid(row=2, columnspan=2)
input3.grid(row=3, columnspan=2)
input4.grid(row=4, columnspan=2)
list1.grid(row=5)
list2.grid(row=5, column=1)
b.grid(row=6, columnspan=2)
text1.insert(0,'Calculation Result')
list1.insert(END, 'Law of Cosines')
for item in ['Law of Sines', 'Hypotenuse', 'Volume of Sphere', 'Surface of Sphere', 'Volume of Cylinder', 'Surface of Cylinder', 'Volume of Cone', 'Surface of Cone', 'Compound Interest', 'Compound Interest Rate', 'Decay', 'Decay Time', 'Annuity Sum', 'Annuity Addition', 'Annuity Years', 'Mortgage', 'Fibonacci Sequence', 'Sum of Progression', 'Own Formula']:
  list1.insert(END, item)
  list1.bind('<ButtonRelease-1>', get_list)
  list2.insert(END, 'general')
for item in ['exponential', 'binary', 'octal', 'hex', '1 decimal place','2 decimal places','3 decimal places','4 decimal places','5 decimal places','6 decimal places']:
  list2.insert(END, item)
  list2.bind('<ButtonRelease-1>', get_list2)
window.mainloop()

