import random

retrieve = input("Enter the digit of the fibonacci sequence you would like: ")



def n_th_num(end):
    end = int(end)
    fib1 = 1
    fib2 = 1
    for i in range(end-1):
        fib2 = fib2 + fib1
        fib1 = fib2 - fib1
    print("The digit is:", fib1)


n_th_num(retrieve)