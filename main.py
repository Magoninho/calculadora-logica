from tkinter import *
from calculator import *

calculator = Calculator()

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)

    equation_label.set(equation_text)

def equals():

    global equation_text
    
    try:
        calculator.set_expression(equation_text)

        newWindow = Toplevel(window)

        newWindow.title("Resultado")
    
        newWindow.geometry("800x500")
    
        Label(newWindow, 
            text=calculator.get_valuation(), font='mono').pack()
        Label(newWindow, 
            text=calculator.get_truth_table(), font='mono').pack()
    except:
        equation_label.set("Expressão mal formada")
        equation_text = ""

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""

def backspace():
    global equation_text

    equation_label.set(equation_text[:-1])

    equation_text = equation_text[:-1]


window = Tk()
window.title("Calculadora lógica")
window.geometry("500x600")

equation_text = ""

equation_label = StringVar()

label = Label(window, textvariable=equation_label, font=('consolas',20), bg="white", width=24, height=2)
label.pack()

frame = Frame(window)
frame.pack()

buttonA = Button(frame, text='A', height=2, width=3, font=35,
                 command=lambda: button_press('A'))
buttonA.grid(row=0, column=0)

buttonB = Button(frame, text='B', height=2, width=3, font=35,
                 command=lambda: button_press('B'))
buttonB.grid(row=0, column=1)

buttonC = Button(frame, text='C', height=2, width=3, font=35,
                 command=lambda: button_press('C'))
buttonC.grid(row=0, column=2)

buttonD = Button(frame, text='D', height=2, width=3, font=35,
                 command=lambda: button_press('D'))
buttonD.grid(row=0, column=3)

buttonE = Button(frame, text='E', height=2, width=3, font=35,
                 command=lambda: button_press('E'))
buttonE.grid(row=1, column=0)

buttonF = Button(frame, text='F', height=2, width=3, font=35,
                 command=lambda: button_press('F'))
buttonF.grid(row=1, column=1)

buttonG = Button(frame, text='G', height=2, width=3, font=35,
                 command=lambda: button_press('G'))
buttonG.grid(row=1, column=2)

buttonH = Button(frame, text='H', height=2, width=3, font=35,
                 command=lambda: button_press('H'))
buttonH.grid(row=1, column=3)

buttonI = Button(frame, text='I', height=2, width=3, font=35,
                 command=lambda: button_press('I'))
buttonI.grid(row=2, column=0)

buttonJ = Button(frame, text='J', height=2, width=3, font=35,
                 command=lambda: button_press('J'))
buttonJ.grid(row=2, column=1)

buttonK = Button(frame, text='K', height=2, width=3, font=35,
                 command=lambda: button_press('K'))
buttonK.grid(row=2, column=2)

buttonL = Button(frame, text='L', height=2, width=3, font=35,
                 command=lambda: button_press('L'))
buttonL.grid(row=2, column=3)

buttonM = Button(frame, text='M', height=2, width=3, font=35,
                 command=lambda: button_press('M'))
buttonM.grid(row=3, column=0)

buttonN = Button(frame, text='N', height=2, width=3, font=35,
                 command=lambda: button_press('N'))
buttonN.grid(row=3, column=1)

buttonO = Button(frame, text='O', height=2, width=3, font=35,
                 command=lambda: button_press('O'))
buttonO.grid(row=3, column=2)

buttonP = Button(frame, text='P', height=2, width=3, font=35,
                 command=lambda: button_press('P'))
buttonP.grid(row=3, column=3)

buttonQ = Button(frame, text='Q', height=2, width=3, font=35,
                 command=lambda: button_press('Q'))
buttonQ.grid(row=4, column=0)

buttonR = Button(frame, text='R', height=2, width=3, font=35,
                 command=lambda: button_press('R'))
buttonR.grid(row=4, column=1)

buttonS = Button(frame, text='S', height=2, width=3, font=35,
                 command=lambda: button_press('S'))
buttonS.grid(row=4, column=2)

buttonT = Button(frame, text='T', height=2, width=3, font=35,
                 command=lambda: button_press('T'))
buttonT.grid(row=4, column=3)

buttonU = Button(frame, text='U', height=2, width=3, font=35,
                 command=lambda: button_press('U'))
buttonU.grid(row=5, column=0)

buttonV = Button(frame, text='V', height=2, width=3, font=35,
                 command=lambda: button_press('V'))
buttonV.grid(row=5, column=1)

buttonW = Button(frame, text='W', height=2, width=3, font=35,
                 command=lambda: button_press('W'))
buttonW.grid(row=5, column=2)

buttonX = Button(frame, text='X', height=2, width=3, font=35,
                 command=lambda: button_press('X'))
buttonX.grid(row=5, column=3)

buttonY = Button(frame, text='Y', height=2, width=3, font=35,
                 command=lambda: button_press('Y'))
buttonY.grid(row=6, column=0)

buttonZ = Button(frame, text='Z', height=2, width=3, font=35,
                 command=lambda: button_press('Z'))
buttonZ.grid(row=6, column=1)

clear = Button(frame, text='C', height=2, width=3, font=35,
                 command=clear, bg="#f44336", fg="white")

clear.grid(row=0, column=7)

backspace = Button(frame, text='⌫', height=2, width=3, font=35,
                 command=backspace, bg="#ff9800", fg="white")

backspace.grid(row=0, column=8)

open_parenthesis = Button(frame, text='(', height=2, width=3, font=35,
                 command=lambda: button_press('('), bg="#546e7a", fg="white")

open_parenthesis.grid(row=1, column=7)

close_parenthesis = Button(frame, text=')', height=2, width=3, font=35,
                 command=lambda: button_press(')'), bg="#546e7a", fg="white")

close_parenthesis.grid(row=1, column=8)

right_arrow = Button(frame, text='→', height=2, width=3, font=35,
                 command=lambda: button_press('→'), bg="#546e7a", fg="white")

right_arrow.grid(row=2, column=7)

conjunction = Button(frame, text='∧', height=2, width=3, font=35,
                 command=lambda: button_press('∧'), bg="#546e7a", fg="white")

conjunction.grid(row=2, column=8)

biconditional = Button(frame, text='↔', height=2, width=3, font=35,
                 command=lambda: button_press('↔'), bg="#546e7a", fg="white")

biconditional.grid(row=3, column=7)

disjunction = Button(frame, text='v', height=2, width=3, font=35,
                 command=lambda: button_press('v'), bg="#546e7a", fg="white")

disjunction.grid(row=3, column=8)

negation = Button(frame, text='~', height=2, width=3, font=35,
                 command=lambda: button_press('~'), bg="#546e7a", fg="white")

negation.grid(row=4, column=7)

exclusive_disjunction = Button(frame, text='⊻', height=2, width=3, font=35,
                 command=lambda: button_press('⊻'), bg="#546e7a", fg="white")

exclusive_disjunction.grid(row=4, column=8)


equal = Button(frame, text='=', height=2, width=3, font=35,
                 command=equals, bg="#4993c5")
equal.grid(row=5, column=7, columnspan=2, rowspan=2, sticky="news")


# plus = Button(frame, text='+', height=2, width=3, font=35,
#                  command=lambda: button_press('+'))
# plus.grid(row=0, column=3)

# minus = Button(frame, text='-', height=2, width=3, font=35,
#                  command=lambda: button_press('-'))
# minus.grid(row=0, column=4)

# multiply = Button(frame, text='*', height=2, width=3, font=35,
#                  command=lambda: button_press('*'))
# multiply.grid(row=2, column=3)

# divide = Button(frame, text='/', height=2, width=3, font=35,
#                  command=lambda: button_press('/'))
# divide.grid(row=3, column=3)

# equal = Button(frame, text='=', height=2, width=3, font=35,
#                  command=equals)
# equal.grid(row=3, column=2)

# decimal = Button(frame, text='.', height=2, width=3, font=35,
#                  command=lambda: button_press('.'))
# decimal.grid(row=3, column=1)



window.mainloop()

