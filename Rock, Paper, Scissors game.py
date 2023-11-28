import random
import time


def print_pause(word):
    print(word)
    time.sleep(2)


class Player:
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.p1choice = self.moves
        self.p2choice = random.choice(self.moves)

    def learn(self, p1choice, p2choice):
        self.p1choice = p1choice
        self.p2choice = p2choice


class ReflectPlayer(Player):
    def move(self):
        return self.p2choice


class RandomPlayer(Player):
    def move(self):
        return random.choice(self.moves)


class HumanPlayer(Player):
    def learn(self, p1choice, p2choice):
        self.p1choice = p1choice
        self.p2choice = p2choice

    def move(self):
        while True:
            real_human_move = input("\n 'Rock', 'paper'"
                                    ", 'scissors?' or quit").lower()
            if real_human_move in self.moves:
                return real_human_move
            elif real_human_move == 'quit':
                exit()


class CyclePlayer(Player):
    def move(self):
        if self.p1choice == self.moves[0]:
            return self.moves[1]
        elif self.p1choice == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class AllRock(Player):
    def move(self):
        return "rock"


class Game:
    def __init__(self, player, bot):
        self.p1_score = 0
        self.p2_score = 0
        self.player = player
        self.bot = bot

    def win(self, player, bot):
        return ((player == 'rock' and bot == 'scissors') or
                (player == 'paper' and bot == 'rock') or
                (player == 'scissors' and bot == 'paper')
                )

    def turns(self):
        my_move = self.player.move()
        comp_move = self.bot.move()
        if self.win(my_move, comp_move):
            self.p1_score += 1
            outcome = print_pause("Player wins")
            champ = "Player won this round"

        elif my_move == comp_move:
            self.p1_score = self.p1_score
            self.p2_score = self.p2_score
            outcome = print_pause(f"Both players had "
                                  " same selections,It is a tie!")
            champ = "Tie"
        else:
            self.p2_score += 1
            outcome = print_pause("Bot wins")
            champ = "CPU won this round"
        print_pause(f" You chose: {my_move}")
        print_pause(f"\n Bot chose: {comp_move}")
        print_pause(f"\nYour score {self.p1_score} ")
        print_pause(f"CPU score  {self.p2_score} ")
        print_pause(f"\n {champ}")
        self.player.learn(my_move, comp_move)
        self.bot.learn(comp_move, my_move)

    def play_game(self):
        print_pause("Welcome to Rock, Paper, Scissors!")
        print_pause("---------------------------------")

        self.limits()
        for limit in range(int(self.game_limit)):
            print_pause(f" Game {limit + 1} ")
            self.turns()

        if self.p1_score > self.p2_score:
            print_pause("\n PLAYER defeated CPU")
        elif self.p2_score > self.p1_score:
            print_pause("\n CPU defeated Player")
        else:
            print_pause("Draw , PLAYER & CPU HAD EQUALL WINS")
        print_pause(f"\nYour results {self.p1_score} ")
        print_pause(f"CPU results  {self.p2_score} ")

    def limits(self):
        while True:
            self.game_limit = input(
                "\n How many turns should be the game limit or input 'quit'")
            if self.game_limit.isdigit():
                return self.game_limit
            elif self.game_limit.lower() == 'quit':
                exit()


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
        [RandomPlayer(), AllRock(),
         ReflectPlayer(), CyclePlayer()]))
    game.play_game()
