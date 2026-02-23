#Funciones_4

def reverse_string(s):
    reversed_iterator = reversed(s)
    reversed_s = "".join(reversed_iterator)
    return reversed_s

input_string = "Hello World"
output_string = reverse_string(input_string)
print(f"original: {input_string}")
print(f"Reversed: {output_string}")

