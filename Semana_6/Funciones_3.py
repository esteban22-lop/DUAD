#Funciones_3

def sum_list_numbers(numbers_list):
    total_sum = 0
    
    for number in numbers_list:
     total_sum += number #This will add the current number to the total
    return total_sum


my_list = [10,20,30,40,50]
result = sum_list_numbers(my_list)

print(f"The list is: {my_list}")
print(f"The sum of all number is: {result}")