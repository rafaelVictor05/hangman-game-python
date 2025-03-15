# Hangman Game

A simple hangman game written in Python.

![Captura de Tela do Jogo](https://imgur.com/yUaxuSh)

## Description

This project is a classic hangman game implemented in Python. It randomly selects a word from a list of English words loaded from a file (`words.txt`), and the player must guess the word letter by letter. With each wrong guess, a part of the hangman is drawn. The game ends when the player either guesses the word or runs out of lives.

The `words.txt` file used in this project was sourced from the [dwyl/english-words GitHub repository](https://github.com/dwyl/english-words/blob/master/words.txt).

## Requirements

- Python 3.x installed on your system.

## Files

- **game.py**: The main script to run the game.  
- **words.txt**: A text file containing a list of English words (one word per line), sourced from the [dwyl/english-words repository](https://github.com/dwyl/english-words/blob/master/words.txt).

## How to Run

1. Clone or download the repository.  
2. Ensure `game.py` and `words.txt` are in the same directory.  
3. Open your terminal and navigate to the project folder.  
4. Run the game with:

   ```bash
   python game.py
