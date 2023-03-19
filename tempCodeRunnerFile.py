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