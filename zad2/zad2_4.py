#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
import random
import getpass
import argparse
import re


class Game:
    def __init__(self, players):
        self.players = players

    def _play(self):
        print("The game has started!")


class Hangman(Game):
    def __init__(self, players, difficulty):
        super().__init__(players)
        self._difficulty = difficulty
        self._guessed_letters = []

    def _game_loop(self):
        wrong_guesses = 0

        while True:
            if wrong_guesses == self._difficulty_settings():
                print("Game over!")
                return

            result = ''
            for letter in self._word:
                if letter in self._guessed_letters:
                    result += letter
                else:
                    result += '_'

            print(f"Mistakes left: {self._difficulty_settings() - wrong_guesses}")
            print(f"Word: {result}")
            print(f"Guessed letters: {sorted(self._guessed_letters)}")

            if result == self._word:
                print("You win!")
                return

            guess = input("Enter a new letter: ")

            if guess in self._guessed_letters:
                print(f"Letter {guess} already was already guessed.")
                continue

            if re.match("^[a-zA-Z]$", guess):
                if guess in self._word:
                    print("Good guess!")
                else:
                    print("The word doesn't contain this letter.")
                    wrong_guesses += 1
                self._guessed_letters.append(guess)
            else:
                print("Incorrect input!")

    def _difficulty_settings(self):
        if self._difficulty == 'beginner':
            return 8
        elif self._difficulty == 'intermediate':
            return 5
        elif self._difficulty == 'advanced':
            return 3

    def play_game(self):
        self._play()
        print(f"Difficulty: {self._difficulty}. Allowed mistakes: {self._difficulty_settings()}")
        if self.players == 1:
            print("1 player mode. The word will be randomly chosen for you.")
            with open('hangman_words.txt') as words_file:
                words = words_file.readlines()
                self._word = random.choice(words).rstrip()
        else:
            self._word = getpass.getpass("2 player mode. Player 1, please pick a word: ")
            if not re.match("^[a-zA-Z]+$", self._word):
                print(f"Wrong input: {self._word}, only English alphabet letters are allowed")
                exit(1)

        self._game_loop()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--num-players', '-n', required=True, type=int)
    
    parser.add_argument('--difficulty', '-d', default='beginner',
                        choices=['beginner', 'intermediate', 'advanced'],
                        type=str)

    return parser.parse_args()


def main():
    args = parse_args()
    Hangman(args.num_players, args.difficulty).play_game()


if __name__ == '__main__':
    main()
