# Functions
# Count how many words are in a string
def word_count(string):
    split = string.split()
    count = 0
    for str in split:
        count += 1
    return count