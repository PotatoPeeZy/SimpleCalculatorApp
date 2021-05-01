import math
from tkinter import *
from math import *

w = Tk()
w.title('Pomato_PeeZy Calculator')
text = Label(w, text='    Pomato_PeeZy Calculator', font=('comic sans MS', 20))
text.grid(row=0, column=0, columnspan=3)
screen = Entry(w, width=20, borderwidth=6, font=('arial', 25))
screen.grid(row=1, column=0, columnspan=4)


def openWindow():
    w2 = Toplevel(w)
    w2.title('Credits')
    c1 = Label(w2, text='Senior Developer: MD Nazmul Hossain Shishir',font = ('arial',15))
    c1.grid(row=0, column=0)
    c2 = Label(w2, text='Junior Developer: Tuba Takowa',font = ('arial',15))
    c2.grid(row=1, column=0)


def degToRad(a):
    return a * (pi / 180)


def numFunc(n):
    s = screen.get()
    s = s + str(n)
    screen.delete(0, END)
    screen.insert(0, s)


def rootFunc():
    s = screen.get()
    screen.delete(0, END)
    screen.insert(0, sqrt(float(s)))


def dotFunc():
    for i in screen.get():
        if i == '.':
            sd = False
        else:
            sd = True
    if sd:
        s = screen.get()
        s = s + '.'
        screen.delete(0, END)
        screen.insert(0, s)


def clrFunc():
    screen.delete(0, END)


def bkscFunc():
    s = ''
    for i in range(len(screen.get()) - 1):
        s = s + screen.get()[i]
    screen.delete(0, END)
    screen.insert(0, s)


def sinFunc():
    s = screen.get()
    screen.delete(0, END)
    screen.insert(0, sin(degToRad(float(s))))


def cosFunc():
    s = screen.get()
    screen.delete(0, END)
    screen.insert(0, cos(degToRad(float(s))))


def tanFunc():
    s = screen.get()
    screen.delete(0, END)
    screen.insert(0, tan(degToRad(float(s))))


n1 = 0
sign = '+'


def operation(o):
    global n1, sign

    n1 = screen.get()
    sign = o
    screen.delete(0, END)


def equalFunc():
    global n1, sign
    n2 = screen.get()
    if sign == '+':
        calc = float(n1) + float(n2)
    if sign == '-':
        calc = float(n1) - float(n2)
    if sign == '*':
        calc = float(n1) * float(n2)
    if sign == '/':
        calc = float(n1) / float(n2)
    screen.delete(0, END)
    screen.insert(0, str(calc))
    sign = '+'
    n1 = 0


button1 = Button(w, text='1', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(1))
button1.grid(row=4, column=0)
button2 = Button(w, text='2', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(2))
button2.grid(row=4, column=1)
button3 = Button(w, text='3', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(3))
button3.grid(row=4, column=2)
button4 = Button(w, text='4', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(4))
button4.grid(row=3, column=0)
button5 = Button(w, text='5', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(5))
button5.grid(row=3, column=1)
button6 = Button(w, text='6', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(6))
button6.grid(row=3, column=2)
button7 = Button(w, text='7', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(7))
button7.grid(row=2, column=0)
button8 = Button(w, text='8', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(8))
button8.grid(row=2, column=1)
button9 = Button(w, text='9', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(9))
button9.grid(row=2, column=2)
button0 = Button(w, text='0', width=10, height=3, bg='pink', borderwidth=6, command=lambda: numFunc(0))
button0.grid(row=5, column=1)
buttonDot = Button(w, text='.', width=10, height=3, bg='pink', borderwidth=6, command=dotFunc)
buttonDot.grid(row=5, column=0)
buttonClr = Button(w, text='C', width=10, height=3, borderwidth=6, command=clrFunc)
buttonClr.grid(row=5, column=2)
buttonPlus = Button(w, text='+', width=10, height=3, bg='#66ffff', borderwidth=6, command=lambda: operation('+'))
buttonPlus.grid(row=2, column=3)
buttonMinus = Button(w, text='-', width=10, height=3, bg='#66ffff', borderwidth=6, command=lambda: operation('-'))
buttonMinus.grid(row=3, column=3)
buttonMul = Button(w, text='X', width=10, height=3, bg='#66ffff', borderwidth=6, command=lambda: operation('*'))
buttonMul.grid(row=4, column=3)
buttonDiv = Button(w, text='/', width=10, height=3, bg='#66ffff', borderwidth=6, command=lambda: operation('/'))
buttonDiv.grid(row=5, column=3)
buttonEqual = Button(w, text='=', width=23, height=3, bg='#d9d9d9', fg='black', borderwidth=6, command=equalFunc)
buttonEqual.grid(row=7, column=2, columnspan=2)
buttonBksc = Button(w, text='<--', width=23, height=3, bg='#d9d9d9', fg='black', borderwidth=6, command=bkscFunc)
buttonBksc.grid(row=7, column=0, columnspan=2)
buttonRoot = Button(w, text='√', width=10, height=3, bg='#66ffff', borderwidth=6, command=rootFunc)
buttonRoot.grid(row=6, column=3)
buttonSin = Button(w, text='Sin()', width=10, height=3, bg='#66ffff', borderwidth=6, command=sinFunc)
buttonSin.grid(row=6, column=0)
buttonCos = Button(w, text='Cos()', width=10, height=3, bg='#66ffff', borderwidth=6, command=cosFunc)
buttonCos.grid(row=6, column=1)
buttonTan = Button(w, text='Tan()', width=10, height=3, bg='#66ffff', borderwidth=6, command=tanFunc)
buttonTan.grid(row=6, column=2)
buttonCredits = Button(w, text='Credits', width=5, height=1, command=openWindow,borderwidth = 2)
buttonCredits.grid(row=0, column=3)

w.mainloop()
