#!/usr/bin/python3

# Author: Wente Li
# Modified date: v1.0 1/4/2019
# Purpose: To make the slab in the center of the simulation cell


ShiftDis = +13.5663      # Indicate the shift distance

import numpy

File = open("CONTCAR.vasp")      # THe header should be deleted
Data = File.readlines()
data=numpy.loadtxt('CONTCAR.vasp')

Export = open("Shift.txt",'w')



for i in range (0,len(data)):
    Export.write(Data[i][0:44]);
    Export.write('%.8f'%(data[i,2]+ShiftDis));
    Export.write('\r\n')

Export.close



