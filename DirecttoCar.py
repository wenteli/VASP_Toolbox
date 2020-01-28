#!/usr/bin/python3

# Author: Wente Li
# Modified date: v1.0 1/4/2019
# Purpose: Direct coor to Cartesian coor.


LCZ = 86.0871300000000000       
LCX = 3.952
LCY = 3.952

import numpy

File = open("CONTCAR")      # THe header should be deleted
Data = File.readlines()
data=numpy.loadtxt('CONTCAR')

Export = open("Shift.txt",'w')



for i in range (0,len(data)):
    Export.write('%.8f'%(data[i,0]*LCX));
    Export.write('    ');
    Export.write('%.8f'%(data[i,1]*LCY));
    Export.write('    ');
    Export.write('%.8f'%(data[i,2]*LCZ));
    Export.write('\r\n')

Export.close



