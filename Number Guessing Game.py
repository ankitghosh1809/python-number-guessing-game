import random
print("Welcome To The Word Guessing Game")
while True:
    a=int(input("Enter A number Between 0-100: "))
    b=random.randint(0,100)
    if abs(a-b)==10:
        if a>b:
            print("Too High")
            print("The Correct Number is: ",b)
        else:
            print("Too Low")
            print("The Correct Number is: ",b)
    elif a==b:
        print("You Guessed The Right Number")
    else:
        print("You Choose A Close Number")
        print("The Correct Number is: ",b)
    c=input("Do You Want To Play Again:")
    if c.upper()=="NO":
        print("Thank You")
        break
