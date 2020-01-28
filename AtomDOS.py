#! /usr/bin/python3


# Author: Wente Li
# Modified date: v1.0 1/4/2019
# Purpose: Atom projected DOS data collection



import os

DOSFile = open("DOSCAR");
DOSData = DOSFile.readlines();
os.mkdir('/home/wente/Desktop/PDOS')    # All output file is instored in PDOS directory.


def evensum(numbers):                   # Sum the values in even positions of a list
    total = 0
    for i in range (0,len(numbers)):
        if i % 2 == 0:
            total += numbers[i]
    return total;

def oddsum(numbers):                    # Sum the values in odd positions of a list
    total = 0
    for i in range (0,len(numbers)):
        if i % 2 == 1:
            total += numbers[i]
    return total;



# Basic parameters reading
NEDOS = int(DOSData[5][32:37]);        # Total number of data points for DOS
Fermi = float(DOSData[5][42:53]);      # Fermi energy
print("Please check the Fermi Energy (read by AtomDOS.py) carefully and indicate T or F for true and false! Fermi Energy = ", Fermi, '\r\n');
judge = input();
if judge == 'F':
    print("Fermi Energy is wrong. Maybe AtomDOS.py read Fermi energy wrong. Check the source code.")
    exit();


print("Please typye in the total number of atoms in the simulation cell!");
TotalNum = int(input());

print("Please indicate ISPIN!");
ISPIN = int(input());

print("Please indicate the maximum orbitals!");
Orbitals = input();
if Orbitals == 's':                   # Determine how many orbitals in total    
   orbitals = 1*ISPIN;
elif Orbitals == 'p':
   orbitals = 4*ISPIN;
elif Orbitals == 'd':
   orbitals = 9*ISPIN;
elif Orbitals == 'f':
   orbitals = 16*ISPIN;
else:
   print('Please check orbitals!')

Orbital = [0]*orbitals;               # List to store the DOS data of each orbital



for k in range (1,1+TotalNum):        # k means the k th atom we focus on (outer loop)
    Export = open('PDOS/%s.txt' % (k),'w');
    #if ISPIN == 2:
     #  Export.write('Energy	sup	sdown	p1up	p1down	p2up	p2down	 p3up	p3down	d1up	d1down	d2up	d2down	d3up	d3down	d4up	d4down	d5up	d5down	f1up	f1down	f2up	f2down	f3up	f3down	f4up	f4down	f5up	f5down	f6up	f6down	f7up	f7down	DOSup	DOSdown\r\n');
    #else:
     #  Export.write('Energy	s	p1	p2	p3	d1	d2	d3	d4	d5	f1	f2	f3	f4	f5	DOS\r\n');

    for i in range (1,1+NEDOS):         # i for inner loop (how many data points for DOS). Read the DOS value of a specific orbital with respect to a specific energy 
        line = (NEDOS+6)+(NEDOS+1)*(k-1)+i; 
        Export.write('%.8f'%(float(DOSData[i+5][4:11])-float(Fermi)));  Export.write('	');
        j = 0;
        while j < orbitals:
            if ISPIN == 1:
               Orbital[j] = float(DOSData[line][12*j+13:12*j+23]);
               Export.write('%.8f'%(Orbital[j]));   Export.write('	');
            else:
               if j % 2 == 0:
                  Orbital[j] = float(DOSData[line][12*j+13:12*j+23]);
                  Export.write('%.8f'%(Orbital[j]));   Export.write('	');
               else:
                  Orbital[j] = -float(DOSData[line][12*j+13:12*j+23]);
                  Export.write('%.8f'%(Orbital[j]));   Export.write('	');
            j = j+1;
        if ISPIN == 1:
            Export.write('%.8f'%(sum(Orbital)));   Export.write('\r\n');
        else:
            Export.write('%.8f'%(evensum(Orbital)));   Export.write('	');  Export.write('%.8f'%(oddsum(Orbital)));   Export.write('\r\n');


    Export.close
