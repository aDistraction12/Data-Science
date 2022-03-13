print("Name: Sumit Singh\nRoll No: 4354\n")
employee1 = set(["Sumit", "Rhea","Anjali","Shrirang"])
employee2 = set(["Taral", "Aayush","Shrirang"])
print(f"Employee Records:\n set1: {employee1}\n set2: {employee2}")

#add is use to add employee in set
employee2.add("Adi")
print(f"\nAdding an employee:\n{employee2}")
#discard is use to remove employee from set
employee1.discard("Rhea")
print(f"\nRemoving an employee:\n{employee1}")

print("\nIntersection of two said sets:")
Intersection = employee1 & employee2 # common name or employees in both set
print(Intersection)

print("\nUnion of two said sets:")
Union = employee1 | employee2
print(Union) #Union means all employees in both sets

difference = employee1-employee2
print("\n Difference in employee1 from employee2:")
print(difference)

#To check if a given set is a subset or superset of another set by comparing sets
print("\nCompare operation on sets of employees")
compare1 = employee1 >= employee2
compare2 = employee1 <= employee2

print("compare1 :",compare1)
print("compare2 :",compare2)

