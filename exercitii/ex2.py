#Write a program to accept a string from the user and display characters that are present at an even index number.

#For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

chosen_word = input("Please write a word")
length_word = len(chosen_word)

for i in range(0, length_word-1, 2):
   print(chosen_word[i])