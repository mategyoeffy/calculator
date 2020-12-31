# File for calculaor software.


# TIPP:
# Wenn bei dem Button command die Funktion mit Variablen in Klammer übergeben wird, 
# dann wird die Funktion beim ertellen des Fensters auch schon ausgeführt, also Funtiónsnamen nur 
# dazuschreiben und ohne Variablen und Klammern aufschreiben

# LOG:
# Logik für die eigentliche Operation mus noch geschaaffen werden...also 

# Packages:
import numpy as np
from tkinter import *

class Calculator():

    Speicher = {}

    def __init__(self):
        self.greeting = "Welcome, how can I help you?"
        self.b = {}
        self.Speicher["first"] = []
        self.Speicher["second"] = []
        #########################################################################################
        # Label, Button, Entry, Text
        # grid
        #
        #########################################################################################
        self.Fenster_1 = Tk()

        self.Fenster_1.title("Calculator")
        self.Fenster_1.geometry("600x600")

        # the nine number-buttons:
        self.b[0] = Button(self.Fenster_1,text=0,command=self.Fenster_1.destroy,width=5,height=2)
        self.b[0].grid(row=12,column=1)

        self.b[","] = Button(self.Fenster_1,text=",",command=self.comma,width=5,height=2)
        self.b[","].grid(row=12,column=2)

        self.b[1] = Button(self.Fenster_1,text=1,command=self.push1,width=5,height=2)
        self.b[1].grid(row=11,column=1)

        self.b[2] = Button(self.Fenster_1,text=2,command=self.push2,width=5,height=2)
        self.b[2].grid(row=11,column=2)

        self.b[3] = Button(self.Fenster_1,text=3,command=self.push3,width=5,height=2)
        self.b[3].grid(row=11,column=3)

        self.b[4] = Button(self.Fenster_1,text=4,command=self.push4,width=5,height=2)
        self.b[4].grid(row=10,column=1)

        self.b[5] = Button(self.Fenster_1,text=5,command=self.push5,width=5,height=2)
        self.b[5].grid(row=10,column=2)

        self.b[6] = Button(self.Fenster_1,text=6,command=self.push6,width=5,height=2)
        self.b[6].grid(row=10,column=3)

        self.b[7] = Button(self.Fenster_1,text=7,command=self.push7,width=5,height=2)
        self.b[7].grid(row=9,column=1)

        self.b[8] = Button(self.Fenster_1,text=8,command=self.push8,width=5,height=2)
        self.b[8].grid(row=9,column=2)

        self.b[9] = Button(self.Fenster_1,text=9,command=self.push9,width=5,height=2)
        self.b[9].grid(row=9,column=3)


        # the display:
        self.T = Label(self.Fenster_1,text="nothing",height=10,width=30)
        self.T["text"] = self.greeting
        self.T.grid(row=1,columnspan=3)

        # the four operations:
        operations = ["+", "-", "*", "%"]
        
        b1 = Button(self.Fenster_1,text=operations[0],command=self.add,height=2,width=5)
        b2 = Button(self.Fenster_1,text=operations[1],command=self.sub,height=2,width=5)
        b3 = Button(self.Fenster_1,text=operations[2],command=self.mult,height=2,width=5)
        b4 = Button(self.Fenster_1,text=operations[3],command=self.div,height=2,width=5)

        b1.grid(row=5,column=4)
        b2.grid(row=6,column=4)
        b3.grid(rowspan=7,column=4)
        b4.grid(rowspan=8,column=4)

        # equal Button:

        equal_button = Button(self.Fenster_1,text="=",height=10,width=10,command=self.compute)
        equal_button.grid(row=1,column=4)

        self.Fenster_1.mainloop()

# Funktionen:

    def add(self):
        self.Speicher["first"].extend([1+2])
        self.Speicher["operation"] = "+"
        self.compute()
        
    def sub(self):
        self.Speicher["first"].extend([3-1])
        self.Speicher["operation"] = "-"
        self.compute()

    def mult(self):
        self.Speicher["first"].extend([10*2])
        self.Speicher["operation"] = "*"
        self.compute()

    def div(self):
        self.Speicher["first"].extend([12/3])
        self.Speicher["operation"] = "/"
        self.compute()

     
    # Update the Screen
    def compute(self):
        self.T["text"] = self.list2number(self.Speicher["first"])

    def list2number(self,Liste):
        a = [str(i) for i in Liste]
        a_string = "".join(a)
        return float(a_string)
    
    # Action when pushing a button
    def push1(self):
        self.Speicher["first"].extend([1])
        self.compute()
    
    def push2(self):
        self.Speicher["first"].extend([2])
        self.compute()

    def push3(self):
        self.Speicher["first"].extend([3])
        self.compute()

    def push4(self):
        self.Speicher["first"].extend([4])
        self.compute()

    def push5(self):
        self.Speicher["first"].extend([5])
        self.compute()

    def push6(self):
        self.Speicher["first"].extend([6])
        self.compute()

    def push7(self):
        self.Speicher["first"].extend([7])
        self.compute()

    def push8(self):
        self.Speicher["first"].extend([8])
        self.compute()

    def push9(self):
        self.Speicher["first"].extend([9])
        self.compute()
        
    def comma(self):
        self.Speicher["first"].extend(["."])
        self.compute()

simple = Calculator()