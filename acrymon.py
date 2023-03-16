'''acronym = input("Enter the word you want to turn to acronym: ")
acronym = acronym.upper()
list_of_words = acronym.split()
for word in list_of_words:
    print(word[0], end= "")
print()'''

letter_z = "z"
num_3 = "3"
a_space = " "
print("Is z a letter or number :", letter_z.isalnum())

def isfloat(str_val):
    try:
        float(str_val)
        return True
    except ValueError:
        return False
print("is PI a Float :", isfloat(num_3))