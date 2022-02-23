import random


def hangman(word):
    wrong = 0
    stages = ["",
              "---------        ",
              "|        |       ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       / \      ",
              "|                ",
              ]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to my Hangman Game!")
    print((" ".join(board)))

    while wrong < len(stages) - 1:
        print("\n")
        char = input("Guess a letter:  ")
        if char in remaining_letters:
            char_ind = remaining_letters.index(char)
            board[char_ind] = char
            remaining_letters[char_ind] = "$"
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))

        if "_" not in board:
            print("You win !!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong]))
        print("\nYou lose! It was {}".format(word))


word_list = ["abruptly", "absurd", "abyss", "avenue",
             "crypt", "cycle", "jockey", "lucky", "oxygen", "subway"]
word = random.choice(word_list)
hangman(word)
