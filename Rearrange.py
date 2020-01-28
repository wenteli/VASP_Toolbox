#!/usr/bin/python3

# Author: Wente Li
# Modified date: v1.0 1/4/2019
# Purpose: Rearrange the POSCAR or CONTCAR file layer by layer


import numpy

LayerNum = 18;                 # Indicate number of layers
Layerdist = 1.18934417;       # Indicate distance between layers
Inipos = 5.00000000;           # Indicate the initial position of the first layer

File = open("CONTCAR.vasp")          # Should delete headers at first
Data = File.readlines()
data=numpy.loadtxt('CONTCAR.vasp')

Export = open("Rearrange.txt",'w')

for j in range (0,LayerNum+1):
    for i in range (0,len(data)):
        if data[i,2]>=Inipos+j*Layerdist-0.01 and data[i,2]<=Inipos+j*Layerdist+0.01:     # 0.001 is the distance tolerance range because the distance can't be very accurate 
           Export.write(Data[i]);

Export.close



