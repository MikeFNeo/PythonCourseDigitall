import random

print("Welcome to Guess the Number!")

# Set the range for the random number
lower_bound = 1
upper_bound = 10
secret_number = random.randint(lower_bound, upper_bound)

# Set the number of allowed guesses
max_guesses = 3

# Optional: Set difficulty level
difficulty = "easy"  # You can change this to "medium" or "hard" for different difficulty levels

print(f"Guess the number between {lower_bound} and {upper_bound}. You have {max_guesses} guesses. ({difficulty} level)")

for attempt in range(1, max_guesses + 1):
    user_guess = int(input("Enter your guess: "))

    # Check if the guess is within bounds
    if user_guess < lower_bound or user_guess > upper_bound:
        print("Your guess is out of bounds. Try again.")
        continue

    # Provide feedback to the user
    if user_guess == secret_number:
        print(f"Congratulations! You guessed it right. Bravo, you guessed my number.")
        break
    elif user_guess < secret_number:
        print("Too low!")
    else:
        print("Too high!")

# If the loop completes without a correct guess
else:
    print(f"Sorry, you've run out of guesses. The correct number was {secret_number}. Better luck next time!")