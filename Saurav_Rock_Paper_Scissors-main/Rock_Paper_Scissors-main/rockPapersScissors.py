from operator import truediv
import random

def gameWin(comp,you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False
    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False  

print("Comp Turn : Rock(r) Paper(p) or Scissors(s)?")
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 'r'
elif randNo == 2:
    comp = 'p'
elif randNo == 3:
    comp = 's'

you = input("Your turn: Rock(r) Paper(p) or Scissors(s)?\n")
a = gameWin(comp, you)

print(f"Computer chose {comp}")
print(f"You chose {you}")

if a==None:
    print("Game is a tie.")
elif a:
    print("You win! ")
else:
    print("You lost.")
