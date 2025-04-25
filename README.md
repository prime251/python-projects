# python-projects

## Project: Guess the Number Game  
**Date**: April 23, 2025  
**Language**: Python

### What the Project Does  
This is a number guessing game. The user tries to guess the number the computer picked (1–100).

### What I Learned  
- Using `while` loops  
- Using `input()` and `if/else`  
- Using `random.randint()`

### What Was Difficult  
Validating user input was difficult, especially ensuring that the user only entered numbers and handling invalid inputs, such as non-numeric values.

### What I Want to Improve  
Add different difficulty levels (easy, medium, hard) where the number range and/or the number of attempts changes.  
For example, the player could have 10 attempts for easy, 7 attempts for medium, and 5 attempts for hard.
___________________________________________________________________________________________________________________________________________________________________________________________________

## Project: Guess the Word (Hangman)  
**Date**: April 24, 2025  
**Language**: Python

### What the Project Does  
This is a Hangman-style word guessing game.  
The computer randomly selects a word from a word list, and the user tries to guess it letter by letter before the hangman drawing is completed.

### What I Learned  
- Replacing letters in a blank list  
- showing the user the answer when lost
- Comparing lists with `if blank_list == chosen_word`
- using variables

### What Was Difficult  
Managing global variables was a little confusing at first.  
Also, understanding how to match and reveal correct letters in the word using `enumerate()` took some practice.

### What I Want to Improve  
- showing what the user already guessed
