#Funciones_2

#Scope

def my_function():
    local_variable = "I'm local"
    
try:
    print(local_variable)
except NameError as e:
    print(f"Error: {e}") #This may print 'local_variable' is not defined
    
global_variable = 10


def change_global():
    global global_variable #With this line we declare the global variable, not local
    print(f"Global before change: {global_variable}")
    global_variable = 20
    print(f"Global after change: {global_variable}")
    

change_global()

print(f"Final value: {global_variable}")