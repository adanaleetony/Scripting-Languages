from random import randint
print("Welcome to Piglet")
roll = randint(1,6)
count = 0
while roll != 1:
    count += roll
    print("You rolled a",roll)
    answer = input("Roll again? ")
    if answer == "yes" or answer == "y":
        roll = randint(1,10)
    elif answer == "no" or answer == "n":
        print(f"You got {count} points")
        break
if roll == 1:
    print(f"You rolled a {roll}")
    print("You got 0 points.")