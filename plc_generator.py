from tkinter import *
root=Tk()
root.title("PLC Generator for Straight Line Printing in Y Axis")
def retrieve_input():
    readFile = open("plcSample.txt","r")
    outName = "plc"+txtBoxList[0].get("1.0","end-1c")+".plc"
    writeFile = open(outName, "w")
    line =0
    writeFile.write("open plc p" + txtBoxList[0].get("1.0", "end-1c")+"\n")
    readFile.readline()
    while line<16:
        writeFile.write(readFile.readline())
        line+=1
    line = 0
    readFile.readline()
    writeFile.write("jog8="+str(int(txtBoxList[1].get("1.0","end-1c"))*1366)+";"+"\n")
    readFile.readline()
    writeFile.write("while(motor[8].Pos<"+str(int(txtBoxList[1].get("1.0","end-1c"))*1366 - int(txtBoxList[2].get("1.0","end-1c"))*1366)
                    +"{} // Stop Wet "+txtBoxList[2].get("1.0","end-1c") +"mm to the end"+"\n")
    readFile.readline()
    writeFile.write(readFile.readline())
    writeFile.write("while(motor[8].Pos<" + str(int(txtBoxList[1].get("1.0","end-1c")) * 1366 - int(txtBoxList[3].get("1.0","end-1c")) * 1366)
                    + "{} // Stop Mixer "+ txtBoxList[3].get("1.0","end-1c")  + "mm to the end"+"\n")
    readFile.readline()
    writeFile.write(readFile.readline())
    writeFile.write(readFile.readline())
    writeFile.write("call Timer("+txtBoxList[4].get("1.0","end-1c")+") // Stop Pump with"+txtBoxList[4].get("1.0","end-1c") + " delay"+"\n")
    readFile.readline()
    while line <12:
        writeFile.write(readFile.readline())
        line+=1
    writeFile.write("disable plc p"+txtBoxList[0].get("1.0","end-1c")+";"+"\n")
    writeFile.write("close"+"\n")

    readFile.close()
    writeFile.close()
txtBoxList=[]
titles = ['PLC Program Number','Total Length (mm)','Wet Stop(mm)',
          'Mixer Stop(mm)','Pump Stop(second)']
r = 0
for t in titles:
    label = Label(root, text=t)
    label.grid(row=r,column=0)
    textBox=Text(root,height=2, width=20)
    textBox.grid(row=r, column=1)
    r +=1
    txtBoxList.append(textBox)

buttonCommit=Button(root, height=2, width=30, text="Generate PLC",
                    command=lambda: retrieve_input())
buttonCommit.grid(row=2, column=2)
mainloop()