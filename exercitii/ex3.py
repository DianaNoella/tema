#Write a program to remove characters from a string starting from zero up to n and return a new string.

#For example:

#remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
#remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
#Note: n must be less than the length of the string.

def remove_char(n):
    word = input("Write a word")
    word = list(word)
    for i in word[n+1:]:
        print(i)

remove_char(4)