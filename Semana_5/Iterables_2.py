#Iterables_2

#Create a program that iterates and prints a string in the other way around without reversed.

my_string = "This is a test"

lenght = len(my_string)

#I thought I could do it with only one "-1" but the print only deletes the last element, I did my research and found out that we need 3 of them because of the length of my list. 
for i in range(lenght -1, -1, -1):
    print(my_string[i])
    