#!/usr/bin/python3

# Author: Wente Li
# Modified date: v1.0 1/11/2019
# Purpose: To add the mirror symmetry part of the cell


Mirrorplane = 46.2

import numpy

File = open("CONTCAR.vasp")      # THe header should be deleted
Data = File.readlines()
data=numpy.loadtxt('CONTCAR.vasp')

Export = open("POSCAR",'w')



for i in range (0,len(data)):
    Export.write(Data[i][0:57]);
    #Export.write('\r')


for i in range (0,len(data)):
    Export.write(Data[i][0:44]);
    if abs(data[i,2]-Mirrorplane) > 0.001: 
       Export.write(str(2*Mirrorplane-data[i,2]));
    Export.write('\r\n')

Export.close



