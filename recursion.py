def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num -1)
        return result

num = int(input("Enter a number to be factorized: "))
print("{}!= ".format(num), factorial(num))