import random
Objects = ['Rock','Paper','Scissors']
Win = 0     #0 for draw, 1 for win and 2 for lose
PCObject = random.choice(Objects)

print("Play your turn by typing either 'Rock', 'Paper' or 'Scissors'.")
UserObject=input()

if 'Rock'==UserObject:
    if 'Paper' == PCObject:
        Win=2
    elif 'Scissors'==PCObject:
        Win=1
elif 'Paper'==UserObject:
    if 'Scissors' == PCObject:
        Win = 2
    elif 'Rock' == PCObject:
        Win = 1
else:
    if 'Rock' == PCObject:
        Win = 2
    elif 'Paper' == PCObject:
        Win = 1

if 0==Win:
    print("Both of you choose "+UserObject+". So it is a draw.")
elif 1==Win:
    print("You choose "+UserObject+". And PC choose "+PCObject+". So you win!")
else:
    print("You choose " + UserObject + ". And PC choose " + PCObject + ". So PC wins!")

