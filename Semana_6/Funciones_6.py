#Funciones_6

def sort_hyphenated_string(input_string):
    words_list = input_string.split('-')
    words_list.sort()
    
    sorted_string = '-'.join(words_list)
    
    return sorted_string

input_str = "python-variable-function-computer-monitor"
result_string = sort_hyphenated_string(input_str)

print(f"Original string: {input_str}")
print(f"Sorted string: {result_string}")

