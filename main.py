# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    with open(filename, 'r') as f:
        lines = f.read()
        print(lines)

def count_words():
    with open('story.txt', 'r') as f:
        lines = f.read()
        print(lines)
    # [assignment] Add your code here
        lines = lines.split()
        word_counts = [(word, lines.count(word)) for word in set(lines)]
        sorted_word_counts = sorted(word_counts, key=lambda x: x[1], reverse=True)
        print(sorted_word_counts)

read_file_content('story.txt')
count_words()
# Read-from-file
