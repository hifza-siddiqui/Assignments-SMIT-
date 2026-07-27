import random

def welcome():
# ------>>Display welcome message
    print("=" * 55)
    print("\t🎮 Welcome to Number Guessing Game! 🎮")
    print("=" * 55)
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess it?")
    print("=" * 55)

def play_game():
    """Main game logic"""
    # Computer selects a random number (using random module from Class 12)
    secret_number = random.randint(1, 100)
    
    attempts = 0
    guessed = False
    
    while not guessed:
        # Get player's guess
        guess = int(input("\nEnter your guess: "))
        attempts += 1
        
        # Check the guess
        if guess < secret_number:
            print("📉 Too Low! Try a higher number.")
        elif guess > secret_number:
            print("📈 Too High! Try a lower number.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
            guessed = True

def play_again():
    """Ask if player wants to play again"""
    choice = input("\nDo you want to play again? (yes/no): ").lower()
    return choice == "yes" or choice == "y"

def main():
    """Main program"""
    welcome()
    
    playing = True
    
    while playing:
        play_game()
        playing = play_again()
    
    print("\n👋 Thanks for playing! Goodbye!")

# Run the game
if __name__ == "__main__":
    main()