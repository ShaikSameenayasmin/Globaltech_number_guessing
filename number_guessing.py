import random
def number_guessing_game():
    low_range = int(input("Enter lower bound:"))  # Define the lower bound of the range
    high_range = int(input("Enter upper bound:"))  # Define the upper bound of the range
    max_attempts = 7  # Define the maximum number of attempts
    print("You only have 7 chances to guess the integer!!")
    # Generate a random number within the range for the player to guess
    secret_number = random.randint(low_range, high_range)
    print(f"Welcome to the Number Guessing Game! Guess a number between {low_range} and {high_range}.")
    attempts = 0
    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            if guess < low_range or guess > high_range:
                print("Your guess is outside the valid range. Please try again.")
                continue
            attempts += 1
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You did it in {attempts} try and your correct guessed number is {secret_number} .")
                break
            remaining_attempts = max_attempts - attempts
            print(f"Remaining attempts: {remaining_attempts}")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")   
    else:
        print(f"Sorry, you have used all {max_attempts} attempts. The correct number was {secret_number}.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "yes":
        number_guessing_game()
    else:
        print("Thank you for playing!")
if __name__ == "__main__":
    number_guessing_game()