print("Name: Sumit Singh\nRoll No:4354")
s0 = "computer"
s1 = "Hello this is data science practical"
s2 = "strings in python"
print(f"s0: {s0}\ns1: {s1}\ns2: {s2}")
      
#CONCATENATING --> adding two strings together
print("-----THIS IS CONCATENATION-----")
print(s1 + s2)
#this is simply concatenating
print(s1 + ',' + s2) #to make it look pretty

#ITERATING --> going through the string character by character
print("-------THIS IS ITERATING-------")
for i in s0:
    print(i)

#upper() --> it will turn string to uppercase
print("-------UPPERCASE	")
print(s0.upper())

#join() --> it will join the other string after each element while iterating
str1 = '->'
str2 = '1234'
print("-------JOINING-------")
print(str1.join(str2))
string = 'Hello'
print('' + '.'.join(string))

#split() --> it will split the string word by word
print("-------SPLITTING-------")
print(s1.split()) #this spilts word by word
print(s1.split(" ",2)) # this will split only first two words then take all other words in single inverted comma

#find() --> it will find the character or word you want and return the index
print("-------FINDING(returns index of the word you want)-------")
print(s1.find('data'))

print("-------REPLACING-------")
print(s1.replace('Hello','hey'))
