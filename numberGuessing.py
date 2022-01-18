import random
numberGuessing = random.randint(1, 9)
chances = 0
while (chances < 5):
    theNumber = int(input("enter the number between 1-9: "))
    if (theNumber > numberGuessing):
        print("The number you chose is too high, TRY AGAIN")
    elif (theNumber == numberGuessing):
        print("You did it...... Congratulation!")
    else :
        print("The Number you chose is too low, TRY AGAIN")
    chances = chances + 1
if (chances > 5):
    print("You are out of chances")