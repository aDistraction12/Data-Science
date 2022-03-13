print("Name: Sumit Singh\nRoll No: 4354")
roll_no = ("1","2","3","4","5","6")

name = ("Sumit","Anjali","Himashree","Shri","Taral","Akshata")
Att = (())
DataS = (())

ReTry = True

print("\nStudent attendence :\n")
from typing import Tuple
import numpy as np
DataS = ((roll_no) , (name))
N = np.matrix(DataS)
print(N)
print(Att)
print("\n")
reEntry = input("Do you want add any new entries (Y/N):")
if reEntry.upper() == "N":
    pass
else :
    while(ReTry):
        print("\n\t\tInsert new data:")
        Name = input("Name :")
        Roll_no = input("Roll NO :")
        N =(str(Name),)
        R = (str(Roll_no),)
        roll_no += tuple(R)
        name += tuple(N)
        DataS = ((roll_no) , (name))
        N = np.matrix(DataS)
        print(N)
        z = input("Continue.. (Y/N)")

        if z.upper() == "Y":
            ReTry = True
        else:
            ReTry = False

for i in range(0,len(roll_no)):
    log = input(f"(A/P) roll no {roll_no[i]} : ")
    Att += ((roll_no[i],name[i],log.upper()),)
N = np.matrix(Att)
print("\n")
print(N) 
