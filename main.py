salary = print(int(input("enter your salaray: ")))
houserent = print(int(input("enter your houserent: ")))
groceries = print(int(input("enter your groceries: ")))
emi = print(float(input("enter your emi: ")))
petrolexpenses = print(int(input("enter your petrol expenses: ")))

# added input

# List of Expenditures
expenditureList = []

grossSalary = int(input("Enter Gross Salary: "))

stop = False
counter = 1
while not stop:
    print("Enter Expenditure ", counter)
    expenditure = float(input())
    expenditureList.append(expenditure)
    counter = counter + 1
    yes_no = input("Any Other Expenditure?(Yes/No)")
    if yes_no == "yes":
        stop = False
    else:
        stop = True

print(expenditureList)


grossSalary=int(input("Enter your gross salary"))
houseRent=int(input("Enter your house rent"))
grosseries=int(input("Enter groceries"))
EMI=int(input("Enter your EMI details"))
petrol_expenses=int(input("Enter your petrol expenses"))

def salary_savings():
    savings=grossSalary-houseRent-grosseries-EMI-petrol_expenses
    return savings
   
print(salary_savings())

def emi_percent():
    return(grossSalary/EMI*100)
print(emi_percent())

g=grossSalary
def Tax(g):
    "g is gross salary per month"
    pft=200 ##professional tax
    epf=g*0.12 ##provident fund
    ns=g-pft-epf ##net salary
    
    ##ih is in-hand salary
    if(ns*12<=250000 and ns>0) :
        ih=ns
    elif(ns*12>250000 and ns<500000) :
        ih=0.95*ns
    elif(ns*12>=500000 and ns<=1000000) :
        ih=0.8*ns
    elif(ns*12>=1000000) :
        ih=0.7*ns

    return ih
    
print(Tax(b))









