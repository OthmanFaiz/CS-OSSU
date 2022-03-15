# bisection search


low = 0
high = 100


print("Please think of a number between 0 and 100!")

while True:
    bisection = (low + high) // 2
    print("Is your secret number", bisection, "?")
    user = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if user == "h":
        high = bisection
        
    elif user == "l":
        low = bisection

    elif user == "c":
        print("Game over. Your secret number was:", bisection)
        break

    else:
        print("Sorry, I did not understand your input.")
        continue