num1, num2 = input("Enter 2 values to divide : ").split()

try:
    quotient =int(num1)/int(num2)

    print("{} / {} ={}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")
except ValueError:
    print("Invalid literal")

else:
    print("You did't raise an exception")


finally:
    print("i execute no matter what")