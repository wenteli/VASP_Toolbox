#! /usr/bin/python3

# Used to plot plane projected DOS vs energy
# Follow the output files from Drawv2.0.py

import numpy
import matplotlib.pyplot as plt

print("Please typye in the total number of planes you want to calculate!");
PlaneNum = int(input());
print("Please typye in the index of each plane (seperate by space)!");
PlaneIndex = [];
for i in range(0,PlaneNum):
    PlaneIndex.append(int(input()));


data=[];
for loop1 in range (0,PlaneNum):
    data.append(numpy.loadtxt('Plane#%s.txt' %(PlaneIndex[loop1])));

print("Please indicate ISPIN.");
ISPIN=int(input());
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


print("Please type in lowest energy limit");
energylow = int(input());
print("Please type in highest energy limit");
energyhigh = int(input());


print("Please indicate the number of orbitals you want to plot.");
orbnum=int(input());
print("Please type in the orbits.\n1-s; 2-p; 3-d; 4-f.\nPlease notethat total DOS will always be included.");
orbital=[]
for loop1 in range(0,orbnum):
    orbital.append(int(input()));




if ISPIN == 1:
   fig = plt.figure();

   for loop1 in range(0,PlaneNum):
       plt.subplot(1,PlaneNum,loop1+1);
       for loop2 in range (0,orbnum):
           if orbital[loop2]==1:
              plt.plot(data[loop1][energylow:energyhigh,orbital[loop2]],data[loop1][energylow:energyhigh,0],lw=1.5);
           elif orbital[loop2]==2:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]]+data[loop1][energylow:energyhigh,orbital[loop2]+1]+data[loop1][energylow:energyhigh,orbital[loop2]+2]),data[loop1][energylow:energyhigh,0],lw=1.5);
           elif orbital[loop2]==3:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+2]+data[loop1][energylow:energyhigh,orbital[loop2]+3]+data[loop1][energylow:energyhigh,orbital[loop2]+4]+data[loop1][energylow:energyhigh,orbital[loop2]+5]+data[loop1][energylow:energyhigh,orbital[loop2]+6]),data[loop1][energylow:energyhigh,0],lw=1.5);
           else:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+6]+data[loop1][energylow:energyhigh,orbital[loop2]+7]+data[loop1][energylow:energyhigh,orbital[loop2]+8]+data[loop1][energylow:energyhigh,orbital[loop2]+9]+data[loop1][energylow:energyhigh,orbital[loop2]+10]+data[loop1][energylow:energyhigh,orbital[loop2]+11]+data[loop1][energylow:energyhigh,orbital[loop2]+12]),data[loop1][energylow:energyhigh,0],lw=1.5);

       plt.plot(data[loop1][energylow:energyhigh,orbitals+1],data[loop1][energylow:energyhigh,0],color='black',lw=2);   # total DOS
       plt.xlim(0,3);                      # Range of intensity of DOS
       plt.yticks([-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5]);        # Range of energy
       plt.xticks([]);

   plt.subplots_adjust(wspace=0);
   plt.show(fig)



else:
   # Plot spin up channel
   figup = plt.figure();
   for loop1 in range(0,PlaneNum):
       plt.subplot(1,PlaneNum,loop1+1);
       for loop2 in range (0,orbnum):
           if orbital[loop2]==1:
              plt.plot(data[loop1][energylow:energyhigh,orbital[loop2]],data[loop1][energylow:energyhigh,0],lw=2,label='s');
              plt.legend();
           elif orbital[loop2]==2:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+1]+data[loop1][energylow:energyhigh,orbital[loop2]+3]+data[loop1][energylow:energyhigh,orbital[loop2]+5]),data[loop1][energylow:energyhigh,0],lw=2,label='p');
              plt.legend();
           elif orbital[loop2]==3:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+6]+data[loop1][energylow:energyhigh,orbital[loop2]+8]+data[loop1][energylow:energyhigh,orbital[loop2]+10]+data[loop1][energylow:energyhigh,orbital[loop2]+12]+data[loop1][energylow:energyhigh,orbital[loop2]+14]),data[loop1][energylow:energyhigh,0],lw=2,label='d');
              plt.legend();
           else:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+15]+data[loop1][energylow:energyhigh,orbital[loop2]+17]+data[loop1][energylow:energyhigh,orbital[loop2]+19]+data[loop1][energylow:energyhigh,orbital[loop2]+21]+data[loop1][energylow:energyhigh,orbital[loop2]+23]+data[loop1][energylow:energyhigh,orbital[loop2]+25]+data[loop1][energylow:energyhigh,orbital[loop2]+27]),data[loop1][energylow:energyhigh,0],lw=2,label='f');
              plt.legend();

       plt.plot(data[loop1][energylow:energyhigh,orbitals+1],data[loop1][energylow:energyhigh,0],color='black',lw=3);   # total DOS
       plt.fill(data[loop1][energylow:energyhigh,orbitals+1],data[loop1][energylow:energyhigh,0],color='black',alpha=0.3);
       plt.xlim(0,1);                      # Range of intensity of DOS
       if loop1==0:
          plt.yticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3]);
       else:
          plt.yticks([]);    
       plt.ylim(-1.5,1); 
       plt.xticks([]);
       #plt.xlabel('spin up');
       plt.hlines(0,0,5,colors='b',linestyles='dashed');

   plt.subplots_adjust(wspace=0);
   plt.show(figup)


   # Plot spin down channel
   figdown = plt.figure();
   for loop1 in range(0,PlaneNum):
       plt.subplot(1,PlaneNum,loop1+1);
       for loop2 in range (0,orbnum):
           if orbital[loop2]==1:
              plt.plot(data[loop1][energylow:energyhigh,orbital[loop2]+1],data[loop1][energylow:energyhigh,0],lw=2,label='s');
              plt.legend();
           elif orbital[loop2]==2:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+2]+data[loop1][energylow:energyhigh,orbital[loop2]+4]+data[loop1][energylow:energyhigh,orbital[loop2]+6]),data[loop1][energylow:energyhigh,0],lw=2,label='p');
              plt.legend();
           elif orbital[loop2]==3:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+7]+data[loop1][energylow:energyhigh,orbital[loop2]+9]+data[loop1][energylow:energyhigh,orbital[loop2]+11]+data[loop1][energylow:energyhigh,orbital[loop2]+13]+data[loop1][energylow:energyhigh,orbital[loop2]+15]),data[loop1][energylow:energyhigh,0],lw=2,label='d');
              plt.legend();
           else:
              plt.plot((data[loop1][energylow:energyhigh,orbital[loop2]+16]+data[loop1][energylow:energyhigh,orbital[loop2]+18]+data[loop1][energylow:energyhigh,orbital[loop2]+20]+data[loop1][energylow:energyhigh,orbital[loop2]+22]+data[loop1][energylow:energyhigh,orbital[loop2]+24]+data[loop1][energylow:energyhigh,orbital[loop2]+26]+data[loop1][energylow:energyhigh,orbital[loop2]+28]),data[loop1][energylow:energyhigh,0],lw=2,label='f');
              plt.legend();

       plt.plot(data[loop1][energylow:energyhigh,orbitals+2],data[loop1][energylow:energyhigh,0],color='red',lw=3);   # total DOS
       plt.fill(data[loop1][energylow:energyhigh,orbitals+2],data[loop1][energylow:energyhigh,0],color='red',alpha=0.3);
       plt.xlim(0,-1);                      # Range of intensity of DOS
       if loop1==0:
          plt.yticks([-3,-2.5,-2,-1.5,-1,-0.5,0,0.5,1,1.5,2,2.5,3]);
       else:
          plt.yticks([]);    
       plt.ylim(-1.5,1); 
       plt.xticks([]);
       #plt.xlabel('spin down');
       plt.hlines(0,0,-5,colors='b',linestyles='dashed');

   plt.subplots_adjust(wspace=0);
   plt.show(figdown)
