from tkinter import *
import math

screen= Tk()
screen.title("calculater by muhammad yousaf")
screen.geometry("320x447")
screen.iconbitmap('favicon.ico')

def click(b):
    global input
    input+=b
    output.set(input)

def clear():
   global input
   input= ''
   output.set("")
def torad(x):
  x*=math.pi/180
  return x

def sin():
    global input
    try:
     result= eval(input)
     result= torad(result)
     result= math.sin(result)
     input= str(result)
     output.set(result)
    except:
     output.set('invalid input')
     input= ''


def log():
    global input
    try:
     result= eval(input)
     result= math.log(result)
     input= str(result)
     output.set(result)
    except:
     output.set('invalid input')
     input= ''
   

def sqrt():
    global input
    try:
     result= eval(input)
     result= math.sqrt(result)
     input= str(result)
     output.set(result)
    except:
     output.set('invalid input')
     input= ''
   
def cos():
    global input
    try:
     result= eval(input)
     result= math.cos(result)
     input= str(result)
     output.set(result)
    except:
     output.set('invalid input')
     input= ''
   
def tan():
    global input
    try:
     result= eval(input)
     result= math.tan(result)
     input= str(result)
     output.set(result)
    except:
     output.set('invalid input')
     input= ''
   
   
def equals():
    global input
    try:
     result= eval(input)
     input= str(result)
     output.set(result)
    except:
     output.set('invalid input')
     input= ''
    



output = StringVar()
input= ''

result= Entry(screen, bg= "light gray",font=('Segoe UI',24,'bold'),justify="right",textvariable=output)
result.place(y=0,x=0,height=60,width=320)


bsin= Button(screen,text='sin',font=('Segoe UI',20,'bold'),command= sin )
bsin.place(x=0,y=60,height=77,width=64)

broot= Button(screen,text='sqrt',font=('Segoe UI',20,'bold'),command=sqrt)
broot.place(x=64,y=60,height=77,width=64)

bopenbrace= Button(screen,text='(',font=('Segoe UI',20,'bold'),command=lambda:click('('))
bopenbrace.place(x=128,y=60,height=77,width=64)

bclosebrace= Button(screen,text=')',font=('Segoe UI',20,'bold'),command=lambda:click(')'))
bclosebrace.place(x=192,y=60,height=77,width=64)

bdivide= Button(screen,text='➗',font=('Segoe UI',20,'bold'),command=lambda:click('/'))
bdivide.place(x=256,y=60,height=77,width=64)

#row2

bcose= Button(screen,text='cos',font=('Segoe UI',20,'bold'),command=cos)
bcose.place(x=0,y=137,height=77,width=64)

b7= Button(screen,text='7',font=('Segoe UI',20,'bold'),command=lambda:click('7'))
b7.place(x=64,y=137,height=77,width=64)

b8= Button(screen,text='8',font=('Segoe UI',20,'bold'),command=lambda:click('8'))
b8.place(x=128,y=137,height=77,width=64)

b9= Button(screen,text='9',font=('Segoe UI',20,'bold'),command=lambda:click('9'))
b9.place(x=192,y=137,height=77,width=64)

bmul= Button(screen,text='x',font=('Segoe UI',20,'bold'),command=lambda:click('*'))
bmul.place(x=256,y=137,height=77,width=64)


#row3

btan= Button(screen,text='tan',font=('Segoe UI',20,'bold'),command=tan)
btan.place(x=0,y=214,height=77,width=64)

b4= Button(screen,text='4',font=('Segoe UI',20,'bold'),command=lambda:click('4'))
b4.place(x=64,y=214,height=77,width=64)

b5= Button(screen,text='5',font=('Segoe UI',20,'bold'),command=lambda:click('5'))
b5.place(x=128,y=214,height=77,width=64)

b6= Button(screen,text='6',font=('Segoe UI',20,'bold'),command=lambda:click('6'))
b6.place(x=192,y=214,height=77,width=64)

bsub= Button(screen,text='-',font=('Segoe UI',20,'bold'),command=lambda:click('-'))
bsub.place(x=256,y=214,height=77,width=64)

#row 4


bin= Button(screen,text='In',font=('Segoe UI',20,'bold'),command=log)
bin.place(x=0,y=291,height=77,width=64)

b1= Button(screen,text='1',font=('Segoe UI',20,'bold'),command=lambda:click('1'))
b1.place(x=64,y=291,height=77,width=64)

b2= Button(screen,text='2',font=('Segoe UI',20,'bold'),command=lambda:click('2'))
b2.place(x=128,y=291,height=77,width=64)

b3= Button(screen,text='3',font=('Segoe UI',20,'bold'),command=lambda:click('3'))
b3.place(x=192,y=291,height=77,width=64)

badd= Button(screen,text='+',font=('Segoe UI',20,'bold'),command=lambda:click('+'))
badd.place(x=256,y=291,height=77,width=64)

#row5


bpow= Button(screen,text='x^y',font=('Segoe UI',20,'bold'),command=lambda:click('x^y'))
bpow.place(x=0,y=368,height=77,width=64)

bc= Button(screen,text='c',font=('Segoe UI',20,'bold'),command= clear)
bc.place(x=64,y=368,height=77,width=64)

b0= Button(screen,text='0',font=('Segoe UI',20,'bold'),command=lambda:click('0'))
b0.place(x=128,y=368,height=77,width=64)

bdot= Button(screen,text='.',font=('Segoe UI',20,'bold'),command=lambda:click('.'))
bdot.place(x=192,y=368,height=77,width=64)

bequal= Button(screen,text='=',font=('Segoe UI',20,'bold'),command= equals)
bequal.place(x=256,y=368,height=77,width=64)



screen.mainloop()

