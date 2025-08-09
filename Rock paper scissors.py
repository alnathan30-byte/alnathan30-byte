import random

def get_player_choice(player_name):
    choice = input(f"{player_name}, enter your move (rock, paper, scissors): ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please choose rock, paper, or scissors.")
        choice = input(f"{player_name}, enter your move (rock, paper, scissors): ").lower()
    return choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(p1, p2):
    if p1 == p2:
        return "draw"
    if (p1 == "rock" and p2 == "scissors") or \
       (p1 == "paper" and p2 == "rock") or \
       (p1 == "scissors" and p2 == "paper"):
        return "player1"
    else:
        return "player2"

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    mode = input("Choose mode: 1 for vs Computer, 2 for 2-Player: ")
    while mode not in ['1', '2']:
        mode = input("Invalid. Choose 1 (vs Computer) or 2 (2-Player): ")

    rounds = input("Best of 3 or 5? Enter 3 or 5: ")
    while rounds not in ['3', '5']:
        rounds = input("Invalid. Enter 3 or 5: ")
    rounds = int(rounds)
    wins_needed = rounds // 2 + 1

    player1_score = 0
    player2_score = 0
    round_num = 1

    while player1_score < wins_needed and player2_score < wins_needed:
        print(f"\n--- Round {round_num} ---")
        p1_choice = get_player_choice("Player 1")

        if mode == '1':
            p2_choice = get_computer_choice()
            print(f"Computer chose: {p2_choice}")
        else:
            p2_choice = get_player_choice("Player 2")

        result = decide_winner(p1_choice, p2_choice)

        if result == "draw":
            print("It's a draw!")
        elif result == "player1":
            print("Player 1 wins this round!")
            player1_score += 1
        else:
            print("Player 2 wins this round!" if mode == '2' else "Computer wins this round!")
            player2_score += 1

        print(f"Score - Player 1: {player1_score}, {'Player 2' if mode == '2' else 'Computer'}: {player2_score}")
        round_num += 1

    if player1_score > player2_score:
        print("\n Player 1 wins the game!")
    else:
        print("\n Player 2 wins the game!" if mode == '2' else "\n Computer wins the game!")

if __name__ == "__main__":
    play_game()