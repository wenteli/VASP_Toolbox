#! /usr/bin/python3


# Author: Wente Li
# Modified date: v1.0 1/4/2019
# Purpose: Average potential calculation.
# Reference: Chapter 2 of Theoretical study of HfO2 as a gate material for CMOS devices, phd thesis by Onise Sharia


# For supercell with several differnet compositions 

def Integrate(x, Boundry, j, Num):
    result = 0;
    if j == Num-1:
       for i in range (int(x-Boundry[j]/2),int(x+Boundry[j]/2)):
           if i > 0 and i < Grid:
              result = result+float(V[i][8:26])*1.0;
    else:
       for i in range (int(x-Boundry[j]/2),int(x+Boundry[j]/2)):
           if i > 0 and i < Grid:
              result = result+Integrate(i, Boundry, j+1, Num);
    return result;


from functools import reduce

File = open("VLINE.txt");    # The origin file is from the Fortran code
V = File.readlines();

print('Please indicate how mant compositions we have!');
NumC = int(input());
LC = [0]*NumC;               # LC = Lattice Constant
Boundry = [0]*NumC;          # Integration boundry


print('Please type in the total length of the simulation cell!');
TotalLen = float(input());

Grid = int(V[0][8:12]);
Interval = TotalLen/Grid;


print('Please type in the lattice constant of each composition!');
for i in range (0,NumC):
    LC[i] = float(input());
    Boundry[i] = LC[i]/Interval;


Ave = [0];
for z in range (1,1+Grid):
    jj = 0;
    Results = Integrate(z,Boundry, jj, NumC);                            # Recursion process
    Ave.append(Results/(reduce((lambda x, y: x * y), Boundry)));


Export = open("AvePOT.txt",'w');         
for i in range (1,1+Grid):
    Export.write(str(i));
    Export.write('	');
    Export.write('%.8f'%(Ave[i]));
    Export.write('\r\n');
Export.close;
