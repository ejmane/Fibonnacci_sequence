import random

length_to_create = input("How many Fibonacci numbers do you want to create? ")
length_to_create = int(length_to_create)

fibonacci_list = [1, 1]

for i in range(length_to_create -2):
    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

print(fibonacci_list)
#test
