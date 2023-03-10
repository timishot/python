money = input("How much to invest : ")
interest_rate =  ("Interest rate : ")

money = float(money)

interest_rate = float(interest_rate) * .01

for i in range(10):
    money = money + (money * interest_rate)

print("investment after 10 years : {:2f}".format(money))