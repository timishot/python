class DogNameError(Exception):

    def __init__(self, args, **kwargs):
        Exception.__init__(self, *args,**kwargs)

try:
    DogName = input("what is your dog name :")

    if any(char.isdigit() for char in DogName):

        raise DogNameError
    

except DogNameError:
    print("YOur dog name cant contain a number")