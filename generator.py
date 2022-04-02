""" First exercise from Impractical Python Projects """
import random as rd

first = ("Clemens", "Andrea", "Lutz", "Sebastian")
last = ("Brauer", "Koch", "NewName")


while True:
    random_first = rd.choice(first)
    random_last = rd.choice(last)

    print("Hello. lets generate a new Name for you! \n\n")
    print(f"Your new Name is: {random_first} {random_last} \n\n ")

    doAgain = input("Wanna play again?\nHit Enter for playing again. Otherwise N:\n")

    if doAgain.lower() == "n":
        break
