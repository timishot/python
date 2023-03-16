#Recieve the message to encrypt and the number of character to shift
message = input("Enter your message : ")
key = int(input("How many character should we shift(1 - 26)"))
#prepare the secret meassage
secret_message=""
#cycle through each character in thr message
for char in message:
    #if it isn't a letter then keep it as it is
    if char.isalpha():
        #Get thecharacter code and add the shift amount
        char_code = ord(char)
        char_code += key

        #if uppercase then compare to upper caseunicosdes
        if char.isupper():

            #if bigger than Z subtract 26
            if char_code > ord('Z'):
                char_code -= 26
            #if smaller than A add 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        secret_message += chr(char_code)
    else:
        secret_message += char
print("Encrypted :", secret_message)

key = -key
orig_message = ""

for char in secret_message:
    if char.isalpha():
        char_code = ord(char)
        char_code += key
        if char.isupper():
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26
        else:
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        orig_message += chr(char_code)
    else:
        orig_message += char
print("Decripted :", orig_message)



    
