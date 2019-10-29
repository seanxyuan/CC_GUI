import paramiko
from ppmac import pp_comm
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class ccSSH:
    def __init__(self, hostname, port, username, password):
        self.sshClient = paramiko.SSHClient()
        self.sshClient.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sshClient.load_system_host_keys()
        self.sshClient.connect(hostname, port, username, password, timeout=6000)
        print('PMAC Connection Successful ...')
        print('Write Commands:')
        self.comm = pp_comm.PPComm(host=hostname, port=port, user=username, password=password)
        self.channel = self.comm.shell_channel()
        self.channel.send_line('gpascii')
        # self.channel.send_line('\n')
    # def enterCommand(self,cmd):
    #     stdin, stdout, stderr = self.sshClient.exec_command(cmd)
    #     for line in stdout.readlines():
    #         print (line)


# =================================================================
# Robot Control Functions Defined for Buttons and Scale Bars:
class buttonBools:
    bState = True

    def __init__(self, bState):
        self.bState = bState


def protate(client):
    #client.channel.send_line("#7 j^81920")
    print("#7 j^81920")

def mrotate(client):
    #client.channel.send_line("#7 j^-81920")
    print("#7 j^-81920")

def py(client):
    #client.channel.send_line("#8 j^-346780")
    print("#8 j^-34678")

def my(client):
    #client.channel.send_line("#8 j^+346780")
    print("#8 j^+34678")

def moveUp(client):
    # client.channel.send_line("#2 $")
    #client.channel.send_line("#2 j^267445")
    print("#2 j^267445")

def moveDown(client):
    # client.channel.send_line("#2 $")
    #client.channel.send_line("#2 j^-267445")
    print("#2 j^-267445")

def px(client):
    # client.channel.send_line("#1 $")
    # client.channel.send_line("#1 j/")
    # client.channel.send_line("#4 $")
    # client.channel.send_line("#4 $j/")
    #client.channel.send_line("#1 j^434600")
    print("#1 j^434600")

def mx(client):
    # client.channel.send_line("#1 $")
    # client.channel.send_line("#1 j/")
    # client.channel.send_line("#4 $")
    # client.channel.send_line("#4 $j/")
    #client.channel.send_line("#1 j^-434600")
    print("#1 j^-434600")

def xSpeedChange(client):
    #client.channel.send_line("#motor[1].JogSpeed = motor[1].JogSpeed + 10")
    #client.channel.send_line("#motor[4].JogSpeed = motor[4].JogSpeed + 10")
    print("X Speed Increased by 10")

def xMSpeedChange(client):
    #client.channel.send_line("#motor[1].JogSpeed = motor[1].JogSpeed - 10")
    #client.channel.send_line("#motor[4].JogSpeed = motor[4].JogSpeed - 10")
    print("X Speed Decreased by 10")

def ySpeedChange(client):
    #client.channel.send_line("#motor[8].JogSpeed = motor[8].JogSpeed + 10")
    print("Y Speed Increased by 10")

def yMSpeedChange(client):
    #client.channel.send_line("#motor[8].JogSpeed = motor[8].JogSpeed - 10")
    print("Y Speed Decreased by 10")

def zSpeedChange(client):
    #client.channel.send_line("#motor[2].JogSpeed = motor[2].JogSpeed + 10")
    print("Z Speed Increased by 10")

def zMSpeedChange(client):
    #client.channel.send_line("#motor[2].JogSpeed = motor[2].JogSpeed - 10")
    print("Z Speed Decreased by 10")

def mixerSpeedChange(client):
    #client.channel.send_line("#motor[6].JogSpeed = motor[6].JogSpeed + 10")
    print("Mixer Speed Increased by 10")

def mixerMSpeedChange(client):
    #client.channel.send_line("#motor[6].JogSpeed = motor[6].JogSpeed - 10")
    print("Mixer Speed Decreased by 10")

def alphaSpeedChange(client):
    #client.channel.send_line("#motor[7].JogSpeed = motor[7].JogSpeed + 10")
    print("Alpha Speed Increased by 10")
    #print(client.channel.get_variable('motor[7].JogSpeed ', type_=int))

def alphaMSpeedChange(client):
    #client.channel.send_line("#motor[7].JogSpeed = motor[7].JogSpeed - 10")
    print("Alpha Speed Decreased by 10")
    #print(client.channel.get_variable('motor[7].JogSpeed ', type_=int))

def SystemOn(client, systemButton, wetButton, pumpButton, onPic, offPic, sysState,
             wetState, pumpState,emergencyButton,eStopPic):
    if (sysState.bState):
        #client.channel.send_line("PowerBrick[0].GpioData[0].17.1=1")
        print("sys=1")
        systemButton['image'] = onPic
        wetButton['state'] = 'normal'
        pumpButton['state'] = 'normal'
        emergencyButton['state'] = 'normal'
        emergencyButton['image'] = eStopPic
        sysState.bState = False
    else:
        #client.channel.send_line("PowerBrick[0].GpioData[0].17.1=0")
        #client.channel.send_line("PowerBrick[0].GpioData[0].18.1=0")
        #client.channel.send_line("PowerBrick[0].GpioData[0].19.1=0")
        print("sys=0")
        print("wet=0")
        print("pump=0")
        systemButton['image'] = offPic
        wetButton['image'] = offPic
        pumpButton['image'] = offPic
        wetButton.config(state=DISABLED)
        pumpButton.config(state=DISABLED)
        sysState.bState = True
        wetState.bState = True
        pumpState.bState = True


def WetOn(client, wetButton, onPic, offPic, wetState):
    if (wetState.bState):
       # client.channel.send_line("PowerBrick[0].GpioData[0].18.1=1")
        print("wet=1")
        wetButton['image'] = onPic
        wetState.bState = False
    else:
        #client.channel.send_line("PowerBrick[0].GpioData[0].18.1=0")
        print("wet=0")
        wetButton['image'] = offPic
        wetState.bState = True

def mixerOn(client, mixerButton, onPic, offPic, mixerState):
    if (mixerState.bState):
        #client.channel.send_line("#6 j+")
        print("mixer=1")
        mixerButton['image']=onPic
        mixerState.bState=False
    else:
        #client.channel.send_line("#6 kill")
        print("mixer=0")
        mixerButton['image'] = offPic
        mixerState.bState = True

def PumpOn(client, pumpButton, onPic, offPic, pumpState):
    if (pumpState.bState):
        #client.channel.send_line("PowerBrick[0].GpioData[0].19.1=1")
        print("pump=1")
        pumpButton['image'] = onPic
        pumpState.bState = False
    else:
        #client.channel.send_line("PowerBrick[0].GpioData[0].19.1 = 0")
        print("pump=0")
        pumpButton['image'] = offPic
        pumpState.bState = True


def emergencyStop(client, emergencyButton, systemButton, wetButton, pumpButton, offPic, eStopGreyPic, sysState, wetState,pumpState):
    #client.channel.send_line("PowerBrick[0].GpioData[0].17.1 = 0")
    #client.channel.send_line("PowerBrick[0].GpioData[0].18.1 = 0")
    #client.channel.send_line("PowerBrick[0].GpioData[0].19.1 = 0")
    #client.channel.send_line("dkill")
    print("sys=0")
    print("wet=0")
    print("pump=0")
    print("dkill")
    emergencyButton['image'] = eStopGreyPic
    systemButton['image'] = offPic
    wetButton['image'] = offPic
    pumpButton['image'] = offPic
    #systemButton.config(state=DISABLED) #commented out this line to be able to run again without closing the GUI
    wetButton.config(state=DISABLED)
    pumpButton.config(state=DISABLED)
    sysState.bState = True
    wetState.bState = True
    pumpState.bState = True
# ==================================================================
def main():
    sysState = buttonBools(True)
    wetState = buttonBools(True)
    pumpState = buttonBools(True)
    mixerState = buttonBools(True)
    # Server Connection
    #ccClient = ccSSH('192.168.0.200', 22, 'root', 'deltatau')
    ccClient="FAKE"
    # ccClient.channel.send_line('\n')
    # ccClient.channel.send_line('\n')
    # =============================================================
    sysState = buttonBools(True)

    root = Tk()
    root.geometry('1280x800+300+100')
    root.iconbitmap(default='transparent.ico')
    bck = ImageTk.PhotoImage(file="images/bck.jpg")
    background = ttk.Label(root, text="CC Control System", image=bck).place(relx=0, rely=0)
    image1 = ImageTk.PhotoImage(file="images/up.png")
    button1 = ttk.Button(root, text="M+", image=image1, command=lambda: moveUp(ccClient)).place(relx=0.555, rely=0.3)
    image2 = ImageTk.PhotoImage(file="images/down.png")
    button2 = ttk.Button(root, text="M-", image=image2, command=lambda: moveDown(ccClient)).place(relx=0.555, rely=0.6)
    image3 = ImageTk.PhotoImage(file="images/mr.png")
    button3 = ttk.Button(root, text="A+", image=image3, command=lambda: protate(ccClient)).place(relx=0.7, rely=0.85)
    image4 = ImageTk.PhotoImage(file="images/pr.png")
    button4 = ttk.Button(root, text="A-", image=image4, command=lambda: mrotate(ccClient)).place(relx=0.75, rely=0.85)
    image5 = ImageTk.PhotoImage(file="images/yp.png")
    button5 = ttk.Button(root, text="Y+", image=image5, command=lambda: py(ccClient)).place(relx=0.77, rely=0.63)
    image6 = ImageTk.PhotoImage(file="images/ym.png")
    button6 = ttk.Button(root, text="Y+", image=image6, command=lambda: my(ccClient)).place(relx=0.68, rely=0.66)
    image7 = ImageTk.PhotoImage(file="images/left.png")
    button7 = ttk.Button(root, text="X+", image=image7, command=lambda: px(ccClient)).place(relx=0.5, rely=0.89)
    image8 = ImageTk.PhotoImage(file="images/right.png")
    button8 = ttk.Button(root, text="X-", image=image8, command=lambda: mx(ccClient)).place(relx=0.91, rely=0.74)
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

    p1Z = ttk.Button(root, text="Speed M+", image=plus, command=lambda: mixerSpeedChange(ccClient)).place(relx=0.42,
                                                                                                          rely=0.43)
    m1Z = ttk.Button(root, text="Speed M-", image=minus, command=lambda: mixerMSpeedChange(ccClient)).place(relx=0.34,
                                                                                                            rely=0.43)

    p1alpha = ttk.Button(root, text="Speed Alpha+", image=plus, command=lambda: alphaSpeedChange(ccClient)).place(
        relx=0.42, rely=0.58)
    m1alpha = ttk.Button(root, text="Speed Alpha-", image=minus, command=lambda: alphaMSpeedChange(ccClient)).place(
        relx=0.34, rely=0.58)

    xSpeedText = ttk.Label(root, text="X Speed - Motor[1 & 4]").place(relx=0.35, rely=0.10)
    ySpeedText = ttk.Label(root, text="Y Speed - Motor[8]").place(relx=0.36, rely=0.25)
    mixerSpeedText = ttk.Label(root, text="Mixer Speed - Motor[6]").place(relx=0.36, rely=0.40)
    alphaSpeedText = ttk.Label(root, text="Alpha Speed - Motor[7]").place(relx=0.35, rely=0.55)

    # ============================================================

    onPic = ImageTk.PhotoImage(file="images/onPic.jpg")
    offPic = ImageTk.PhotoImage(file="images/offPic.jpg")
    eStopPic = ImageTk.PhotoImage(file="images/eStop.png")
    eStopGreyPic = ImageTk.PhotoImage(file="images/eStopGrey.png")
    mixerOnPic= ImageTk.PhotoImage(file="images/MIXER-ON.jpg")
    mixerOffPic = ImageTk.PhotoImage(file="images/MIXER-OFF.jpg")
    mixerButton = ttk.Button(root, text="mixer", image=mixerOffPic,
                           command=lambda: mixerOn(ccClient, mixerButton, mixerOnPic, mixerOffPic, mixerState))
    mixerButton.place(relx=0.1325, rely=0.55)
    systemText = ttk.Label(root, text="System").place(relx=0.157, rely=0.10)
    wetText = ttk.Label(root, text="Wetting Module").place(relx=0.14, rely=0.25)
    wetButton = ttk.Button(root, state=DISABLED, text="wet", image=offPic,
                           command=lambda: WetOn(ccClient, wetButton, onPic, offPic, wetState))
    wetButton.place(relx=0.15, rely=0.28)
    pumpText = ttk.Label(root, text="Pump").place(relx=0.158, rely=0.40)
    pumpButton = ttk.Button(root, state=DISABLED, text="pump", image=offPic,
                            command=lambda: PumpOn(ccClient, pumpButton, onPic, offPic, pumpState))
    pumpButton.place(relx=0.15, rely=0.43)
    systemButton = ttk.Button(root, text="System", image=offPic,
                              command=lambda: SystemOn(ccClient, systemButton, wetButton, pumpButton, onPic, offPic,
                                                       sysState, wetState, pumpState,emergencyButton, eStopPic))
    systemButton.place(relx=0.15, rely=0.13)

    emergencyButton = ttk.Button(root, text="Emergency Stop", image=eStopPic,
                                 command=lambda: emergencyStop(ccClient, emergencyButton, systemButton, wetButton,
                                                               pumpButton, offPic, eStopGreyPic, sysState, wetState,pumpState))
    emergencyButton.place(relx=0.1, rely=0.73)

    root.mainloop()  # While Loop for GUI Live Streaming

if __name__ == "__main__":
    main()