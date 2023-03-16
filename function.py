def add_numbers(num1, num2):
    return (num1 + num2)
print("5 + 4 =", add_numbers(5,4))

def assign_name():
    name = "Doug"

assign_name()

def solve_eq(equation):
    x, add, num1, equal, num2 = equation.split()
    num1, num2 = int(num1), int(num2)

    return "x ="+ str(num2 - num1)

print(solve_eq("x + 4 = 9"))

def mult_divide(num1, num2):
    return (num1 * num2), (num1/num2)

mult, divide = mult_divide(5,4)

print("5 * 4=", mult)
print("5/4=", divide)

# a prime can only by one and itself

#input mAX prime
#use a for loop and check if modul == 0  True

def isPrime(num):
    for i in range(2, num):
        if(num % i)==0:
            return False
    return True
#list prime

def getPrimes(max_number):
    list_of_primes = []

    for num1 in range(2, max_number):
        if isPrime(num1):
            list_of_primes.append(num1)
    return list_of_primes
    
max_num_to_check = int(input("Search for Primes up to : "))

list_of_primes = getPrimes(max_num_to_check)

for prime in list_of_primes:
    print(prime)

