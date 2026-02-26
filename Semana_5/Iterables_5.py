#Iterables_5 

#Ask for 10 numbers and sort them.

numbers = []

for i in range(10):
    num = int(input(f"Enter number # {i + 1}: "))
    numbers.append(num)
    
print(f"Numbers entered: {numbers}")
print(f"The highest number was{max(numbers)}. ")
