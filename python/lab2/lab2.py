
############

'''Write a function that accepts two arguments (length, start) 
generate an array of a specific length filled with integer numbers
increased by one from start.'''

def generate_array(length, start):
    return [i for i in range(start, length+start)]

# print(generate_array(5,3))

############

'''write a function that takes a number as an argument and if the
number divisible by 3 return "Fizz" and if it is divisible by 5 return
"Buzz" and if is is divisible by both return "FizzBuzz"'''

def fizz_buzz(n):
    output = ''
    output += 'Fizz' if n%3==0 else ''
    output += 'Buzz' if n%5==0 else ''
    return output

# print(fizz_buzz(15))

############

'''Write a function which has an input of a string from user then it
will return the same string reversed.'''

def reverse_string(text: str):
    return ''.join(reversed(text))

# print(reverse_string('lorem ipsum'))

############

''' Ask the user for his name then confirm that he has entered his
name(not an empty string/integers). then proceed to ask him for
his email and print all this data (Bonus) check if it is a valid email
or not'''

def get_user_info():
    name = input("please input your name: ")
    if not name.replace(" ", "").isalpha():
        print("Please enter a valid name next time...")
        return
    email = input("Confirmed. Now please enter your e-mail: ")
    # easiest way for email validation is with regex, but we can also
    # make a simple string parser that checks for main substrings ex: provider, suffix, @, ., etc.
    if email.count('@') != 1 or email.count('.') <= 0:
        print("Please enter a valid email next time...")
        return

    print("User Information:")
    print("Name: " + name)
    print("Email: " + email)

# get_user_info()

############

'''Write a function that takes a string and prints the
longest alphabetical ordered substring occurred For example, if
the string is 'abdulrahman' then the output is: Longest substring in
alphabetical order is: abdu'''

def longest_increasing_substring(s):
    s = s.replace(" ", "")  
    longest = current = ''
    for char in s:
        if not current or char >=current[-1]:
            current += char
        else:
            longest = max(longest, current, key=len)
            current = char
    longest = max(longest, current, key=len)
    return longest

# print(longest_increasing_substring('lorem ipsum dolor sit amet'))


############

'''Write a program which repeatedly reads numbers until the user
enters “done”.
○ Once “done” is entered, print out the total, count, and
average of the numbers.
○ If the user enters anything other than a number, detect their
mistake, print an error message and skip to the next number.'''

def get_average():
    tot = cnt = 0
    print("Enter numbers one by one, type 'done' to finish:")
    while True:
        user_input = input()
        if user_input.lower() == 'done':
            break
        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue
        num = int(user_input)
        tot += num
        cnt += 1
        
    print(f"Total: {tot} \nCount: {cnt} \nAverage: {round(tot/cnt, 2) if cnt else 0}")

# get_average()

############

'''Word guessing game (hangman)
○ A list of words will be hardcoded in your program, out of
which the interpreter will
○ choose 1 random word.
○ The user first must input their names
○ Ask the user to guess any alphabet. If the random word
contains that alphabet, it
○ will be shown as the output(with correct placement)
○ Else the program will ask you to guess another alphabet.
○ Give 7 turns maximum to guess the complete word.'''

import random as rnd
from words import WORD_LIST

def hangman():
    word = rnd.choice(WORD_LIST)
    guessed = [False] * len(word)
    turns = 7
    while(turns):
        print(f"Current word: {''.join([char if guessed[i] else '_' for i, char in enumerate(word)])}")
        guess = input('Your guess: ')
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabet.")
            continue
        
        guessed = list(map(lambda x: x[1] or word[x[0]] == guess, enumerate(guessed)))

        if all(guessed):
            print(f"Congratulations! You've guessed the word: {word}")
            return
        turns -= 1
        print(f"Wrong guess! Turns left: {turns}")
    print(f"Game over! The word was: {word}")

# hangman()
