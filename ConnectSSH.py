import datetime as dt
from time import sleep
from tkinter import *
from tkinter import ttk

import paramiko
from PIL import ImageTk

from ppmac import pp_comm

now = dt.datetime.now()
log_name="GUI_log_"+str(now.year)+"-"+str(now.month)+"-"+str(now.day)+"_"\
         +str(now.hour)+"-"+str(now.minute)+"-"+str(now.second)
f=open(log_name+".txt",'w')
global layerNumber
layerNumber=1
class ccSSH:
    def __init__(self, hostname, port, username, password):
        self.sshClient = paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshClient.load_system_host_keys()
        self.sshClient.connect(hostname, port, username, password,timeout=6000)
        print('PMAC Connection Successful ...')
        print('Write Commands:')
        self.comm = pp_comm.PPComm(host=hostname, port=port, user=username, password=password)
        #self.channel = self.comm.shell_channel()
        #self.channel.send_line('gpascii')

        self.channel = self.comm.gpascii #gpascii channel is exactly like shell cannel but it has more capabilities
                                                # it has more methods added, and it is already inside gpascii mode
        #self.channel.send_line('\n')
    # def enterCommand(self,cmd):
    #     stdin, stdout, stderr = self.sshClient.exec_command(cmd)
    #     for line in stdout.readlines():
    #         print (line)

#=================================================================
#Robot Control Functions Defined for Buttons and Scale Bars:
class buttonBools:
    bState=True
    def __init__(self, bState):
        self.bState=bState

def nozzleLeftOn(client):
    client.channel.send_line("left=1")

def nozzleLeftOff(client):
    client.channel.send_line("left=0")

def nozzleRightOn(client):
    client.channel.send_line("right=1")

def nozzleRightOff(client):
    client.channel.send_line("right=0")


def nozzleCenterOn(client):
    client.channel.send_line("center=1")


def nozzleCenterOff(client):
    client.channel.send_line("center=0")


def nozzleValveOn(client):
    client.channel.send_line("valve=1")


def nozzleValveOff(client):
    client.channel.send_line("valve=0")


def activateMotors(client):
    client.channel.send_line("enable plc gantrysafety")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("Motor[4].CmdMotor = 1")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("Motor[4].ServoCtrl = 8")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#1 $")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#4 $")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#1 j/")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#4 j/")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#8 $")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#8 j/")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#7 $")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#7 j/")
    sleep(0.1)  # Time in seconds.
    # client.channel.send_line("#6 $")
    # sleep(0.05)  # Time in seconds.
    # client.channel.send_line("#6 j/")
    # sleep(0.05)  # Time in seconds.
    client.channel.send_line("#2 $")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#2 kill")
    sleep(0.1)  # Time in seconds.
    f.write("activate_Motors"+'\n')

def raiseZ(client,inchAmount):
    zCMD = "#2 j^"+str(inchAmount*5500) #inchAmount * 0.1 inch
    client.channel.send_line(zCMD)
    f.write(zCMD + '\n')

def cutter(client):
    client.channel.send_line("cut=1")
    sleep(1.5)  # Time in seconds.
    client.channel.send_line("cut=0")
    f.write("cut=1"+'\n')
    f.write("sleep 1.5 second"+'\n')
    f.write("cut=0"+'\n')

def homeAlpha(client):
    client.channel.send_line("#7 kill")
    sleep(0.5)  # Time in seconds.
    client.channel.send_line("motor[7].Pos=0")
    sleep(0.5)  # Time in seconds.
    f.write("#7 kill"+'\n')
    f.write("motor[7].Pos=0" + '\n')

def plcRun(client, plcName):
    plcCMD = "enable plc " + plcName
    client.channel.send_line(plcCMD)
    f.write("Layer Printing" + '\n')
    f.write(plcCMD+'\n')

def progRunnerwithZ(client, progNumber):
    client.channel.send_line("#2 j^137500")
    sleep(14)
    client.channel.send_line("#2 j=0")
    sleep(16)
    client.channel.send_line("#2 kill")
    sleep(2)
    client.channel.send_line("left=1")
    client.channel.send_line("right=0")
    sleep(0.5)  # Time in seconds.
    client.channel.send_line("left=0")
    client.channel.send_line("right=1")
    sleep(0.5)  # Time in seconds.
    client.channel.send_line("center=1")
    sleep(0.5)  # Time in seconds.
    client.channel.send_line("valve=1")
    sleep(0.5)  # Time in seconds.
    client.channel.send_line("center=0")
    sleep(0.5)  # Time in seconds.
    client.channel.send_line("valve=0")
    sleep(0.5)  # Time in seconds.
    progCMD = "#1 #8 #7 J/ &1 B" + progNumber +" r"
    client.channel.send_line(progCMD)
    f.write(progCMD+'\n')

def progRunner(client, progNumber):

    # client.channel.send_line("left=1")
    # client.channel.send_line("right=0")
    # sleep(0.5)  # Time in seconds.
    # client.channel.send_line("left=0")
    # client.channel.send_line("right=1")
    # sleep(0.5)  # Time in seconds.
    # client.channel.send_line("center=1")
    # sleep(0.5)  # Time in seconds.
    # client.channel.send_line("valve=1")
    # sleep(0.5)  # Time in seconds.
    # client.channel.send_line("center=0")
    # sleep(0.5)  # Time in seconds.
    # client.channel.send_line("valve=0")
    # sleep(0.5)  # Time in seconds.
    progCMD = "#1 #8 #7 J/ &1 B" + progNumber +" r"
    client.channel.send_line(progCMD)
    f.write(progCMD+'\n')

def protate(client):
    client.channel.send_line("#7 j^227.5") # 1 degree
    f.write("#7 j^227.5"+'\n')

def mrotate(client):
    client.channel.send_line("#7 j^-227.5") # -1 degree
    f.write("#7 j^-227.5"+'\n')

def py(client):
    client.channel.send_line("#8 j+")
    f.write("#8 j+"+'\n')

def my(client):
    client.channel.send_line("#8 j-")
    f.write("#8 j-"+'\n')

def stop8(client):
    #client.channel.send_line("#8 j/")
    client.channel.send_line("#8 j/")
    f.write("#8 j/"+'\n')

def zero1and4(client):
    client.channel.send_line("#1 kill")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("#4 kill")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("motor[1].Pos=0")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("motor[4].Pos=0")
    f.write("#1 kill"+'\n')
    f.write("#4 kill" + '\n')
    f.write("motor[1].Pos=0"+'\n')
    f.write("motor[4].Pos=0" + '\n')


def zero8(client):
    client.channel.send_line("#8 kill")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("motor[8].Pos=0")
    f.write("#8 kill"+'\n')
    f.write("motor[8].Pos=0"+'\n')

def moveUp(client):
    client.channel.send_line("#2 j+")
    #client.channel.send_line("#2 j^60500")
    f.write("#2 j+"+'\n')

def moveDown(client):
    client.channel.send_line("#2 j-")
    #client.channel.send_line("#2 j^-5500")
    f.write("#2 j-"+'\n')

def kill2(client):

    client.channel.send_line("#2 kill")
    f.write("#2 kill"+'\n')

def zero2(client):
    client.channel.send_line("#2 kill")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("motor[2].Pos=0")
    f.write("#2 kill"+'\n')
    f.write("motor[2].Pos=0"+'\n')

def px(client):
    #client.channel.send_line("#1 $")
    #client.channel.send_line("#1 j/")
    #client.channel.send_line("#4 $")
    #client.channel.send_line("#4 $j/")
    client.channel.send_line("#1 j+")
    f.write("#1 j+"+'\n')

def mx(client):
    #client.channel.send_line("#1 $")
    #client.channel.send_line("#1 j/")
    #client.channel.send_line("#4 $")
    #client.channel.send_line("#4 $j/")
    client.channel.send_line("#1 j-")
    f.write("#1 j-"+'\n')

def stop1(client):
    #client.channel.send_line("#1 $")
    #client.channel.send_line("#1 j/")
    #client.channel.send_line("#4 $")
    #client.channel.send_line("#4 $j/")
    client.channel.send_line("#1 j/")
    f.write("#1 j/"+'\n')

def xSpeedChange(client):
    client.channel.send_line("motor[1].JogSpeed = motor[1].JogSpeed + 10")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("motor[4].JogSpeed = motor[4].JogSpeed + 10")
    f.write("motor[1].JogSpeed = motor[1].JogSpeed + 10"+'\n')
    f.write("motor[4].JogSpeed = motor[4].JogSpeed + 10"+'\n')

def xMSpeedChange(client):
    client.channel.send_line("motor[1].JogSpeed = motor[1].JogSpeed - 10")
    sleep(0.1)  # Time in seconds.
    client.channel.send_line("motor[4].JogSpeed = motor[4].JogSpeed - 10")
    f.write("motor[1].JogSpeed = motor[1].JogSpeed - 10"+'\n')
    f.write("motor[4].JogSpeed = motor[4].JogSpeed - 10"+'\n')

def ySpeedChange(client):
    client.channel.send_line("motor[8].JogSpeed = motor[8].JogSpeed + 10")
    f.write("motor[8].JogSpeed = motor[8].JogSpeed + 10"+'\n')

def yMSpeedChange(client):
    client.channel.send_line("motor[8].JogSpeed = motor[8].JogSpeed - 10")
    f.write("motor[8].JogSpeed = motor[8].JogSpeed - 10"+'\n')

def zSpeedChange(client):
    client.channel.send_line("motor[2].JogSpeed = motor[2].JogSpeed + 10")
    f.write("motor[2].JogSpeed = motor[2].JogSpeed + 10"+'\n')

def zMSpeedChange(client):
    client.channel.send_line("motor[2].JogSpeed = motor[2].JogSpeed - 10")
    f.write("motor[2].JogSpeed = motor[2].JogSpeed - 10"+'\n')

def mixerSpeedChange(client):
    client.channel.send_line("motor[6].JogSpeed = motor[6].JogSpeed + 10")
    print("Mixer Speed Increased by 10")
    #client.channel.send_line("motor[6].JogSpeed = 350")
    #f.write("motor[6].JogSpeed = 350"+'\n')
def mixerMSpeedChange(client):
    client.channel.send_line("motor[6].JogSpeed = motor[6].JogSpeed - 10")
    print("Mixer Speed Decreased by 10")
    #client.channel.send_line("motor[6].JogSpeed = 80")
    #f.write("motor[6].JogSpeed = 80"+'\n')
def alphaSpeedChange(client):
    client.channel.send_line("motor[7].JogSpeed = motor[7].JogSpeed + 10")
    f.write("motor[7].JogSpeed = motor[7].JogSpeed + 10"+'\n')
    #print(client.channel.get_variable('#Motor[7].JogSpeed', type_=float))

def alphaMSpeedChange(client):
    client.channel.send_line("motor[7].JogSpeed = motor[7].JogSpeed - 10")
    f.write("motor[7].JogSpeed = motor[7].JogSpeed - 10" + '\n')

    #print(client.channel.get_variable('Motor[7].JogSpeed', type_=float))

def SystemOn(client, systemButton, wetButton, pumpButton,doserButton, onPic, offPic, sysState,
             wetState, pumpState, doserState):
    if (sysState.bState):
        client.channel.send_line("sys=1")
        f.write("sys=1" + '\n')
        systemButton['image'] = onPic
        wetButton['state'] = 'normal'
        pumpButton['state'] = 'normal'
        doserButton['state']='normal'
        sysState.bState = False
    else:
        client.channel.send_line("sys=0")  #system
        sleep(0.05)  # Time in seconds.
        client.channel.send_line("pump=0")  #pump
        sleep(0.05)  # Time in seconds.
        client.channel.send_line("wet=0")  #wet
        sleep(0.05)  # Time in seconds.
        client.channel.send_line("doser=0")  # wet
        f.write("sys=0"+ '\n')
        f.write("wet=0"+ '\n')
        f.write("pump=0"+ '\n')
        f.write("doser=0" + '\n')
        systemButton['image'] = offPic
        wetButton['image'] = offPic
        pumpButton['image'] = offPic
        doserButton['image'] = offPic
        wetButton.config(state=DISABLED)
        pumpButton.config(state=DISABLED)
        doserButton.config(state=DISABLED)
        sysState.bState = True
        wetState.bState = True
        pumpState.bState = True
        doserState.bState = True

def WetOn(client, wetButton, onPic, offPic, wetState):
    if (wetState.bState):
        client.channel.send_line("wet=1")
        f.write("wet=1"+'\n')
        wetButton['image']=onPic
        wetState.bState=False
    else:
        client.channel.send_line("wet=0")
        f.write("wet=0"+'\n')
        wetButton['image'] = offPic
        wetState.bState = True

def doserOn(client, doserButton, onPic, offPic, doserState):
    if (doserState.bState):
        client.channel.send_line("admixture=1")
        f.write("doser=1"+'\n')
        doserButton['image']=onPic
        doserState.bState=False
    else:
        client.channel.send_line("admixture=0")
        f.write("doser=0"+'\n')
        doserButton['image'] = offPic
        doserState.bState = True

def mixerOn(client, mixerButton, onPic, offPic, mixerState):
    if (mixerState.bState):
        client.channel.send_line("#6 j+")
        f.write("mixer=1"+'\n')
        mixerButton['image']=onPic
        mixerState.bState=False
    else:
        client.channel.send_line("#6 j/")
        f.write("mixer=0"+'\n')
        mixerButton['image'] = offPic
        mixerState.bState = True

def PumpOn(client, pumpButton, onPic, offPic, pumpState):
    if (pumpState.bState):
        client.channel.send_line("pump=1")
        f.write("pump=1"+'\n')
        pumpButton['image']=onPic
        pumpState.bState=False
    else:
        client.channel.send_line("pump=0")
        f.write("pump=0"+'\n')
        pumpButton['image'] = offPic
        pumpState.bState = True


def emergencyStop(client, systemButton, wetButton, pumpButton,doserButton, offPic,
                  sysState, wetState,pumpState,doserState, mixerButton, mixerOffPic, mixerState):
    client.channel.send_line("#dkill")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("#8 kill")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("#6 kill")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("#2 kill")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("#1 kill")
    sleep(0.01)  # Time in seconds.
    client.channel.send_line("#4 kill")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("#7 kill")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("sys = 0")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("wet = 0")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("pump = 0")
    sleep(0.05)  # Time in seconds.
    client.channel.send_line("doser = 0")

    f.write("sys=0"+'\n')
    f.write("wet=0"+'\n')
    f.write("pump=0"+'\n')
    f.write("doser=0" + '\n')
    f.write("mixer=OFF"+'\n')
    f.write("#dkill"+'\n')
    systemButton['image'] = offPic
    wetButton['image'] = offPic
    pumpButton['image'] = offPic
    mixerButton['image'] = mixerOffPic
    doserButton['image']=offPic
    #systemButton.config(state=DISABLED) #commented out this line to be able to run again without closing the GUI
    wetButton.config(state=DISABLED)
    pumpButton.config(state=DISABLED)
    doserButton.config(state=DISABLED)
    sysState.bState = True
    wetState.bState = True
    pumpState.bState = True
    mixerState.bState = True
    doserState.bState=True
# keep track of widgets for event handlers
widget_track = {}

#==================================================================
def main():

    sysState = buttonBools(True)
    wetState = buttonBools(True)
    pumpState = buttonBools(True)
    mixerState = buttonBools(True)
    doserState = buttonBools(True)
    # Server Connection
    ccClient = ccSSH('192.168.0.200', 22, 'root', 'deltatau')
    #ccClient="FAKE"
    # =============================================================
    sysState = buttonBools(True)

    root = Tk()
    root.geometry('1280x800+300+100')
    root.iconbitmap(default='transparent.ico')
    bck = ImageTk.PhotoImage(file="images/bck.jpg")
    background = ttk.Label(root, text="CC Control System", image=bck).place(relx=0, rely=0)
    actImg = ImageTk.PhotoImage(file="images/activate.png")
    activateBut = ttk.Button(root, text="Activate",image=actImg,
                             command=lambda: activateMotors(ccClient)).place(relx=0.044, rely=0.05)

    #exp1 = ttk.Button(root, text="EXP-1", command=lambda: raiseZ(ccClient, 1)).

    # z1 = ttk.Button(root, text="1", command=lambda: raiseZ(ccClient, 1)).place(relx=0.65, rely=0.3)
    # z2 = ttk.Button(root, text="2", command=lambda: raiseZ(ccClient, 2)).place(relx=0.65, rely=0.34)
    # z3 = ttk.Button(root, text="3", command=lambda: raiseZ(ccClient, 3)).place(relx=0.65, rely=0.38)
    # z4 = ttk.Button(root, text="4", command=lambda: raiseZ(ccClient, 4)).place(relx=0.65, rely=0.42)
    # z5 = ttk.Button(root, text="5", command=lambda: raiseZ(ccClient, 5)).place(relx=0.65, rely=0.46)
    #
    # z11 = ttk.Button(root, text="-1", command=lambda: raiseZ(ccClient, -1)).place(relx=0.73, rely=0.3)
    # z12 = ttk.Button(root, text="-2", command=lambda: raiseZ(ccClient, -2)).place(relx=0.73, rely=0.34)
    # z13 = ttk.Button(root, text="-3", command=lambda: raiseZ(ccClient, -3)).place(relx=0.73, rely=0.38)
    # z14 = ttk.Button(root, text="-4", command=lambda: raiseZ(ccClient, -4)).place(relx=0.73, rely=0.42)
    # z15 = ttk.Button(root, text="-5", command=lambda: raiseZ(ccClient, -5)).place(relx=0.73, rely=0.46)
    bHomeX = ttk.Button(root, text="Home X", command=lambda: plcRun(ccClient, "homingx")).place(relx=0.05, rely=0.3)
    bHomeY = ttk.Button(root, text="Home Y", command=lambda: plcRun(ccClient, "homingy")).place(relx=0.05, rely=0.35)
    bHomeZ = ttk.Button(root, text="Home Z", command=lambda: plcRun(ccClient, "homingz")).place(relx=0.05, rely=0.4)
    #buttonStaple= ttk.Button(root, text="Staple", command=lambda: plcRun(ccClient,"staple")).place(relx=0.05, rely=0.65)
    buttonProg7 = ttk.Button(root, text="Prog7", command=lambda: progRunner(ccClient,"7")).place(relx=0.05, rely=0.15)
    #buttonProg12 = ttk.Button(root, text="Prog12", command=lambda: progRunner(ccClient,"12")).place(relx=0.05, rely=0.25)
    #buttonProg13 = ttk.Button(root, text="First", command=lambda: progRunner(ccClient,"13")).place(relx=0.05, rely=0.25)
    #buttonProg14 = ttk.Button(root, text="Go to Start", command=lambda: progRunner(ccClient,"14")).place(relx=0.05, rely=0.35)
    #buttonProg15 = ttk.Button(root, text="Next Layer", command=lambda: progRunner(ccClient,"15")).place(relx=0.05, rely=0.55)
    #buttonHome7 = ttk.Button(root, text="Home7", command=lambda: homeAlpha(ccClient)).place(relx=0.83, rely=0.9)

    #buttonzAdjust = ttk.Button(root, text="Adjust Z", command=lambda: zCheck.adjustHeight()).place(relx=0.2, rely=0.05)


    #buttonP10 = ttk.Button(root, text="P10",  command=lambda: plcRun(ccClient,"p10")).place(relx=0.05, rely=0.15)
    #buttonProg17 = ttk.Button(root, text="W/Prog17", command=lambda: progRunner(ccClient,"17")).place(relx=0.05, rely=0.20)
    #buttonProg18 = ttk.Button(root, text="Without/18", command=lambda: progRunner(ccClient, "18")).place(relx=0.05,rely=0.25)
    #buttonLong = ttk.Button(root, text="long", command=lambda: plcRun(ccClient, "long")).place(relx=0.05, rely=0.15)
    #buttonp10= ttk.Button(root, text="p10", command=lambda: plcRun(ccClient,"p10")).place(relx=0.05, rely=0.25)
    #buttonP16 = ttk.Button(root, text="P16", command=lambda: plcRun(ccClient, "p16")).place(relx=0.05, rely=0.35)
    #buttonP20 = ttk.Button(root, text="P20-NEXT", command=lambda: plcRun(ccClient,"p20")).place(relx=0.05, rely=0.35)
    # buttonP17 = ttk.Button(root, text="P17",  command=lambda: plcRun(ccClient,"p17")).place(relx=0.05, rely=0.45)
    # buttonP18 = ttk.Button(root, text="P18-GO", command=lambda: plcRun(ccClient,"p18")).place(relx=0.05, rely=0.55)
    # buttonProg9 = ttk.Button(root, text="Prog9", command=lambda: progRunner(ccClient,"9")).place(relx=0.05, rely=0.15)
    # buttonProg10 = ttk.Button(root, text="Prog10", command=lambda: progRunner(ccClient,"10")).place(relx=0.05, rely=0.25)
    # buttonProg11 = ttk.Button(root, text="Prog11", command=lambda: progRunner(ccClient,"11")).place(relx=0.05, rely=0.45)

    #buttonCutter = ttk.Button(root, text="Stapler", command=lambda: cutter(ccClient)).place(relx=0.05, rely=0.30)
    #
    # buttonLeftOn = ttk.Button(root, text="Left On",  command=lambda: nozzleLeftOn(ccClient)).place(relx=0.17, rely=0.55)
    # buttonLeftOff = ttk.Button(root, text="Left Off", command=lambda: nozzleLeftOff(ccClient)).place(relx=0.24, rely=0.55)
    # buttonRightOn = ttk.Button(root, text="Right On", command=lambda: nozzleRightOn(ccClient)).place(relx=0.17, rely=0.6)
    # buttonRightOff = ttk.Button(root, text="Right Off", command=lambda: nozzleRightOff(ccClient)).place(relx=0.24, rely=0.6)
    # buttonCenterOn = ttk.Button(root, text="Center On", command=lambda: nozzleCenterOn(ccClient)).place(relx=0.17, rely=0.65)
    # buttonCenterOff = ttk.Button(root, text="Center Off", command=lambda: nozzleCenterOff(ccClient)).place(relx=0.24, rely=0.65)
    # buttonValveOn = ttk.Button(root, text="Valve On", command=lambda: nozzleValveOn(ccClient)).place(relx=0.17, rely=0.7)
    # buttonValveOff = ttk.Button(root, text="Valve Off", command=lambda: nozzleValveOff(ccClient)).place(relx=0.24, rely=0.7)
    # buttonGoHome = ttk.Button(root, text="Back Home", command=lambda: plcRun(ccClient,"plc2")).place(relx=0.05, rely=0.15)
    # buttonGoStart = ttk.Button(root, text="Go Start", command=lambda: plcRun(ccClient,"plc3")).place(relx=0.05,rely=0.2)
    # buttonStartPrint = ttk.Button(root, text="Start Print with Z (5 times)", command=lambda: progRunner(ccClient,"5")).place(relx=0.025,
    #                                                                                                    rely=0.25)
    #
    # buttonStartPrint = ttk.Button(root, text="Start Print without Z (5 times)",
    #                               command=lambda: progRunner(ccClient, "6")).place(relx=0.017,
    #                                                                                     rely=0.3)



    image1 = ImageTk.PhotoImage(file="images/up.png")
    button1 = ttk.Button(root, text="Z+", image=image1, command=lambda: moveUp(ccClient)).place(relx=0.555, rely=0.3)
    image2 = ImageTk.PhotoImage(file="images/down.png")
    button2 = ttk.Button(root, text="Z-", image=image2, command=lambda: moveDown(ccClient)).place(relx=0.555, rely=0.6)
    image12 = ImageTk.PhotoImage(file="images/kill.png")
    button12 = ttk.Button(root, text="#2 kill", image=image12, command=lambda: kill2(ccClient))\
        .place(relx=0.555, rely=0.50)
    image1212 = ImageTk.PhotoImage(file="images/home.jpg")
    button1212 = ttk.Button(root, text="motor[2].Pos=0", image=image1212, command=lambda: zero2(ccClient))\
        .place(relx=0.555, rely=0.40)

    image3 = ImageTk.PhotoImage(file="images/mr.png")
    button3 = ttk.Button(root, text="A+", image=image3, command=lambda: mrotate(ccClient)).place(relx=0.7, rely=0.85)
    image4 = ImageTk.PhotoImage(file="images/pr.png")
    button4 = ttk.Button(root, text="A-", image=image4, command=lambda: protate(ccClient)).place(relx=0.75, rely=0.85)

    image3434 = ImageTk.PhotoImage(file="images/home.jpg")
    button3434 = ttk.Button(root, text="motor[7].Pos=0", image=image1212, command=lambda: homeAlpha(ccClient)).place(relx=0.725, rely=0.9)

    image5 = ImageTk.PhotoImage(file="images/yp.png")
    button5 = ttk.Button(root, text="Y+", image=image5, command=lambda: py(ccClient)).place(relx=0.77, rely=0.63)
    image6 = ImageTk.PhotoImage(file="images/ym.png")
    button6 = ttk.Button(root, text="Y-", image=image6, command=lambda: my(ccClient)).place(relx=0.68, rely=0.66)

    image56 = ImageTk.PhotoImage(file="images/kill.png")
    button56 = ttk.Button(root, text="#8 j/", image=image56, command=lambda: stop8(ccClient)).place(
        relx=0.72, rely=0.58)

    image5656 = ImageTk.PhotoImage(file="images/home.jpg")
    button5656 = ttk.Button(root, text="motor[8].pos=0", image=image5656, command=lambda: zero8(ccClient)).place(
        relx=0.72, rely=0.50)

    image7 = ImageTk.PhotoImage(file="images/left.png")
    button7 = ttk.Button(root, text="X-", image=image7, command=lambda: mx(ccClient)).place(relx=0.5, rely=0.89)
    image8 = ImageTk.PhotoImage(file="images/right.png")
    button8 = ttk.Button(root, text="X+", image=image8, command=lambda: px(ccClient)).place(relx=0.612, rely=0.895)

    image78 = ImageTk.PhotoImage(file="images/kill.png")
    button78 = ttk.Button(root, text="#1 j/", image=image78, command=lambda: stop1(ccClient)).place(
        relx=0.555, rely=0.892)
    image1home = ImageTk.PhotoImage(file="images/home.jpg")
    button1home = ttk.Button(root, text="motor[1].pos=0", image=image5656, command=lambda: zero1and4(ccClient)).place(
        relx=0.45, rely=0.89)



    plus = ImageTk.PhotoImage(file="images/plus.png")
    minus = ImageTk.PhotoImage(file="images/minus.png")

    p1X = ttk.Button(root, text="Speed X+", image=plus, command=lambda: xSpeedChange(ccClient)).place(relx=0.42,
                                                                                                      rely=0.13)
    m1X = ttk.Button(root, text="Speed X-", image=minus, command=lambda: xMSpeedChange(ccClient)).place(relx=0.34,
                                                                                                        rely=0.13)

    p1Y = ttk.Button(root, text="Speed Y+", image=plus, command=lambda: ySpeedChange(ccClient)).place(relx=0.42,
                                                                                                      rely=0.28)
    m1Y = ttk.Button(root, text="Speed Y-", image=minus, command=lambda: yMSpeedChange(ccClient)).place(relx=0.34,
                                                                                                        rely=0.28)

    #p1Z = ttk.Button(root, text="Speed M+", image=plus, command=lambda: mixerSpeedChange(ccClient)).place(relx=0.42,rely=0.43)
    #m1Z = ttk.Button(root, text="Speed M-", image=minus, command=lambda: mixerMSpeedChange(ccClient)).place(relx=0.34,rely=0.43)

    p1alpha = ttk.Button(root, text="Speed Alpha+", image=plus, command=lambda: alphaSpeedChange(ccClient)).place(
        relx=0.42, rely=0.43)
    m1alpha = ttk.Button(root, text="Speed Alpha-", image=minus, command=lambda: alphaMSpeedChange(ccClient)).place(
        relx=0.34, rely=0.43)

    xSpeedText = ttk.Label(root, text="X Speed - Motor[1 & 4]").place(relx=0.35, rely=0.10)
    ySpeedText = ttk.Label(root, text="Y Speed - Motor[8]").place(relx=0.36, rely=0.25)
    #mixerSpeedText = ttk.Label(root, text="Mixer Speed - Motor[6]").place(relx=0.36, rely=0.40)
    alphaSpeedText = ttk.Label(root, text="Alpha Speed - Motor[7]").place(relx=0.35, rely=0.4)

    # ============================================================

    onPic = ImageTk.PhotoImage(file="images/onPic.jpg")
    offPic = ImageTk.PhotoImage(file="images/offPic.jpg")
    eStopPic = ImageTk.PhotoImage(file="images/eStop.png")
    eStopGreyPic = ImageTk.PhotoImage(file="images/eStopGrey.png")
    #mixerOnPic= ImageTk.PhotoImage(file="images/MIXER-ON.jpg")
    #mixerOffPic = ImageTk.PhotoImage(file="images/MIXER-OFF.jpg")
    #mixerButton = ttk.Button(root, text="mixer", image=mixerOffPic, command=lambda: mixerOn(ccClient, mixerButton, mixerOnPic, mixerOffPic, mixerState))
    #mixerButton.place(relx=0.1325, rely=0.55)

    systemText = ttk.Label(root, text="System").place(relx=0.157, rely=0.10)
    #wetText = ttk.Label(root, text="Water").place(relx=0.183, rely=0.40)
    wetButton = ttk.Button(root, state=DISABLED, text="wet", image=offPic,command=lambda: WetOn(ccClient, wetButton, onPic, offPic, wetState))

    #wetButton.place(relx=0.175, rely=0.43)
    pumpText = ttk.Label(root, text="Pump").place(relx=0.16, rely=0.25)
    pumpButton = ttk.Button(root, state=DISABLED, text="pump", image=offPic, command=lambda: PumpOn(ccClient, pumpButton, onPic, offPic, pumpState))
    pumpButton.place(relx=0.15, rely=0.28)

    doserText = ttk.Label(root, text="Admixture").place(relx=0.151, rely=0.40)
    doserButton = ttk.Button(root, state=DISABLED, text="Admixture", image=offPic, command=lambda: doserOn(ccClient, doserButton, onPic, offPic, doserState))
    doserButton.place(relx=0.15, rely=0.43)
    systemButton = ttk.Button(root, text="System", image=offPic,command=lambda: SystemOn(ccClient, systemButton, wetButton, pumpButton,doserButton, onPic, offPic, sysState, wetState, pumpState, doserState))
    systemButton.place(relx=0.15, rely=0.13)

    #emergencyButton = ttk.Button(root, text="Emergency Stop", image=eStopPic,command=lambda: emergencyStop(ccClient, systemButton, wetButton,pumpButton,doserButton, offPic, sysState, wetState,pumpState,doserState, mixerButton, mixerOffPic, mixerState))
    #emergencyButton.place(relx=0.1, rely=0.73)

    root.mainloop()  # While Loop for GUI Live Streaming
    f.close()

if __name__ == "__main__":
    main()