import random
print("Welcome To The Word Guessing Game")
while True:
    a=int(input("Enter A number Between 0-100: "))
    b=random.randint(0,100)
    if abs(a-b)==10:
        if a>b:
            print("Too High")
        else:
            print("Too Low")
    elif a==b:
        print("You Guessed The Right Number")
    else:
        print("You Choose A Close Number")
    c=input("Do You Want To Play Again:")
    if c.upper()=="NO":
        print("Thank You")
        break
