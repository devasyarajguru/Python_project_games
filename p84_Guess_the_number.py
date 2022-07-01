import random

y = random.randint(1,20)
print(y)
c = 0
x = 0
s1 = 1
s2 = 20
while x!=y:

    print("Enter Your number between ", s1, "to", s2)
    x = int(input("Guess the number==>"))
    c = c + 1

    if x>20:
        print("You number is Invalid!")
    elif x<y:
        print("Try greater number:")
        s1 = x
    elif x>y:
        print("Try Lesser number:")
        s2 = x
    else:
        break

print("Your Guesses Tried for :",c)




