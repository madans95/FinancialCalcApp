
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









