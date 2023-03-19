

# def islower(c):
#     letter = ord(c)
#     for i in range(ord('a'), ord('z')+1):
#         if letter == i:
#             return True
    
#     print("hello")
#     return False

def uppercase(s):
    for c in s:
        # Convert lowercase letters to uppercase
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - ord('a') + ord('A'))
        # Print the character without a newline
        print(c, end='')
    # Print a newline at the end of the string
    print()

str = input("Enter text :")
uppercase(str)

# def uppercase(s):

#     diff = ord('a') - ord('A')

#     for c in s:

#         if ord('a') <= ord(c) <= ord('z'):

#             c = chr(ord(c) - diff)

#         print(c, end='')

#     print()



str = input("Enter your text: ")

uppercase(str)





# def islower(c):

#     letter = ord(c)

#     if letter in range(ord('a'), ord('z')+1):
#          return True
#     else:
#          return False

           

# ans = islower('E')

# print(ans)