import random

# Generate a list of 20 random numbers
B = [random.randint(-10, 10) for _ in range(20)]

# Calculate the sum of positive elements in the list
positive_sum = sum(num for num in B if num > 0)

print("List B:", B)
print("Sum of positive elements in list B:", positive_sum)
