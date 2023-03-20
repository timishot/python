timiDict = {"fName": "Timi", "lName": "Adeniran", "Address": "6 jerusalem"}

print("My name :", timiDict["fName"])

timiDict["Address"] = "215 james"

timiDict["city"] = "lagos"

print("is there a city:", "city" in timiDict)

print(timiDict.values())
print(timiDict.keys())

for k, v in timiDict.items():
    print(k, v)

print(timiDict.get("lName", "Not here"))

del timiDict["lName"]

for i in timiDict:
    print(i)

timiDict.clear()


employee = []

fName, lName = input("Enter Employee Name : ").split()

employee.append({'fName': fName, 'lName': lName})
print(employee)
