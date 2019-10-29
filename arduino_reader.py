import serial
from ConnectSSH import ccSSH
import matplotlib

import numpy as np
import matplotlib.pyplot as plt



class zAdjustment:
    def __init__(self, COM, port, threshold, zError):
        #self.ccClient = ccSSH('192.168.0.200', 22, 'root', 'deltatau')
        self.COM=COM
        self.port=port
        self.threshold=threshold
        self.zError = zError
    def adjustHeight(self):
        #ser = serial.Serial('COM11', 115200)
        ser = serial.Serial(self.COM, self.port)
        doKill=False
        value = int(ser.readline().strip())
        valList=[]
        counter=0
        while(True):
            counter+=1
            value = int(ser.readline().strip())
            valList.append(value)
            #plt.scatter(counter,value)
            #plt.xticks(valList)
            #plt.ylim(0,100)
            #plt.hlines(y=self.threshold, xmin=0, xmax=counter, linewidth=2, color='b')
            #plt.pause(0.01)

            if (len(valList)==20):
                print(valList)
                zAve = sum(valList) / len(valList)
                zDiff = zAve - self.threshold
                print("Current Height is " + str(zAve) + "(mm), We are moving to " + str(self.threshold)+"(mm)")
                if(abs(zDiff) >self.zError):
                    doKill = True
                    commandZ = "#2 j^"+str(round(-2105.866142*zDiff+10529))
                    print(commandZ)
                    #self.ccClient.channel.send_line(commandZ)
                    #exit(0)
                else:
                    print("Z Height is already correct!")
                    #exit(0)
            #     if (zDiff > 0):
            #         print("#2 j-   " + str(value))
            #         self.ccClient.channel.send_line("#2 j-")
            #     if (zDiff < 0):
            #         print("#2 j+   " + str(value))
            #         self.ccClient.channel.send_line("#2 j+")
            # else:
            #     value = int(ser.readline().strip())
            #     zDiff = value - self.threshold
            #     if doKill:
            #         if (zDiff == 0):
            #             print("Height is now: " + str(value))
            #             print("#2 kill")
            #             self.ccClient.channel.send_line("#dkill")
            #             exit(0)
            #             doKill = False
        #return value

zCheck = zAdjustment('COM15',9600,71,1)
val = zCheck.adjustHeight()

f = open("zHeights.txt", 'w')
for x in valList:
    f.write(str(x) + '\n')

#plt.title("Z Sensor", loc="left")
#plt.xlabel("Value of Z")
#plt.ylabel("Read #")
#plt.show(linestyle='-', marker='o')

#zCheck = zAdjustment('COM11', 115200, 100, 2)

