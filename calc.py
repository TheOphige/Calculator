'''Hello, it is me once more. I am using Python 2.3, and I must use Zelle's graphics class (and I must agree with many of you. Tkinter is much better). We have been tasked with creating a Graphical Scientific Calculator. In addition to the normal operators, it must contain the following buttons:
 log - base 10 of display
 ln - base e of display
 exp - e to the display power
 sin - sine of display in radians
 cos - cosine of display in radians
 tan - tangent of display in radians
 sqrt - square root of display
 1/x - reciprocal of display
 X**2 - display squared
 pi - append pi to display for use in successive calculations
 ( - append ( to display
 ) - append ) to display
 MC - clear memory
 MR - append contents of memory to display
 MS - display evaluated and result copied to memory
 M+ - display evaluated and result added to memory
 OFF - close the calculator

I do not believe that I will have trouble calculating most of it. I am hoping someone will help me with organizing the placement of the keys in a visually pleasing manner. I am also unfamiliar with MC, MR, MS, and M+. If someone would be so kind to explain them to me, it would be appreciated. My professor simply ignored me when I asked him what exactly he meant by MC, MR, MS, M+.

The basic calculator starting code that was provided to us:
'''
from graphics import *
from button import Button
from math import pi, e, sin, cos, tan, log, log10, exp, sqrt

class Calculator:
    # This class implements a simple calculator GUI

    def __init__(self):
        # create the window for the calculator
        win = GraphWin("calculator")
        win.setCoords(0,0,9,13.5)   #from (0,0,6,7)
        win.setBackground("slategray")
        self.win = win
        # Now create the widgets
        self.__createButtons()
        self.__createDisplay()

    def __createButtons(self):
        # create list of buttons
        # start with all the standard sized buttons
        # bSpecs gives center coords and label of buttons
        bSpecs = [(2,1,'0'), (3,1,'.'),
                  (1,2,'1'), (2,2,'2'), (3,2,'3'), (4,2,'+'), (5,2,'-'),
                  (1,3,'4'), (2,3,'5'), (3,3,'6'), (4,3,'*'), (5,3,'/'),
                  (1,4,'7'), (2,4,'8'), (3,4,'9'), (4,4,'<-'),(5,4,'C')]
        self.buttons = []
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),.75,.75,label))
        # create the larger = button
        self.buttons.append(Button(self.win, Point(4.5,1), 1.75, .75, "="))
        # activate all buttons
        for b in self.buttons:  b.activate()

    def __createDisplay(self):
        bg = Rectangle(Point(.5,12), Point(8.5,13))   #from (.5,5.5), (5.5,6.5)
        bg.setFill('white')
        bg.draw(self.win)
        text = Text(Point(4.5,12.5), "")   #from (3,6)
        text.draw(self.win)
        text.setFace("courier")
        text.setStyle("bold")
        text.setSize(12)
        self.display = text

    def getButton(self):
        # Waits for a button to be clicked and returns the label of
        #    the button that was clicked.
        while True:
            p = self.win.getMouse()
            for b in self.buttons:
                if b.clicked(p):
                    return b.getLabel() # method exit

    def processButton(self, key):
        # Updates the display of the calculator for press of this key
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            # Backspace, slice off the last character.
            self.display.setText(text[:-1])
        elif key == '=':
            # Evaluate the expresssion and display the result.
            # the try...except mechanism "catches" errors in the
            # formula being evaluated.
            try:
                result = eval(text)
            except: result = 'ERROR'
            self.display.setText(str(result))
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text+key)
        
    def run(self):
        # Infinite 'event loop' to process button clicks.
        while True:
            key = self.getButton()
            self.processButton(key)

# This runs the program.
if __name__ == '__main__':
    # First create a calculator object
    theCalc = Calculator()
    # Now call the calculator's run method.
    theCalc.run()




#Update for the above code:
def __createButtons(self):
        # create list of buttons
        # start with all the standard sized buttons
        # bSpecs gives center coords and label of buttons
        bSpecs = [(2.5,1,'0'), (4,1,'.'), (1,2.5,'1'), (2.5,2.5,'2'), (4,2.5,'3'),
                   (5.5,2.5,'+'), (7,2.5,'-'), (1,4,'4'), (2.5,4,'5'), (4,4,'6'),
                   (5.5,4,'*'), (7,4,'/'), (1,5.5,'7'), (2.5,5.5,'8'), (4,5.5,'9'),
                   (5.5,5.5,'<-'),(7,5.5,'C')]
        bSpecs2 = [(1,1,'OFF'), (2.5,7,'pi'), (4,7,'('), (5.5,7,')'),
                   (7,7,'1/x'), (8.5,1,'ln'), (8.5,2.5,'log'), (8.5,4,'exp'),
                   (8.5,5.5,'sqrt'), (8.5,7,'x**2'), (1,8.5,'M+'), (2.5,8.5,'MS'),
                   (4,8.5,'MR'), (1,7,'MC'), (5.5,8.5,'sin'), (7,8.5,'cos'),
                   (8.5,8.5,'tan')]
        self.buttons = []
        #add to bSpecs
        for cx,cy,label in bSpecs:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,1.5,label))
        for cx,cy,label in bSpecs2:
            self.buttons.append(Button(self.win,Point(cx,cy),1.5,1.5,label))
        # create the larger = button
        self.buttons.append(Button(self.win,Point(6.25,1),3,1.5,"="))
        # activate all buttons
        for b in self.buttons:  b.activate()



def processButton(self, key):
        '''        elif key == 'MS':
            self.memory == eval(text)
        elif key == 'M+':
            self.memory += eval(text)
        elif key == 'MR':
            self.display.setText(text+str(self.memory))
        elif key == 'MC':
            self.memory == 0'''   
        # Updates the display of the calculator for press of this key
        text = self.display.getText()
        if key == 'C':
            self.display.setText("")
        elif key == '<-':
            # Backspace, slice off the last character.
            self.display.setText(text[:-1])
        elif key == '=':
            # Evaluate the expresssion and display the result.
            # the try...except mechanism "catches" errors in the
            # formula being evaluated.
            if 'pi' in text:
                replace(text, pi, math.pi)
            try:
                result = eval(text)
            except:
                result = 'ERROR'
            self.display.setText(str(result))
        elif key == 'log':
            try:
                result = math.log10(eval(text))
            except:
                result = 'ERROR'
            self.display.setText(str(result))
        elif key == 'ln':
            try:
                result = math.log(eval(text))
            except:
                result = 'ERROR'
            self.display.setText(str(result))
        elif key == '1/x':
            try:
                result = 1/(eval(text))
            except:
                result = 'ERROR'
            self.display.setText(str(result))
        elif key == 'sin':
            result = math.sin(eval(text))*(180/math.pi)
            self.display.setText(str(result))
        elif key == 'cos':
            result = math.cos(eval(text))*(180/math.pi)
            self.display.setText(str(result))
        elif key == 'tan':
            result = math.tan(eval(text))*(180/math.pi)
            self.display.setText(str(result))
        elif key == 'sqrt':
            result = math.sqrt(eval(text))
            self.display.setText(str(result))
        elif key == 'exp':
            result = math.e**(eval(text))
            self.display.setText(str(result))
        elif key == 'x**2':
            result = eval(text)**2
            self.display.setText(str(result))
        elif key == 'OFF':
            self.win.close()
        else:
            # Normal key press, append it to the end of the display
            self.display.setText(text+key)


  
from Tkinter import *
from math import *
from random import random

hyps=arc=''
mem=0
resflag=False ## for clearing the display after result automatically without CE

fact=factorial

def calc(s):
    global resflag
    brackc = display.get().count('(') - display.get().count(')')
    try:    display.set(eval('1.0*'+display.get()+')'*brackc)) ## try to fix bracket unbalance
    except: display.set('Error')
    number.icursor('end')
    resflag=True

def push_key(e):
    global resflag
    if 38<=e.x<=202 and 110<=e.y<=236:
        x,y = (e.x-38,e.y-110)
        x,y = (x/32,y/31)
        if isinstance(keys[y][x],basestring):
            if resflag: clear(e)
            resflag=False
            display.set(display.get()+keys[y][x])
            number.icursor('end')
        else: keys[y][x](e)
            
    if 34<=e.x<=201 and 28<=e.y<=101:
        x,y = (e.x-34, e.y-28)
        x,y = (int(x/27.8),int(y/24.3))
        if isinstance(fkeys[y][x],basestring):
            if fkeys[y][x] in ('sin','cos','tan'):
                display.set(hyp(fkeys[y][x])+display.get())
            else:
                if (fkeys[y][x][:2]=='**') or (fkeys[y][x][0] in '()'):
                    display.set(display.get()+fkeys[y][x])
                else:   display.set(fkeys[y][x]+display.get())
            number.icursor('end')
        else: fkeys[y][x](e)
            
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

def hyptoggle(e):
    global hyps
    if hyps:    hyps = ''
    else:       hyps = 'h'
    
def shifttoggle(e):
    global arc,fkeys
    if arc:
        arc =  ''
        panel1.config(image=image1)
        fkeys=bfkeys
    else:
        arc = 'a'
        panel1.config(image=image2)
        fkeys=afkeys       

def hyp(trig): return arc+trig+hyps+'('

def sign(e):
    display.set('-'+display.get())
    calc(e)

def bs(e): display.set(display.get()[:-1])

def xtox(e): display.set(str(display.get())+'**'+str(display.get()))

bfkeys=(('1/(','**0.5','**2','log10(','ln(','**'),
       (shifttoggle,'pi',hyptoggle,'sin','cos','tan'),
       (sign, bs, '(',')',Min,MR))

afkeys=(('fact(','sqrt(',xtox,'10**','e**','**(1/'),
       (shifttoggle,'random()',hyptoggle,'sin','cos','tan'), ## sin,cos,tan by function
       (sign, bs, '(',')',Min,MR))

fkeys=bfkeys

keys=(('7','8','9',clear,ac),
      ('4','5','6','*','/'),
      ('1','2','3','+','-'),
      ('0','.','e',calc,mp))

root=Tk()
display = StringVar()
number=Entry(root,textvariable=display, justify='center')
number.pack(side='top', fill='x', expand='no')
image1 = PhotoImage(file="calc.gif")
image2 = PhotoImage(file="calc2.gif")
w,h = image1.width(), image1.height()
root.title('SimplistiCalc')
root.geometry ="%dx%d+0+0" % (w, h)
panel1 = Label(root, image=image1)
panel1.pack(side='top', fill='both', expand='yes')
number.focus()
number.bind('<Return>',calc)
number.bind('<Escape>',clear)
root.bind('<Button-1>',push_key)
root.mainloop()




if (fkeys[y][x][:2]=='**') or (fkeys[y][x][:2]=='pi') or(fkeys[y][x][0] in '()'):
    display.set(display.get()+fkeys[y][x])
else:
    display.set(fkeys[y][x]+display.get())




def push_key(e):
    global resflag
    if 38<=e.x<=202 and 110<=e.y<=236:
        x,y = (e.x-38,e.y-110)
        x,y = (x/32,y/31)
        if isinstance(keys[y][x],basestring):
            if resflag and keys[y][x] in '0123456789' : clear(e)
            resflag=False
            display.set(display.get()+keys[y][x])
            number.icursor('end')
        else: keys[y][x](e)
            
    if 34<=e.x<=201 and 28<=e.y<=101:
        x,y = (e.x-34, e.y-28)
        x,y = (int(x/27.8),int(y/24.3))
        if isinstance(fkeys[y][x],basestring):
            if fkeys[y][x] in ('sin','cos','tan'):
                display.set(hyp(fkeys[y][x])+display.get())
            else:
                if (fkeys[y][x][:2]=='**') or (fkeys[y][x][:2]=='pi') or(fkeys[y][x][0] in '()'):
                    display.set(display.get()+fkeys[y][x])
                else:   display.set(fkeys[y][x]+display.get())
            number.icursor('end')
        else: fkeys[y][x](e)


