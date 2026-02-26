#Calculadora

#First of all I'll create functions in order to help me with the math operations

def suma (a, b):
    return a + b


def difference (a, b):
    return a - b


def multiplication (a, b):
    return a * b


def division (a, b):
    return a / b



def calculator():
    current_number = 0 #We need to start with an initial number and that will be 0
    
    while True:
        print(f"Current number: {current_number}")
        print("1. Sum")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Divison")
        print("5. Clear result")
        print("6. Exit")
        
        option = input("Please, choose your option from 1-6: ")
        
        if option in ('1','2','3','4'):
            try:
                new_number = float(input("Enter a number: "))
                
            except ValueError:
                print("Invalid number")
                continue
            
            if option == '1':
                current_number = suma(current_number, new_number)
            elif option == '2':
                current_number = difference(current_number, new_number)
            elif option == '3':
                current_number = multiplication(current_number, new_number)
            elif option == '4':
                if new_number == 0:
                    print("Cannont divide by zero")
                    continue
                current_number = division(current_number, new_number)
                
        elif option == '5':
            current_number = 0
            print("Result cleared.")
            
        elif option == '6':
            print("Exit from calculator")
            break
        else:
            print("Please enter a valid option.")
            

if __name__=="__main__":
    calculator()
    
