3# Put your function here
def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n<0:
        return print("Invalid answer, factorial cannot be done on negatives")
    else:
        return n * factorial(n-1)
# testing
num = 5
print(factorial(num))
