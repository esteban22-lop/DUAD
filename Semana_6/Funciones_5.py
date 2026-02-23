#Funciones_5

def count_upper_lower(input_string):
    upper_count = 0 
    lower_count = 0 
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"There is {upper_count} upper cases and {lower_count} lower cases")
    


test_string = "I love Nation Sushi too. Also, I love Ramen."
count_upper_lower(test_string)
