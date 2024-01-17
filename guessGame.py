secret_word = "influence"
guess = ""
guess_limit = 3
guess_count = 0
out_of_guess = False

while guess != secret_word and not out_of_guess:
    if guess_count < guess_limit:
        guess = input("Enter Guess: ")
        guess_count += 1

    else:
       out_of_guess = True


if out_of_guess:
    print("You are out of limit, You lose!")

else:
    print("You win")

