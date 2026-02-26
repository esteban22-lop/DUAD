#Iterables_3

#Create a program that change the first and last element of one list. Doesn't matter the size.
#It must work regardless of the list size

my_list = ["1","2","3","4","5","6"]

temp_change = my_list[0]
# I changed the 3 for -1, with the 3 worked before because of the lenght, however, if the list gets either bigger or shorter it won't wotk. 
# So, I implemented the minus one to start from the last element. Does not matter the size.
my_list[0] = my_list[-1]
my_list[-1] = temp_change

print(f"interchanged list: {my_list}")
