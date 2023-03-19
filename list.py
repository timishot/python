import random
import math

# randList = ["string", 1.234, 28]

# oneTOTEN = list(range(10))

# randList = randList + oneTOTEN

# print(randList[0])

# print("list length : ", len(randList))

# first3 = randList[0:3]

# for i in first3:
#     print("{} : {}".format(first3.index(i), i))

# print(first3[0] * 3)

# print('string' in first3)

# print("index of string : ", first3.index("string"))

# print("How many string :", first3.count("string"))

# first3[0] = "New string"

# for i in first3:
#     print("{} : {}".format(first3.index(i), i))
          
# first3.append("another")
# for i in first3:
#     print("{} : {}".format(first3.index(i), i))


numList = []

for i in range(5):
    numList.append(random.randrange(1, 10))

numList.insert(5, 10)

numList.remove(10)

numList.pop(2)



# i = len(numList) - 1

# while(i > 1):
#     j = 0
#     while j < i:

#         print("\nIs {} > {}".format(numList[j], numList[j+1]))
#         if numList[j] > numList[j + 1]:
#             print("Switch")
#             temp = numList[j]
#             numList[j] = numList[j + 1]
#             numList[j + 1] = temp 
#         else:
#             print("DOn't Switch")

#         j += 1

#         for k in numList:
#             print(k,end=", ")
#         print()

#     print("End of Round")
#     i -= 1
for k in numList:
    print(k, end=", ")
print ()