from random import randint

# Ask for user's name
user_name = input("Hi! What is your name?\n")


# The computer gets 5 guesses, so loop 5 times
for num in range(5):

    # Guess your birth month (1-12) and year (1924-2004, including those years)

    birth_month = int(randint(1, 12))
    birth_year = int(randint(1924, 2004))

    print("Guess", num + 1, ": ", user_name,
          "were you born in", birth_month, "/", birth_year, "?")
    response = input("yes or no?\n")

# If user inputs yes due to correct answer, then print "I knew it!" and end the game

    if response == "yes":
        print("I knew it!")
        exit()

# If the computer has guessed more than 5 times, then print "I have other things to do. Good bye."

    elif num < 5:
        print("I have other things to do. Good bye.")

# If user inputs no due to incorrect answer, then print "Drat! Lemme try again!"

    elif response == "no":
        print("Drat! Lemme try again!")
