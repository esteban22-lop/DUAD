#Lists and iterables 

#Create a program that iterates and prints the values of two lists of the same size at the same time

first_list = ["Hello", "Esteban", "to be a great developer","but one day  will be easier","and that is the hard part"]
second_list = ["It's me", "I'm trying my best","I know this may be hard","we need to do it everyday","Just don't stop."]
#Get the length of one list
length = len(first_list)

#Then we iterate using indices. We can use "While" however we'll need to make some adjustments, and we do know the size of both list, so I think it's easier if we use "For"
for i in range (length):
    print(first_list[i], second_list[i])