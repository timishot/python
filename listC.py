import random
import math

multiTable = [[0] * 10 for i in range(10)]

for i in range(1,10):
    for j in range(1, 10):
        multiTable[i][j] = i * j

for i in range(1,10):
    for j in range(1, 10):
        print(multiTable[i][j], end=", ")
    print()
# listTable = [[0] * 4 for i in range(4)]

# for i in range(4):
#     for j in range(4):
#         listTable[i][j] = "{} : {}".format(i, j)

# for i in range(4):
#     for j in range(4):
#         print(listTable[i][j], end=" || ")
# multiDlist = [[0] * 10 for i in range(10)]

# multiDlist[0][1] = 10
# print(multiDlist[0][1])

# multiDlist = [[0] * 5 for i in range(5)]

# for i in range(5):
#     for j in range(5):
#         multiDlist[i][j] = random.randint(1, 10)

# print(multiDlist)



# numList = [1,2,3,4,5]

# listOfValues = [[math.pow(m,2), math.pow(m,3), math.pow(m,4)]
#                 for m in numList]

# for i in listOfValues:
#     print(i)
# print()
# evenList = [i*2 for i in range(10)]

# for i in evenList:
#     print(i)