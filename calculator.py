from math import *
from tkinter import *
calculator=Tk()
calculator.title("Calculator")

#function of button
def onclick(t):
    global eq
    global ans
    eq=eq+str(t)
    screen.config(state='normal')
    screen.insert(END,t)
    screen.config(state='disabled')
def onequal():
    global ans
    global eq
    ans=eval(eq)
    screen.config(state='normal')
    screen.delete(1.0,END)
    screen.insert(END,ans)
    eq=str(ans)
    screen.config(state='disabled')
def onclear():
    global eq
    global ans
    screen.config(state='normal')
    eq=""
    screen.delete(1.0,END)
    ans=""
    screen.config(state='disabled')
        
#placing canvas
C=Canvas(calculator,bg="#dedcff",height=170,width=610)
C.grid(row=2,column=0,columnspan=8,rowspan=6)


#making screen
screen=Text(calculator,bg="#dedcff",state='disabled',font=("Helvetica",20),height=2,width=52,fg='black',cursor='arrow')
eq=""
ans=""
screen.grid(row=0,column=0,columnspan=8,rowspan=2)

#creating button
def createButton(t):
    def click():
        onclick(t)
    
    if t=="clear":
        return Button(calculator,text=t,width=25,bd=5,height=2,fg='black',command=onclear) 
    elif t=="=":
        return Button(calculator,text=t,width=17,bd=5,height=2,fg='black',command=onequal)

    return Button(calculator,text=t,width=8,bd=5,height=2,fg='black',command=click) 
      

#creating a button
B1=createButton("INV")
B2=createButton("log")
B3=createButton("(")
B4=createButton(")")
B5=createButton(".")
B6=createButton("+")
B7=createButton("sqrt")
B8=createButton("sin")
B9=createButton("cos")
B10=createButton("tan")
B11=createButton("7")
B12=createButton("8")
B13=createButton("9")
B14=createButton("-")
B15=createButton("%")
B16=createButton("asin")
B17=createButton("acos")
B18=createButton("atan")
B19=createButton("4")
B20=createButton("5")
B21=createButton("6")
B22=createButton("/")
B23=createButton("//")
B24=createButton("pow")
B25=createButton("exp")
B26=createButton("Abs")
B27=createButton("1")
B28=createButton("2")
B29=createButton("3")
B30=createButton("*")
B31=createButton("**")
B32=createButton("ceil")
B33=createButton("floor")
B34=createButton(",")
B35=createButton("0")
B36=createButton("clear")
B37=createButton("=")
#placing all buttons in a list
B=[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11,B12,B13,B14,B15,B16,B17,B18,B19,B20,B21,B22,B23,B24,B25,B26,B27,B28,B29,B30,B31,B32,B33,B34,B35,B36,B37]
#placing the button
c=0
for i in range(2,7):
    for j in range(0,8):
        if c==36:
            B[36].grid(row=6,column=6,columnspan=2)
            break
        elif c==35:
            B[c].grid(row=i,column=j,columnspan=3)
        else:
            B[c].grid(row=i,column=j)
        c=c+1



calculator.mainloop()
