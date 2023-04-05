import random

#length_to_create = input("How many Fibonacci numbers do you want to create? ")
#length_to_create = int(length_to_create)

#fibonacci_list = [1, 1]

#for i in range(length_to_create -2):
#    fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])

#print(fibonacci_list)

#Get n-th Fibonacci number

fib1 = 1
fib2 = 1
fib3 = 0

def n_th_num(end):
    global fib1, fib2, fib3
    for i in range(end-1):
        fib2 = fib2 + fib1
        fib1 = fib2 - fib1
    print(fib1)

n_th_num(3)