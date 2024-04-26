import random

# Generate a list of 20 random numbers
A = [random.randint(-10, 10) for _ in range(20)]

# Count the number of negative elements in the list
negative_count = sum(1 for num in A if num < 0)

print("List A:", A)
print("Number of negative elements in list A:", negative_count)
