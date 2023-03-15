'''samp_string  = "This is a very important string"

print("length :", len(samp_string))

for i in range(0, len(samp_string)-1, 2):
   print(samp_string[i] + samp_string[i + 1])'''

#enter a string to hide in uppercase : 

#secret Message : 35647890

#Original Message : Hide

'''norm_string = input("Enter a string to hide in Uppercase : ")

secret_string = ""

for char in norm_string:
    secret_string += str(ord(char)-23)

print("secret Message : ", secret_string)

normal_string = ""
for i in range(0, len(secret_string)-1, 2):
    char_code = secret_string[i] + secret_string[i+1]

    normal_string += chr(int(char_code) + 23)

print("original Message :", norm_string)'''

rand_string = "  this is an a important string   "

rand_string = rand_string.strip()
print(rand_string)
print(rand_string.capitalize())
print(rand_string.upper())
print(rand_string.lower())

a_list = ["bunch", "of", "random", "words"]
print(" ".join(a_list))

a_list2 = rand_string.split()
for i in a_list2:
    print(i)

print("How many is :", rand_string.split().count("this"))

print("Where is string :",rand_string.find("string"))
print(rand_string.replace("an ", "a kind of "))