#!/usr/bin/python3

# Author: Wente Li
# Modified date: v1.1 7/1/2020
# Purpose: To make the slab in the center of the simulation cell


ShiftDis = 20      # Indicate the shift distance

import numpy

File = open("QW.vasp")      # THe header should be deleted
Data = File.readlines()
data=numpy.loadtxt('QW.vasp')

Export = open("Shift.txt",'w')



for i in range (0,len(data)):
    Export.write(Data[i][0:43]);
    Export.write('%.8f'%(data[i,2]+ShiftDis));
    Export.write('\r\n')

Export.close



