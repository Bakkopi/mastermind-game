# Mastermind Game

This project is a Python implementation of the classic Mastermind game. The game generates a secret code consisting of 4 colors, and the player's objective is to guess the code within a specific number of attempts. The game provides feedback after each attempt to assist in refining the guesses.

## How to Play

1. Execute the Python script using a compatible Python interpreter.
2. The program will prompt for a username (up to 20 characters) to appear on the leaderboard.
3. Players are given a predetermined number of attempts to guess the secret code.
4. Enter a combination of 4 colors by typing the first letter of each color.
5. After each attempt, the feedback will indicate the accuracy of the guess.
6. Keep guessing until the code is broken or the attempts are exhausted.

## Features

- The secret code is randomly generated for each game.
- Feedback on each attempt specifies the number of correct colors in the right and wrong positions.
- The interface is designed for easy user interaction.
- A leaderboard keeps track of attempts made by players to solve the code.
- The game can be replayed to enjoy the challenge again.

## Example Outputs

Shown below are sample outputs that players might encounter during the gameplay:

```plaintext
WELCOME TO MASTERMIND!  \('o' )/

Crack the secret 4-colour code to win!
Enter the first letter for each colour (Colours can be repeated!)

...

Pick a combination of 4:
Red(R), Yellow(Y), Green(G), Blue(B), Violet(V), Cyan(C)

Attempt 1
Colour 1: R
Colour 2: Y
Colour 3: G
Colour 4: B

Your combination: (R) (Y) (G) (B)
Colour RIGHT, position WRONG: 2
Colour RIGHT, position RIGHT: 1

It's alright! Try again. q(^-^q)

...

CODE BROKEN

You finished it in 7 attempts. Good job!

          LEADERBOARD

 #              Username        Attempts
 1               Alice              6
 2               Bob                7
 3               Eve               12
 ...
