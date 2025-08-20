# global variables
vowel = "aeiouAEIOU"

###########

'''Write a program that counts up the number of vowels 
[a, e, i, o,u] contained in the string.'''

def count_vowels(text):
    cnt=0
    for char in text:
        if char in vowel:
            cnt+=1
    return cnt

# print(count_vowels('lorem ipsum'))

############

'''Fill an array of 5 elements from the user, Sort it in
descending and ascending orders then display the output.'''

def sort_numbers():
    input_arr=[]
    for i in range(5):
        element = input("Enter number: ").replace(' ', '')
        if element.isnumeric():
            input_arr.append(int(element))
        else:
            print('Please enter a valid number')
            
    print("ascending order:", sorted(input_arr))
    print("descending order:", sorted(input_arr, reverse=True)) 
# we can also use arr.sort(), which modifies the list in place

# sort_numbers()

############

'''Write a program that prints the number of times 
the string 'iti' occurs in anystring.'''

def count_iti(text: str):
    return text.lower().count('iti')
#note: iti doesnt  >>> overlap <<<

# print(count_iti('ITIti is a good iti institute'))
############

'''Write a program that remove all vowels from the
input word and generate a brief version of it'''

def remove_vowels(text):
    filtered_text = filter(lambda char: char not in vowel, text)
    return ''.join(filtered_text)
# can also loop with index, and remove all vowels

# print(remove_vowels('lorem ipsum'))

############

'''Write a program that prints the locations of 
"i" character in string you added'''

def locate_i(text):
    return [i for i in range(len(text)) if text[i] in 'iI']

# print(locate_i('lorem ipsum'))  

#############

'''Write a program that generate a multiplication
 table from 1 to the number passed.'''

def multiplication_tables():
    n = int(input("Enter number : "))
    arr = []
    for i in range(1, n+1):
        arr.append([i*j for j in range(1,i+1)])
    return arr

# print(multiplication_tables())

############

'''Write a program that build a Mario pyramid'''

def mario_pyramid():
    n = int(input("Enter number : "))
    for i in range(n):
        print(' ' * (n-i-1) + '*' * (i+1))

# mario_pyramid()


