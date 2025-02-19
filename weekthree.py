# Function to count vowels in a given string (Question 1)
def count_vowels(text):   
    vowels = "aeiouAEIOU"
    count = sum(1 for char in text if char in vowels)
    return count

text = input("Enter a string to count vowels: ")
print("Vowel Count:", count_vowels(text))


# Function to find the maximum number in a list (Question 2)
def find_maximum(list1):
    max_value = list1[0]  # Assume first element is the largest
    for num in list1:
        if num > max_value:
            max_value = num
    return max_value

list1 = list(map(int, input("Enter numbers separated by space: ").split()))
print("Max Number:", find_maximum(list1))


# Function to print multiplication table of a given number (Question 3)
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

n = int(input("Enter a number for multiplication table: "))
multiplication_table(n)


# Function to find the longest word in a sentence (Question 4)
def largest_word(sentence):
    words = sentence.split()
    longest_word = max(words, key=len)  # Finds the longest word
    return longest_word

sentence = input("Enter a sentence to find the longest word: ")
print("Longest Word:", largest_word(sentence))


# Function to calculate the sum of a list of numbers (Question 5)
def sum_of_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total  

numbers = list(map(int, input("Enter numbers separated by space: ").split()))
print("Sum of List:", sum_of_list(numbers))


# Function to convert a sentence to title case (Question 6)
def to_title_case(sentence):
    return sentence.title()

sentence = input("Enter a sentence to convert to title case: ")
print("Title Case:", to_title_case(sentence))


# Function to check if a word is a palindrome (Question 7)
def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word to check if it's a palindrome: ")
print("Palindrome Check:", is_palindrome(word))


# Function to count occurrences of each character in a string (Question 8)
def char_count(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

s = input("Enter a string to count character occurrences: ")
print("Character Count:", char_count(s))