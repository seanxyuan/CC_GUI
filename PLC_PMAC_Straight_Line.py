from tkinter import *
from tkinter import ttk

titles = ['Total Length (mm)','Mixer Start(mm)','Wet Start(mm)','Pump Start(mm)','Mixer Stop(mm)',
          'Wet Stop(mm)','Pump Stop(mm)']
def printtext(varList):
    for x in varList:
        print(x.get())


r = 0
vars=[]
root = Tk()

root.title('PLC Generator')
for c in titles:
    # labelText2 = StringVar()
    # Label(root,text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    # Entry(root, relief=SUNKEN,width=10).grid(row=r,column=1)
    # vars.append(labelText2.get())
    labelText2 = StringVar()
    labelText2.set(c)
    labelDir2 = Label(root, textvariable=labelText2, height=4)
    labelDir2.pack()
    e2 = Entry(root)
    e2.pack()
    e2.focus_set()
    vars.append(e2)
    r = r + 1

b = Button(root,text='Generate PLC Code',command=printtext(vars))
b.pack(side='bottom')
root.mainloop()