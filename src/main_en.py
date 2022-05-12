## This code allows the users to play hangman. It provides an interface with which two or more players can interact, keeping track of the game

# The first player must type a random word
word = input("Give me a word! " )

# This snippet of code counts the letters in the word in order to create a board
# It then prints out as many lines as letters in the word 
count = 0
for letters in word: 
    count += 1

hidden_word = ["_"] * count
print(' '.join(map(str,hidden_word)))

# The second player (or players) have 6 lives
number_lives = 6

# They can introduce letters 1 by 1 
# each time they get a letter right, it will be printed and take the place of the respective line 
# each time they get a letter wrong, a life will be taken away from them 
while number_lives > 0:
    if "_" in (hidden_word):
        letter_guessed = input("Give me a letter: ")
        try :
            word.index(letter_guessed)
        except ValueError as e: 
            number_lives -= 1
            print("You lost a life, you have ", number_lives, "lives left")
        else: 
            for i in range(len(word)):
                if letter_guessed == word[i] :
                    hidden_word[i] = letter_guessed
            print(' '.join(map(str,hidden_word)))
    else:
        print("You guessed the word:", word, ", you win!" )
        break
else: 
    print("You are out of lives")