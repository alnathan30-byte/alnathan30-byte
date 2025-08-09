import random

# Global trackers
high_score = None
game_number = 1
game_results = []  # To store results of each game


def play_game():
    global high_score, game_number

    print(f"\n🎯 Welcome to the Number Guessing Game! (Game {game_number})")
    print("Choose a difficulty level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    choice = input("Enter 1, 2, or 3: ")
    if choice == '1':
        max_attempts = 10
    elif choice == '2':
        max_attempts = 7
    elif choice == '3':
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to Easy level.")
        max_attempts = 10

    secret_number = random.randint(1, 100)
    attempts = 0
    won = False

    print(f"\nGuess the number between 1 and 100. You have {max_attempts} attempts!")

    while attempts < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("⛔ Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("📉 Too low!")
        elif guess > secret_number:
            print("📈 Too high!")
        else:
            print(f"🎉 Correct! The number was {secret_number}.")
            print(f"You guessed it in {attempts} attempt(s)!")
            won = True

            # Update high score
            if high_score is None or attempts < high_score:
                high_score = attempts
                print("🏆 New High Score!")
            else:
                print(f"🥈 Your best score so far is {high_score} attempt(s).")
            break

    if not won:
        print(f"\n💥 Game Over! The correct number was {secret_number}.")
        if high_score is not None:
            print(f"🎖️ Your best score so far is {high_score} attempt(s).")

    # Save game result
    result = {
        "game": game_number,
        "result": "✅ Won" if won else "❌ Missed",
        "secret_number": secret_number,
        "attempts": attempts if won else "—"
    }
    game_results.append(result)

    game_number += 1


# Main loop
while True:
    play_game()
    again = input("\n🔁 Do you want to play again? (yes/no): ").lower()
    if again not in ['yes', 'y']:
        break

# 📊 Show Summary
print("\n📋 Game Summary:")
for game in game_results:
    print(f"{game['game']}️⃣ Game {game['game']} – {game['result']} – Number: {game['secret_number']} – Attempts: {game['attempts']}")

# 🏆 Best Score
if high_score:
    print(f"\n🏆 Best Score: {high_score} attempt(s)")
else:
    print("\n🏆 Best Score: None (Try to win a game!)")

print("\n👋 Thanks for playing! Goodbye.")