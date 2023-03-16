t as it is
    if char.isalpha():
        #Get thecharacter code and add the shift amount
        char_code = ord(char)
        char_code += key

        #if uppercase then compare to upper caseunicosdes
        if char.isupper