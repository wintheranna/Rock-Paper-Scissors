import random

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


    def beats(one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))


class RockPlayer(Player):

    def move(self):
        return moves[0]


class CyclePlayer(Player):

    def move(self):
        if self.my_move is None:
            return random.choice(moves)
        if self.my_move == "rock":
            return "paper"
        elif self.my_move == "paper":
            return "scissors"
        else:
            return "rock"

    def learn(self, my_move, their_move):
        self.my_move = my_move


class ReflectPlayer(Player):

    def move(self):
        if self.their_move is None:
            return random.choice(moves)
        else:
            return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class RandomPlayer(Player):

    def move(self):
        move = random.choice(moves)
        return move


class HumanPlayer(Player):

    def move(self):
        while True:
            humanMove = input("Rock, paper, scissors?").lower()
            if humanMove in moves:
                return humanMove
            else:
                print("Invalid input.Try again.")


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")


if __name__ == '__main__':
    game = Game(Player(), Player())
    game.play_game()
