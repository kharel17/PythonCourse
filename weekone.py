# Assignment Week 1
# Question 1: Convert float to integer and string
float_num = float(input("Enter a decimal number: "))
int_num = int(float_num)
str_num = str(float_num)
print(f"Original float: {float_num}")
print(f"Converted to integer: {int_num}")
print(f"Converted to string: \"{str_num}\"")

# Question 2: Extract initials from full name
full_name = input("Enter your full name: ")
names = full_name.split()
if len(names) >= 2:
    initials = names[0][0].upper() + "." + names[-1][0].upper()
    print(f"Your initials are: {initials}")
else:
    print("Please enter both first and last name.")

# Question 3: Reverse a string
user_string = input("Enter a string: ")
reversed_string = user_string[::-1]
print(f"Reversed string: {reversed_string}")

# Question 4: Extract substring from a given index


# Question 5: Extract domain from email address
email = input("Enter your email address: ")
if "@" in email:
    domain = email.split("@")[1]
    print(f"Domain: {domain}")
else:
    print("Invalid email address.")

# Question 6: Swap first and last character of a word
word = input("Enter a word: ")
if len(word) > 1:
    swapped_word = word[-1] + word[1:-1] + word[0]
    print(f"Modified word: {swapped_word}")
else:
    print("Word must have at least two characters.")
