# I'll try to have a different approach? If I can
# It should be able to print "Hi, my name is _____. I am ____ years old and I live in _____ ."

# I think it will be better if I separate two names. Just for additional work lmao.
def ArtistName():
    given = input("First Name: " )
    last = input ("Last Name: ")
    return given + " " + last 

name = ArtistName()

def ArtistAge():
    toshi = input("Age: ")
    return toshi

age = ArtistAge()

# I tried using direct substitution of the function
def ArtistAddress():
     jusho = input("Address: ")
     return jusho

Address = ArtistAddress()

def Statement():
    statement = input(f"Hi, my name is {name}. I am {age} years old and I live in {Address}.")
    return statement

print(Statement())
