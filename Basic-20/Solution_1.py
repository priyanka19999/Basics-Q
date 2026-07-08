# Anagrams Game: Build a Scrambled Word Game using Python

import random
f = open("word.txt", "r")
a = f.readline()
words = a.split(",")
print(words)
# words = ["ironman", "thor", "hawkeye", "wanda", "vision"]

single_word = random.choice(words)
print(single_word)

jumble = "".join(random.sample(single_word, len(single_word)))
# print(jumble)

chances = 3
print("~" * 30)
print("~~~ Avengers Jumble Bumble ~~~")
print("~" * 30)
while chances!= 0:
    print(jumble)
    guess = input("enter your guessed word: ").lower()
    if guess == single_word:
        print("Correct Guess! !")
        print("You Won")
        break
    else:
        chances -= 1
        print("Incorrect Guess!!")
        print("Remaining chances are:", chances)
        
else:
    print("all your chances are exhausted")
    print("you lose")
    print("The correct word is: ",single_word)
    

print("Thank you for playing")

# Output:
# She-Hulk
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ~~~ Avengers Jumble Bumble ~~~
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  khHeul-S
# enter your guessed word: lkkl
# Incorrect Guess!!
# Remaining chances are: 2
#  khHeul-S
# enter your guessed word: ppp
# Incorrect Guess!!
# Remaining chances are: 1
#  khHeul-S
# enter your guessed word: iii
# Incorrect Guess!!
# Remaining chances are: 0
# all your chances are exhausted
# you lose
# The correct word is:   She-Hulk
# Thank you for playing