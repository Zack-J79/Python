# start
import random
# Generate a random number between 1 and 100
random_number = random.randint(1,100)
# Get player's name
player_name = input("Enter Your Name Please:")
# Display Welcome Message
print(f"Hello, {player_name}, Welcome to the Guess the Number Game!")
# Variables
attempts = 0
correct_guess = False
# Loop until the player guesses the correct number
while not correct_guess:
    # Allow player to guess the number
    player_guess = int(input("Guess the number (between 1 and 100): "))
    # Increment attempts counter
    attempts += 1
    # Check to see if the number is correct, too high, or too low
    if player_guess == random_number:
        correct_guess = True
        print(f"Correct!! You guessed the correct number in {attempts} attempts.")
    elif player_guess > random_number:
        print("Too High!! Sorry, Try again.")
    else:
        print("Too Low!! Sorry, Try again.")
# Display Game Over message
print("Thank you for playing the numbers game! Game Over!")
# end
