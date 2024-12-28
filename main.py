# Functions
# Count how many words are in a string
def word_count(string):
    split = string.split()
    count = 0
    for str in split:
        count += 1
    return count

# Count how many letters are in a string
def count_letters(string):
    # exclude = "[]{}<>.?!@#$%^&*()~`-_,'\":\\n;/" # Exclude string to tell what characters to exclude, not used right now becuase .isalpha is better
    string = string.lower()
    letters = {}
    for letter in string:
        if not letter.isalpha():
            pass
        elif letter in letters:
            letters[letter] = letters[letter] + 1
        else:
            letters[letter] = 1
    return letters

# returns the number value from a dictionary for sorting, used by sort_dictionary function
def sort_on(dict):
    return dict["number"] 

# Takes a dictionary with value:num entries and sorts it by num and returns a sorted dictionary
def sort_dictionary(dict):
    sorted = {}
    # Create a temporary list and populate it with dictionaries that have the letter:value and number:value as entries so that the dictionary can be sorted by number:value
    temp = []
    for key in dict:
        temp.append({"letter":key, "number": dict[key]})

    # Sort using the .sort function
    temp.sort(reverse = True, key=sort_on)

    # Put this back into a dictionary the way that it was input
    for dict_tmp in temp:
        sorted[dict_tmp["letter"]] = dict_tmp["number"]

    return sorted

# Print a formatted report for the current book
def print_report(word_count, letter_count, book_name):
    print(f"--- Begin report of {book_name} ---")
    print(f"{word_count} words found in the document\n")
    letter_count = sort_dictionary(letter_count)
    for key in letter_count:
        print(f"The '{key}' character was found {letter_count[key]} times")


def main(book):
    if book == "" or book is None:
        book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    wc = word_count(file_contents)
    lc = count_letters(file_contents)
    print_report(wc, lc, book)



main(input("Input the directory of a book to report on, or press Enter to start processing Frankenstein: "))