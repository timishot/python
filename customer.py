# create an list
customers = []

# creata a loop
while True:
    createEntry = input("Enter Customer (Yes/No) : ")
    createEntry = createEntry[0].lower()

    #check  to leave loop
    if createEntry == 'n':
        break
    #Get customers data
    else:
        fName, lName  = input("Enter customer Name: ").split()
    #add customrt data to list
        customers.append({'fName': fName, 'lName': lName})

        
#Get input and make it for y or n
for cust in customers:
    print(cust['fName'], cust['lName'])
#check to leave loop

#Get customer data

#Add customer data to list

#print costomer data
