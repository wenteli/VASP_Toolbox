#!/usr/bin/env python
# coding: utf-8
# Author: Wente Li
# Modified date: v2.1 04/30/2019
# Update: can use an external txt file to type in atom index, no need tp type in each one by hand :-)
# Purpose: Used to read DOS data of each atom, calculate the PDOS of each plane and combine them into one file. 

# In[6]:
import numpy


print("Please typye in the total number of atoms in the simulation cell!");
TotalNum = int(input());

data = [[]];
for i in range (0,TotalNum):
    data.append([]);

print("Please typye in the total number of planes you want to calculate!");
PlaneNum = int(input());

#index file has to have the same number of column, if less, use zero to compensate
atomindex=numpy.loadtxt("index.txt");
for loop1 in range (0,PlaneNum):
    print("Reading the index of each atom in current plane # %s" %(loop1+1));
    for loop2 in range (0,len(atomindex[loop1])):
        index=int(atomindex[loop1][loop2]);
        if index != 0:
           data[index]=numpy.loadtxt('%s.txt' %(index))
    if loop1 == PlaneNum-1:
        print("Job done! Congratulations :-)")
    else:
        print("End current plane. Please continue to next plane.");



print("Please indicate ISPIN!");
ISPIN = int(input());

print("Please indicate the maximum orbitals!");
Orbitals = input();
if Orbitals == 's':                   # Determine how many orbitals in totat, including total DOS (sum of all orbitals) 
   orbitals = 2*ISPIN;
elif Orbitals == 'p':
   orbitals = 5*ISPIN;
elif Orbitals == 'd':
   orbitals = 10*ISPIN;
elif Orbitals == 'f':
   orbitals = 17*ISPIN;
else:
   print('Please check orbitals!')


def DOSsum(planeindex,orbital,index,energy):                   # Sum the values in even positions of a list
    total = 0
    for i in range (0,len(index[planeindex])):
        if int(index[planeindex][i]) != 0:
           total = total+data[int(index[planeindex][i])][energy][orbital+1];
    return total;



# In[7]:
for loop1 in range (0,PlaneNum):
    Export = open("Plane#%s.txt" %(loop1+1),'w')
    for loop2 in range (0,len(data[int(atomindex[0][0])])):                        #loop2 indicates energy
        Export.write('%.8f'%(data[int(atomindex[0][0])][loop2][0]))                #First column is energy
        Export.write('\t')
        for loop3 in range (0,orbitals):
            Export.write('%.8f'%(DOSsum(loop1,loop3,atomindex,loop2)));
            Export.write('\t')
        Export.write('\r\n')

    Export.close
