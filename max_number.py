# The last item to code
# last one
# In this program, I need to find how many apples I can buy if I input a certain amount

# Procedures:
    # I need something where one can input their money
    # Then input the price of the apple they're buying
    # I think the next would be division, wherein; this will be the max number of apple one can buy
    # Then, multiply the number of apple, wherein; the price and the max number would be the variables
    # next would be subtraction of the money inputted then the price of the apple
    # Finally, the printing of the statement

# Starting Officially! currently 23:12 

def Money(money,apple):
    max = money//apple
    return max

cash = int(input("How much money you have in hand: "))
price = int(input("How much each apple cost: "))

print(f"You currently have {cash} pesos in hand.")
maxNumber = Money(cash,price)
# I included the printing so the user can follow what they are doing
print(f"You can buy {maxNumber} apples with the money you have." )

def Payables(pay,now):
    liability = pay*now
    return liability

Cost = Payables(maxNumber,price)
print(f"The amount is {Cost}.")

def Change():
    change = cash-Cost
    return change

total = Change()

def final():
    amount = print(f"You can buy {maxNumber} apples and your change is {total} pesos.")
    return amount

print(final())

    
