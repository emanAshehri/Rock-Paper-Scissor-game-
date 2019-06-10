
import random
import time
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
"""The Player class is the parent class for all of the Players
in this game"""


def print_pause(message):
    print(message)
    time.sleep(2)


# text effects
pT = '\33[95m'  # pink Text
pB = '\33[105m'  # pink Background
gB = '\x1b[6;35;47m'  # grey Background
e1 = '\33[0m'
e2 = '\x1b[0m'  # end of the color
b = '\033[01m'  # bold text
yB = '\33[103m'  # yellow Background

moves = ['rock', 'paper', 'scissors']


class Player:

    def __init__(self):
        self.my_move = moves
        self.their_move = random.choice(moves)

    def learn(self, my_move, their_move):
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class RockerPlayer(Player):
    def move(self):
        return 'rock'


class CopyPlayer(Player):
    # imitate the pervious other player move
    def move(self):
        if self.their_move is None:
            return self.my_move
        return self.their_move

class CyclePlayer(Player):  # Rock -> Paper -> Scissors -> Rock -> ...

    def __init__(self):
        self.lastmove = 'rock'

    def move(self):
        if self.learn is None:
            return random.choice(moves)

        elif self.lastmove == 'scissors':
            return 'rock'

        else:
            last_move = self.lastmove
            nextmove = moves[moves.index(last_move) + 1]
            return nextmove

    def learn(self, my_move, their_move):
        self.lastmove = my_move
        return self.lastmove


class HumanPlayer(Player):
    def move(self):
        print_pause("\nWhat is you move ?")
        humanMove = input("Rock, paper, scissors?").lower()
        while humanMove not in moves:
            print("\nI wasn't expect that, try again")
            humanMove = input("Rock, paper, scissors?").lower()
        return humanMove


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        self.score1 = 0
        self.score2 = 0

    def intro():
        print_pause(f"\n{yB}Rock, Paper, Scissor Game{e1}\n")
        print_pause("Welcom, I am Eman, Your host. \nNice to meet you! ")
        print_pause("""
You can choose what strategy do you want me to use:
Rocker - Randomizer - reflict - Cycler """)

    def beats(self, move1, move2):
        return ((move1 == 'rock' and move2 == 'scissors') or
                (move1 == 'scissors' and move2 == 'paper') or
                (move1 == 'paper' and move2 == 'rock'))

    def rounds(self):
        while True:
            self.rounds = input(f"{pT}How many rounds do you want to play?\n")
            if self.rounds.isdigit():
                return self.rounds

    def play_round(self):

        move1 = self.p1.move()
        move2 = self.p2.move()

        if move1 == move2:
            result = 'TIE, No winner.'

        elif self.beats(move1, move2):
            self.score1 += 1
            result = " YOU WINS "

        else:
            self.score2 += 1
            result = ' I WINS '

        print_pause(f"\nYou played : {move1}")
        print_pause(f"And I played : {move2}")
        print_pause(f"\n{result}\n")
        print_pause(f"{pB}  Score  {e1}")
        print_pause(f"  {self.score1} | {self.score2}\n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def final_score(self):

        winner = {
            '1st_wins': f"{pT}Congratulations! You are the Winner!{e1}",
            '2nd_wins': f"\n{pT}WOW!! I AM THE WINNER!{e1} ",
            'Tie': f"\n{pT}It's a draw! Everyone's a Winner!{e1}"
                        }

        print_pause(f"\n{pB}  Final Score  {e1}")
        print_pause(f"    {self.score1} | {self.score2}\n")

        if self.score1 == self.score2:
            print_pause(winner['Tie'])

        elif self.score1 > self.score2:
            print_pause(winner['1st_wins'])

        else:
            print_pause(winner['2nd_wins'])

    def play_game(self):
        self.rounds()
        print_pause(f"\n{yB}Game start!{e1}\n")
        print_pause("Ready ? Let's begin!\n")
        for round in range(int(self.rounds)):
            round += 1
            print(f"\n{gB} Round {round} {e2}")
            self.play_round()
        self.final_score()
        print_pause("Amazing game , I hope you injoy it as much as I do")


if __name__ == '__main__':
    choose_player2 = {
                   'rocker': RockerPlayer(),
                   'randomizer': RandomPlayer(),
                   'reflict': CopyPlayer(),
                   'cycler': CyclePlayer()}
    Game.intro()
    p1 = HumanPlayer()
    p2 = input(f"{pT}So, What is your choice?{e1}\n").lower()
    while p2 not in choose_player2:
        p2 = input("I don't know that!,\n What is your choice?\n").lower()

    game = Game(p1, choose_player2[p2])
    game.play_game()
