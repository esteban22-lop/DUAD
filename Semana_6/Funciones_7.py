#Funciones_7

def is_prime(number):
    
    if number <= 1:
        return False
    
    for i in range (2, int(number*0.5) + 1):
        if (number % i) == 0:
            return False
        
    return True


def filter_primes_from_list(numbers_list):
    prime_numbers = []
    
    for num in numbers_list:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


input_list = [1, 4, 6, 7, 13, 9, 67]
result_list = filter_primes_from_list(input_list)

print(f"Original list: {input_list}")
print(f"Prime numbers list: {result_list}")