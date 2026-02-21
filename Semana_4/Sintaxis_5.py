#Sintaxis 5

#Calculate average

n = int(input("Enter the number of grades to calculate the average: "))

total_sum = 0.0
approved_sum = 0.0
approved_count = 0.0

fail_sum = 0.0
fail_count = 0.0

for i in range(1, n + 1):
    while True:
        grade = float(input(f"Enter grade #{i}: "))
        if 0 <= grade <= 100:
            break
    print("The value must be between 0 and 100.")

total_sum += grade

if grade >= 70:
    approved_sum += grade
    approved_count += 1
else:
    fail_sum += grade
    fail_count += 1

avg_all = total_sum / n
avg_approved = approved_sum / approved_count if approved_count > 0 else None
avg_fail = fail_sum / fail_count if fail_count > 0 else None

print("\n Results ")
print(f"Approved grades: {approved_count}")
print(f"Failed grades: {fail_count}")
print(f"Average of all grades: {avg_all}")

if avg_approved is not None:
    print(f"Average of approved grades: {avg_approved}")
else:
    print(f"N/A (You did not pass any grade)")

if avg_fail is not None:
    print(f"Average of failed grades:{avg_fail} ")
else:
    print("Great job, you passed all the grades ;)")
    


