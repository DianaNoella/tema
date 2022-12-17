import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 3
    print("Let's play Hangman!")
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        print("You have", tries, "tries")
        print(word_completion)

        guess = input("Please guess a letter or word:").upper()
        if not guess.isalpha():
            print("Not a valid guess")
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
                continue

            if guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
                continue

            print("Good job,", guess, "is in the word!")
            guessed_letters.append(guess)
            word_as_list = list(word_completion)
            for index, letter in enumerate(word):
                if letter == guess:
                    word_as_list[index] = guess
            word_completion = "".join(word_as_list)
            guessed = "_" not in word_completion
            continue

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
                continue

            if guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
                continue

            guessed = True
            word_completion = word
            break

        else:
            print("Not a valid guess")
            continue


    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries.")

def main():
    word = get_word()
    play(word)

if __name__ == "__main__":
    main()
