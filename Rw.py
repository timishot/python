import os

with open("mydata.txt", mode="w", encoding="utf-8") as myFile:
    myFile.write("Some Random text\nMore random text\nand some more")

with open("mydata.txt", encoding="utf-8") as myFile:

    print(myFile.read())

print(myFile.closed)

print(myFile.name)

print(myFile.mode)

os.rename("mydata.txt", "mydata6.txt")

os.remove("mydata6.txt")

# os.mkdir("mydir")

os.chdir("mydir")

print("current Directory :", os.getcwd())

# os.chdir("..")

print("Current Directory :", os.getcwd)