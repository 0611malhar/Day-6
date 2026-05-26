import sys
p1 = input("Player 1\nChoose from Snake, Water & Gun :)")
p1 = p1.lower()
p2 = input("Player 2\nChoose from Snake, Water & Gun :)")
p2 = p2.lower()

if p1 == p2:
    print("tie")
    sys.exit()


if p1 == "snake":
    if p2 == "gun":
        print("Player 2 wins")
    elif p2 == "water":
        print("Player 1 wins")


elif p1 == "water":
    if p2 == "snake":
        print("Player 2 wins")
    elif p2 == "gun":
        print("Player 1 wins")


else:
    if p2 == "snake":
        print("Player 1 wins")
    elif p2 == "water":
        print("Player 2 wins")