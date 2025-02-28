import os

# 1️ Function to Read File Content
def read_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# 2️ Function to Write Content to a File
def write_to_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

# 3️ Function to Find the Longest Word in a File
def find_longest_word(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
    return max(words, key=len) if words else None

# 4️ Function to Check if a File is Empty
def check_file_empty(file_path):
    return os.stat(file_path).st_size == 0  # Returns True if file size is 0

# 5️ Function to Reverse File Content and Save to a New File
def reverse_file_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()[::-1]  # Reverse content

    new_file_path = os.path.join(os.path.dirname(file_path), "reversed.txt")
    with open(new_file_path, 'w', encoding='utf-8') as new_file:
        new_file.write(content)

# 6️ Function to Convert List of Strings to Uppercase Using Lambda
def convert_to_uppercase(words):
    return list(map(lambda word: word.upper(), words))

# 7️ Function to Filter Even-Length Words Using Lambda
def filter_even_length_words(words):
    return list(filter(lambda word: len(word) % 2 == 0, words))

# 8️ Function to Process a File and Convert Words to Uppercase Using Lambda
def process_file_with_lambda(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    processed_lines = [" ".join(map(lambda word: word.upper(), line.split())) for line in lines]

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("\n".join(processed_lines))

if __name__ == "__main__":
    file_path = r"C:\Users\DELL.DESKTOP-9SPGAH9\Desktop\LDR 300\Inter.txt"

    # Read and print content
    print("File Content:")
    print(read_file_content(file_path))

    # Write to file
    write_to_file(file_path, "Hello World! Python is fun.")

    # Find longest word
    print("Longest Word:", find_longest_word(file_path))

    # Check if file is empty
    print("Is File Empty:", check_file_empty(file_path))

    # Reverse content and save to 'reversed.txt'
    reverse_file_content(file_path)
    print("Reversed file content saved.")

    # Convert list of words to uppercase
    words_list = ["hello", "world", "python", "lambda"]
    print("Uppercase Words:", convert_to_uppercase(words_list))

    # Filter even-length words
    print("Even-Length Words:", filter_even_length_words(words_list))

    # Process file and convert words to uppercase
    process_file_with_lambda(file_path)
    print("File content converted to uppercase.")
