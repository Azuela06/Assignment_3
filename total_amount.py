#another item huhu
# what I need to do this time is to know how much the apples and orange if in a certain value
# To find the amount of apple I think I should multiply first
# just like the apple, multiply first 
# then add. Right?

def TotalApple(applePrice,numberApple):
    product = applePrice*numberApple
    return product

Apple = 20
appleYouWant = int(input("How many apples do you want: "))

apple = TotalApple (Apple, appleYouWant)

def TotalOrange(orangePrice,numberOrange):
    Product = orangePrice*numberOrange
    return Product

Orange = 25
orangeYouWant = int(input("How many Oranges do you want: "))

orange = TotalOrange(Orange,orangeYouWant)

def TotalAmount(amountApple,amountOrange):
    Sum = int(amountApple + amountOrange)
    return Sum

Amount = TotalAmount(apple,orange)          #kind of forgot how to print lmao.

def statement():
    finalStatement = print(f"The total amount is {Amount}.")
    return finalStatement

print(statement())