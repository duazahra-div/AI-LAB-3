#Write a program to guess a number between 1 to 9
number = 5
while True:
    guess = int(input("Guess a number between 1 and 9: "))
    if guess == number:
        print("Well guessed!")
        break