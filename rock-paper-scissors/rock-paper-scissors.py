from random import choice

def check_win(user, computer):
    if (user == 'r' and computer == 's') or (user == 's' and computer == 'p') or (user == 'p' and computer == 'r'):
        return True
    elif (computer == 'r' and user == 's') or (computer == 's' and user == 'p') or (computer == 'p' and user == 'r'):
        return False

def rock_paper_scissors():
    player_wins = 0
    opponent_wins = 0
    rounds = int(input("how many rounds do you want to play?: "))
    for _ in range(rounds):
        print(f"player wins: {player_wins} and opponent wins: {opponent_wins}")
        player = input("What is your choice - 'r' for rock, 's' for scissor, 'p' for paper: ")
        choices = ['r','s','p']
        opponent = choice(choices)

        if check_win(player, opponent):
            print(f"Yay! you won! Choice is {opponent}")
            player_wins += 1

        elif check_win(player, opponent) == False:
            print(f"You lost! Choice is {opponent}")
            opponent_wins += 1

        elif player == opponent:
            print(f"Its a Tie! opponent is {opponent}")
    
    print(f"player wins: {player_wins} and opponent wins: {opponent_wins}")


rock_paper_scissors()
