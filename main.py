from tkinter import *

root = Tk()
w = 265
h = 270
sw = root.winfo_screenwidth()
hw = root.winfo_screenheight()
x = (sw/2) - (w/2)
y = (hw/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False, False)
root.title('Simple Calculator')

textInput = StringVar()
operator = ''


def btnClick(data):
    global operator
    operator += str(data)
    textInput.set(operator)


def btnClear():
    global operator
    operator = ''
    textInput.set('')


def btnEquals():
    global operator
    result = str(eval(operator))
    textInput.set(result)
    operator = result


calculator = Frame(root, relief=SUNKEN)
calculator.pack()

display = Entry(calculator, font=('courier new', 14), state=DISABLED, textvariable=textInput, insertwidth=4, justify='right')
display.grid(columnspan=4, row=0, column=0, padx=10, pady=20)

btn7 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='7', command=lambda: btnClick(7)).grid(row=1, column=0)
btn8 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='8', command=lambda: btnClick(8)).grid(row=1, column=1)
btn9 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='9', command=lambda: btnClick(9)).grid(row=1, column=2)
btnDiv = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='/', command=lambda: btnClick('/')).grid(row=1, column=3)

btn4 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='4', command=lambda: btnClick(4)).grid(row=2, column=0)
btn5 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='5', command=lambda: btnClick(5)).grid(row=2, column=1)
btn6 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='6', command=lambda: btnClick(6)).grid(row=2, column=2)
btnMul = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='*', command=lambda: btnClick('*')).grid(row=2, column=3)

btn1 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='1', command=lambda: btnClick(1)).grid(row=3, column=0)
btn2 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='2', command=lambda: btnClick(2)).grid(row=3, column=1)
btn3 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='3', command=lambda: btnClick(3)).grid(row=3, column=2)
btnSub = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='-', command=lambda: btnClick('-')).grid(row=3, column=3)

btn0 = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='0', command=lambda: btnClick(0)).grid(row=4, column=0)
btnPoi = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='.', command=lambda: btnClick('.')).grid(row=4, column=1)
btnMod = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='M', command=lambda: btnClick('%')).grid(row=4, column=2)
btnAdd = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='+', command=lambda: btnClick('+')).grid(row=4, column=3)

btnLPar = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='(', command=lambda: btnClick('(')).grid(row=5, column=0)
btnRPar = Button(calculator, padx=1, pady=1, font=('courier new', 14), text=')', command=lambda: btnClick(')')).grid(row=5, column=1)
btnCle = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='C', command=btnClear).grid(row=5, column=2)
btnEqu = Button(calculator, padx=1, pady=1, font=('courier new', 14), text='=', command=btnEquals).grid(row=5, column=3)

root.mainloop()
