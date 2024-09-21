# start
import random
# Generate a random number between 1 and 100
random_number = random.randint(1,100)
# Get player's namez
player_name = input("Enter Your Name Please:")
# Display Welcome Message
print(f"Hello, {player_name}, Welcome to the Guess the Number Game!")
# Allow player to guess the number
player_guess = int(input("Guess the number (between 1 and 100)"))
# Check to see if the number is correct, too high or too low
if player_guess == random_number:
    print("Correct!! You guessed the correct number.")
elif player_guess > random_number:
    print("Too High!! Sorry, Try again.")
else: 
    print("Too Low!! Sorry, Try again.")
# Display Game Over message
print("Thank you for playing the numbers game! Game Over!")
# end

