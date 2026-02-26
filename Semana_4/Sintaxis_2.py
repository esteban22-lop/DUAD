#Sintaxis 2

#Ask for name, last name, age. Show life stages

name = input("Please, add your name: ")
last_name = input("Last name: ")
age = int(input("age: "))

if age < 3:
    stages = "Baby"
elif age >= 3 and age <= 9:
    stages = "Child" 
elif age >= 10 and age <= 12:
    stages = "Pre-Adolescence"
elif age >= 13 and age <= 17:
    stages = "Adolescence"
elif age >= 18 and age <= 25:
    stages = "Young adult"
elif age >=26 and age <= 59:
    stages = "Adult"
else:
    stages = "Senior citizen"
    
print(f"{name} {last_name}, you are {stages}.")