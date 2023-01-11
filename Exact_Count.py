from collections import Counter
import string
import random
import time
import urllib.request  # the lib that handles the url stuff

def exact_counter(link):
    start_exact = time.time()
    operations = 0
    letter_num_dict = {}
    for letter in string.ascii_uppercase:
        letter_num_dict[letter] = 0
    text_flag = False #Flag that checks if we're reading a Gutenberg header or the actual book
    for line in urllib.request.urlopen(link):
        line = line.decode('utf-8')
        if "*** S" in line:
            text_flag = True
        if "*** E" in line:
            break
        if text_flag:
            if len(line) == 2:
                continue
            else:
                for char in line:
                    operations +=1
                    if char in string.ascii_lowercase or char in string.ascii_uppercase:
                        char = char.upper()
                        letter_num_dict[char] += 1
        
    k = Counter(letter_num_dict)
    high = k.most_common(3)
    print(operations)
    print(high)
    print("\n")


links = ["https://www.gutenberg.org/files/62615/62615-0.txt", "https://www.gutenberg.org/cache/epub/30/pg30.txt", "https://www.gutenberg.org/files/62383/62383-0.txt"]
for link in links:
    exact_counter(link)
