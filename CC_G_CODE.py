"""
    // Power PMAC PROGRAM Template.
// The following Sample PROGRAM is the standard template for creating Motion Programs.
// Sample PROGRAM
/****************************************/
undefine all
&1
#7->1000x
#8->1000y

open prog 3
// --------------------User Code Goes Here------------------------
linear

abs

ta 125
ts 35
tm 1000

dwell 0 Gather.Enable = 2 dwell 0

x 0 y 0
dwell 2000
x 0 y 50
dwell 2000
x 50 y 50
dwell 100
Gather.Enable = 0 dwell 0
close
/****************************************/


"""


def addLayers(layerFile,numberOfLayers):
    fileName = layerFile+".txt"
    layer = open(fileName, 'r')
    layers=[]

