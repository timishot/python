class DogNameError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args,**kwargs)

try:
    DogName = input("what is your dog name :")

    if any(char.isdigit() for char in DogName):

        raise DogNameError("Your dog name can't contain a number.")
    

except DogNameError as e:
    print(e)

# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops! That was no valid number.  try again....") 

# class B(Exception):
# try:
#     aList =[1,2,3]

#     print(aList[3]) 

# except IndexError:
#     print("Sorry that index doesn't exist")

# except:
#     print("an unknown error occured")