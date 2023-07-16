
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
    return(grossSalary/EMI)
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








