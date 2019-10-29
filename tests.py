
def plcRun(plcName):
    plcCMD = "#1 #8 #7 J/ &1 B" + plcName +" r"
    print(plcCMD)

plcRun ("1")