# The last item to code
# last one
# In this program, I need to find how many apples I can buy if I input a certain amount

# Procedures:
    # I need something where once can input their money
    # Then input the price of the apple they're buying
    # I think the next would be division, wherein; this will be the max number of apple one can buy
    # Then, multiply the number of apple, wherein; the price and the max number would be the variables
    # next would be subtraction of the money inputted then the price of the apple
    # Finally, the printing of the statement

# Starting Officially! currently 23:12 

def Money():
    howMuch = int(input("How much money you have in hand: "))
    return howMuch

money = print(f"You currently have {Money()} in hand.")

def Pay():
    price = int(input("How much is the Apple?: "))
    return price

Price = print(f"The apple costs {Pay()} pesos.")

