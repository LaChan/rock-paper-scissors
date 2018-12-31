#!/usr/bin/env python3

import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""Function for the game's Win Condition"""


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        while True:
            response = input("Enter your move: rock, "
                             "paper, or scissors\nPress z to exit.\n").lower()
            if response in moves:
                break
            elif response == 'z':
                print("Thanks for playing!")
                quit()
            else:
                print("Please enter only rock, paper, scissors, or z")
        return response


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class ReflectPlayer(Player):
    def __init__(self):
        self.move_to_play = ""

    def learn(self, my_move, their_move):
        self.move_to_play = their_move

    def move(self):
        if self.move_to_play == "":
            return random.choice(moves)
        else:
            return self.move_to_play


class CyclePlayer(Player):
    def __init__(self):
        self.move_to_play = ""

    def learn(self, my_move, their_move):
        i = moves.index(my_move)
        if i == 2:
            i -= 2
        else:
            i += 1
        self.move_to_play = moves[i]

    def move(self):
        if self.move_to_play == "":
            return random.choice(moves)
        else:
            return self.move_to_play


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.s1 = 0
        self.s2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"\nPlayer 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print("Player 1 wins!")
            self.s1 += 1
            print(f"\nScores are now Player 1: {self.s1}"
                  f" and Player 2: {self.s2} \n")
        elif beats(move2, move1):
            print("Player 2 wins!")
            self.s2 += 1
            print(f"\nScores are now Player 1: {self.s1}"
                  f" and Player 2: {self.s2} \n")
        else:
            print(f"No winners! Play again! \n"
                  f"Scores are still Player 1: {self.s1}"
                  f" and Player 2: {self.s2} \n")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("\n|--Game start!--|\n")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.s1 > self.s2:
            print (f"Player 1 wins with {self.s1} points!")
        elif self.s2 > self.s1:
            print (f"Player 2 wins with {self.s2} points!")
        else:
            print("It's a Mexican Standoff...Nobody wins!")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), ReflectPlayer())
    game.play_game()