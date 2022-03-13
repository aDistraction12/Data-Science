print("Name: Sumit Singh\nRoll No:4354")
salary = {'Prasad': 23000, 'Sumit' : 34000, 'Sachin' : 20000, 'Sameer' : 90000}
print("\nDictionary available:", salary)

#for getting highest salary
print("\nEmployee having highest salary is:",max(salary, key= salary.get))

#for getting lowest salary
print("\nEmployee having lowest salary is:",min(salary, key= salary.get))

#for getting particular employee's salary
print(salary.get('Sumit'))
